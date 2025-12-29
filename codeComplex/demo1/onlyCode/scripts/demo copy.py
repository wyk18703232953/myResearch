import time
import re
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from scipy.optimize import curve_fit
import os
import sys
import dis
from openai import OpenAI
import config  # 假设你有一个 config.py 文件

# ==========================================
# 核心工具函数
# ==========================================

def format_bytecode_count(count):
    """格式化字节码计数显示"""
    if count >= 1e6:
        return f"{count/1e6:.2f}M"
    elif count >= 1e3:
        return f"{count/1e3:.2f}K"
    else:
        return f"{int(count)}"

def extract_upper_envelope(n, y, window_fraction=0.10):
    """
    提取数据的上包络线（最坏情况点）。
    原理：将数据分段，每段只取 y 值最大的点。
    
    Args:
        n: 输入规模数组
        y: 字节码计数数组
        window_fraction: 窗口大小占总数据量的比例
        
    Returns:
        (n_envelope, y_envelope): 筛选后的用于拟合的数据点
    """
    # 确保按 n 排序
    sorted_indices = np.argsort(n)
    n_sorted = n[sorted_indices]
    y_sorted = y[sorted_indices]
    
    # 如果数据点太少，不进行过滤
    if len(n) < 10:
        return n_sorted, y_sorted

    n_env = []
    y_env = []
    
    # 动态计算窗口大小，至少包含3个点，防止窗口过小
    window_size = max(3, int(len(n) * window_fraction))
    
    # 使用滑动窗口（无重叠）提取局部最大值
    for i in range(0, len(n), window_size):
        # 切片当前窗口
        end_idx = min(i + window_size, len(n))
        n_chunk = n_sorted[i:end_idx]
        y_chunk = y_sorted[i:end_idx]
        
        if len(y_chunk) == 0: continue
            
        # 找到该窗口内 y 最大的索引
        max_local_idx = np.argmax(y_chunk)
        
        n_env.append(n_chunk[max_local_idx])
        y_env.append(y_chunk[max_local_idx])
        
    return np.array(n_env), np.array(y_env)

def count_dynamic_bytecode(code_str, globals_dict, locals_dict):
    """
    执行代码并统计动态字节码指令数
    """
    compiled_code = compile(code_str, '<string>', 'exec')
    instruction_count = 0
    line_instruction_counts = {}
    
    def count_instructions_per_line(code_obj):
        current_line = None
        line_counts = {}
        for inst in dis.get_instructions(code_obj):
            if inst.starts_line:
                current_line = inst.starts_line
            if current_line is not None:
                if current_line not in line_counts: line_counts[current_line] = 0
                line_counts[current_line] += 1
        for line, count in line_counts.items():
            line_instruction_counts[(code_obj, line)] = count
    
    def process_code_objects(code_obj):
        count_instructions_per_line(code_obj)
        for const in code_obj.co_consts:
            if hasattr(const, 'co_code'):
                process_code_objects(const)
    
    process_code_objects(compiled_code)
    
    def trace_function(frame, event, arg):
        nonlocal instruction_count
        if event == 'line':
            code_obj = frame.f_code
            line_num = frame.f_lineno
            if (code_obj, line_num) in line_instruction_counts:
                instruction_count += line_instruction_counts[(code_obj, line_num)]
        return trace_function
    
    try:
        original_trace = sys.gettrace()
        sys.settrace(trace_function)
        exec(compiled_code, globals_dict, globals_dict)
        sys.settrace(original_trace)
        return instruction_count
    except Exception as e:
        sys.settrace(original_trace)
        # fallback: count static
        instruction_count = 0
        exec(compiled_code, globals_dict, globals_dict)
        def count_all(code_obj):
            nonlocal instruction_count
            for _ in dis.get_instructions(code_obj): instruction_count += 1
            for const in code_obj.co_consts:
                if hasattr(const, 'co_code'): count_all(const)
        count_all(compiled_code)
        return instruction_count

# ==========================================
# 复杂度模型定义
# ==========================================

def constant_model(n, a):
    return np.full_like(n, a, dtype=np.float64)

def linear_model(n, a, b):
    return a * n + b

def quadratic_model(n, a, b, c):
    return a * n**2 + b * n + c

def cubic_model(n, a, b, c, d):
    return a * n**3 + b * n**2 + c * n + d

def logarithmic_model(n, a, b):
    return a * np.log(n) + b

def n_log_n_model(n, a, b):
    return a * n * np.log(n) + b

def exponential_model(n, a, b):
    return a * np.exp(np.clip(b * n, -100, 100))

def power_model(n, a, b):
    return a * np.power(n, b)

# 模型注册表
MODELS = {
    'O(1)': {'func': constant_model, 'params': 1},
    'O(n)': {'func': linear_model, 'params': 2},
    'O(n^2)': {'func': quadratic_model, 'params': 3},
    'O(n^3)': {'func': cubic_model, 'params': 4},
    'O(log n)': {'func': logarithmic_model, 'params': 2},
    'O(n log n)': {'func': n_log_n_model, 'params': 2},
    'O(2^n)': {'func': exponential_model, 'params': 2},
    'O(n^k)': {'func': power_model, 'params': 2}
}

# ==========================================
# 大模型调用
# ==========================================

def call_large_model(original_code, api_key=None, base_url=None):
    if api_key is None:
        api_key = "sk-3sNQAO5ydpVp29WWoCqvM7Ajqzd1I5WKOpe29cpoT3DoMrZe"
    if base_url is None:
        base_url = "https://yunwu.ai/v1"
    
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    system_prompt = "你是一位算法专家。将Python程序转换为无input()、可参数化规模n的程序。"
    user_prompt = f"""请将以下Python程序转换为一个无input()、包含 main(n) 函数的程序。
    
    要求：
    1. 移除 input()。
    2. 函数 main(n) 封装逻辑，n为规模。
    3. 根据 n 生成测试数据。
    4. 仅输出代码。
    
    原始代码：
    ```python
    {original_code}
    ```
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-5.1", 
            temperature=0.0,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        output = response.choices[0].message.content.strip()
        if output.startswith('```python'): output = output[9:]
        if output.endswith('```'): output = output[:-3]
        return output.strip()
    except Exception as e:
        raise Exception(f"API调用失败: {e}")

# ==========================================
# 核心分析逻辑
# ==========================================

def calculate_aic(n_samples, rss, num_params):
    """计算 AIC"""
    if n_samples <= num_params + 1 or rss <= 0:
        return float('inf')
    
    aic = n_samples * np.log(rss / n_samples) + 2 * num_params
    aic_c = aic + (2 * num_params * (num_params + 1)) / (n_samples - num_params - 1)
    return aic_c

def process_code_file(code_path, force_reanalyze=False):
    if not os.path.exists(code_path): return
    
    file_name = os.path.basename(code_path)
    base_name = os.path.splitext(file_name)[0]
    result_dir = f"{config.constant_results_base_dir}/results_{base_name}"
    os.makedirs(result_dir, exist_ok=True)
    
    # 1. 代码生成与读取
    generated_code_path = os.path.join(result_dir, f"generated_{base_name}.py")
    if os.path.exists(generated_code_path) and not force_reanalyze:
        with open(generated_code_path, 'r', encoding='utf-8') as f:
            generated_code = f.read()
    else:
        with open(code_path, 'r', encoding='utf-8') as f: original_code = f.read()
        print(f"正在为 {base_name} 生成测试代码...")
        generated_code = call_large_model(original_code)
        with open(generated_code_path, 'w', encoding='utf-8') as f:
            f.write(generated_code)

    # 2. 数据收集
    test_results = []
    temp_results_path = os.path.join(result_dir, "temp_results.npz")
    
    if not force_reanalyze and os.path.exists(temp_results_path):
        test_results = np.load(temp_results_path)['results'].tolist()
        start_n = int(test_results[-1][0]) + config.step if test_results else config.start_n
    else:
        start_n = config.start_n

    if start_n <= config.max_n:
        print(f"开始分析 {base_name} (n={start_n} -> {config.max_n})...")
        try:
            for n in range(start_n, config.max_n + 1, config.step):
                run_code = f"{generated_code}\nmain({n})"
                bytecode_count = count_dynamic_bytecode(run_code, {}, {})
                test_results.append((n, bytecode_count))
                
                if len(test_results) % 10 == 0:
                    print(f"  n={n}, count={bytecode_count}")
                    np.savez(temp_results_path, results=test_results)
        except Exception as e:
            print(f"执行出错: {e}")
        finally:
            np.savez(temp_results_path, results=test_results)

    # 3. 拟合准备：数据提取与过滤
    if len(test_results) < 5:
        print("数据点不足，跳过拟合。")
        return

    data = np.array(test_results)
    n_raw = data[:, 0]
    y_raw = data[:, 1]

    # [新增步骤] 提取最坏情况点（上包络线）用于拟合
    # 我们只使用这些“峰值”点进行曲线拟合，从而忽略“最好情况”或“平均情况”的干扰
    n_fit, y_fit = extract_upper_envelope(n_raw, y_raw, window_fraction=0.08)
    
    print(f"数据过滤: 原始点数 {len(n_raw)} -> 用于最坏情况拟合的点数 {len(n_fit)}")

    # 归一化因子 (基于用于拟合的数据)
    n_scale = np.max(n_fit)
    y_scale = np.max(y_fit)
    
    n_norm = n_fit / n_scale
    y_norm = y_fit / y_scale

    best_aic = float('inf')
    best_model_name = None
    fit_report = {}
    predict_funcs = {}

    print("最坏复杂度拟合分析中...")
    
    for name, model_info in MODELS.items():
        func = model_info['func']
        k = model_info['params']
        
        try:
            # 初始参数猜测
            p0 = [1.0] * k 
            if name == 'O(n^2)': p0 = [1.0, 1.0, 0.0]
            if name == 'O(log n)': p0 = [0.5, 0.0]

            # 使用过滤后的(最坏情况)数据进行拟合
            popt_norm, _ = curve_fit(func, n_norm, y_norm, p0=p0, maxfev=10000)
            
            # 创建预测闭包
            def make_predictor(f, params, ns, ys):
                return lambda x: f(x / ns, *params) * ys

            predictor = make_predictor(func, popt_norm, n_scale, y_scale)
            predict_funcs[name] = predictor
            
            # 评估：使用 fitting data (最坏情况点) 计算误差
            y_pred_fit = predictor(n_fit)
            
            # 计算 RSS 和 R2
            residuals = y_fit - y_pred_fit
            rss = np.sum(residuals**2)
            
            ss_tot = np.sum((y_fit - np.mean(y_fit))**2)
            r2 = 1 - (rss / ss_tot) if ss_tot > 0 else 0
            
            # AIC 计算
            aic = calculate_aic(len(n_fit), rss, k)
            
            fit_report[name] = {
                'r2': r2,
                'aic': aic,
                'params_norm': popt_norm.tolist()
            }
            
            if aic < best_aic:
                best_aic = aic
                best_model_name = name
                
        except Exception as e:
            pass

    # 4. 绘图 (可视化过滤过程)
    plt.figure(figsize=(12, 7))
    
    # [可视化] 1. 绘制所有原始数据 (灰色，作为背景)
    plt.scatter(n_raw, y_raw, color='gray', s=10, alpha=0.3, label='All Executions (Raw)', zorder=1)
    
    # [可视化] 2. 绘制被选为“最坏情况”的数据点 (红色叉号)
    plt.scatter(n_fit, y_fit, color='red', marker='x', s=40, alpha=1.0, label='Worst Case Points (Filtered)', zorder=5)
    
    # [可视化] 3. 绘制拟合曲线
    x_smooth = np.linspace(min(n_raw), max(n_raw), 500)
    
    # 按AIC排序绘制图例
    sorted_models = sorted(fit_report.items(), key=lambda x: x[1]['aic'])
    
    for idx, (name, metrics) in enumerate(sorted_models):
        if name not in predict_funcs: continue
        
        y_smooth = predict_funcs[name](x_smooth)
        
        is_best = (name == best_model_name)
        linewidth = 3 if is_best else 1.5
        alpha = 1.0 if is_best else 0.4
        linestyle = '-' if is_best else '--'
        
        # 图例显示
        label = f"{name}"
        if is_best:
            label = f"★ Best Fit: {name} (AIC={metrics['aic']:.1f})"
            
        plt.plot(x_smooth, y_smooth, label=label, 
                 linewidth=linewidth, alpha=alpha, linestyle=linestyle, zorder=10 if is_best else 2)

    plt.title(f'Worst-Case Complexity Analysis: {base_name}', fontsize=14)
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Bytecode Instructions', fontsize=12)
    
    ax = plt.gca()
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format_bytecode_count(x)))
    
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.legend()
    
    plot_path = os.path.join(result_dir, f"complexity_plot_{base_name}.png")
    plt.savefig(plot_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    # 5. 保存报告
    report_path = os.path.join(result_dir, "report.json")
    with open(report_path, 'w') as f:
        json.dump({'best_model': best_model_name, 'details': fit_report}, f, indent=2)
    
    print(f"分析完成。最佳最坏情况模型: {best_model_name} (AIC={best_aic:.2f})")
    print(f"结果已保存至: {result_dir}")

def main():
    folder_path = config.constant_folder_path
    python_files = sorted([os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.py')])
    
    print(f"找到 {len(python_files)} 个文件。")
    for i, path in enumerate(python_files):
        print(f"\n--- 处理文件 {i+1}/{len(python_files)}: {os.path.basename(path)} ---")
        process_code_file(path, force_reanalyze=True)

if __name__ == "__main__":
    main()