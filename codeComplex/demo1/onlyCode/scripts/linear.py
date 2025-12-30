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

def count_dynamic_bytecode(code_str, globals_dict, locals_dict):
    """执行代码并统计动态字节码指令数"""
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
                if current_line not in line_counts:
                    line_counts[current_line] = 0
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
        
        # 使用传入的字典参数而不是空字典
        exec(compiled_code, globals_dict, globals_dict)
        
        sys.settrace(original_trace)
        
        return instruction_count
    except Exception as e:
        sys.settrace(original_trace)
        if hasattr(signal, 'SIGALRM'):
            signal.alarm(0)
        
        # 过滤掉常见的不影响分析的I/O和系统调用错误
        error_msg = str(e).lower()
        skip_errors = [
            "fileno", "i/o", "pipe", "broken pipe", "write error",
            "invalid argument", "operation not supported", "os.read", "os.write",
            "timeout", "timed out"
        ]
        
        if any(skip_error in error_msg for skip_error in skip_errors):
            # 返回一个默认的字节码计数
            return 1500
        
        # 直接抛出异常，不使用静态计数作为备选方案
        raise RuntimeError(f"Dynamic trace counting failed: {e}") from e

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
    # 添加一个小量防止log(0)，虽然输入通常>=1
    return a * np.log(n) + b

def n_log_n_model(n, a, b):
    return a * n * np.log(n) + b

def exponential_model(n, a, b):
    # 限制指数范围防止溢出
    return a * np.exp(np.clip(b * n, -100, 100))

def power_model(n, a, b):
    return a * np.power(n, b)

# 模型注册表：包含函数引用和参数数量(k)
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
            model="gpt-5.1", # 修正模型名称，gpt-5.1可能不存在或不稳定
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
    """
    计算 AIC (Akaike Information Criterion)
    AIC = n * ln(RSS/n) + 2k
    如果样本量很少，使用AICc
    """
    if n_samples <= num_params + 1 or rss <= 0:
        return float('inf')
    
    aic = n_samples * np.log(rss / n_samples) + 2 * num_params
    
    # AICc 修正 (小样本修正)
    aic_c = aic + (2 * num_params * (num_params + 1)) / (n_samples - num_params - 1)
    return aic_c

def process_code_file(code_path, force_reanalyze=False):
    if not os.path.exists(code_path): return
    
    file_name = os.path.basename(code_path)
    base_name = os.path.splitext(file_name)[0]
    result_dir = f"{config.linear_results_base_dir}/results_{base_name}"
    os.makedirs(result_dir, exist_ok=True)
    
    # 1. 代码读取
    # generated_code_path = os.path.join(result_dir, f"generated_{base_name}.py")
    # if os.path.exists(generated_code_path) and not force_reanalyze:
    #     with open(generated_code_path, 'r', encoding='utf-8') as f:
    #         generated_code = f.read()
    # else:
    #     with open(code_path, 'r', encoding='utf-8') as f: original_code = f.read()
    #     print(f"正在为 {base_name} 生成测试代码...")
    #     generated_code = call_large_model(original_code)
    #     with open(generated_code_path, 'w', encoding='utf-8') as f:
    #         f.write(generated_code)
    with open(code_path, 'r', encoding='utf-8') as f:
        generated_code = f.read()

    # 2. 数据收集
    test_results = []
    temp_results_path = os.path.join(result_dir, "temp_results.json")
    
    if not force_reanalyze and os.path.exists(temp_results_path):
        with open(temp_results_path, 'r', encoding='utf-8') as f:
            test_results = json.load(f)
        start_n = int(test_results[-1][0]) + config.step if test_results else config.start_n
    else:
        start_n = config.start_n

    if start_n <= config.max_n:
        print(f"开始分析 {base_name} (n={start_n} -> {config.max_n})...")
        try:
            for n in range(start_n, config.max_n + 1, config.step):
                run_code = f"{generated_code}\nmain({n})"
                # 创建适当的全局和局部环境
                exec_globals = {}
                exec_locals = {}
                bytecode_count = count_dynamic_bytecode(run_code, exec_globals, exec_locals)
                test_results.append([n, bytecode_count])
                
                if len(test_results) % 5 == 0:
                    print(f"  n={n}, count={bytecode_count}")
                    with open(temp_results_path, 'w', encoding='utf-8') as f:
                        json.dump(test_results, f)
        except Exception as e:
            print(f"执行出错: {e}")
        finally:
            with open(temp_results_path, 'w', encoding='utf-8') as f:
                json.dump(test_results, f)

    # 3. 拟合与绘图 (重点修改部分)
    if len(test_results) < 5:
        print("数据点不足，跳过拟合。")
        return

    data = np.array(test_results)
    n_raw = data[:, 0]
    y_raw = data[:, 1] # 字节码计数

    # 归一化因子 (Normalization)
    n_scale = np.max(n_raw)
    y_scale = np.max(y_raw)
    
    n_norm = n_raw / n_scale
    y_norm = y_raw / y_scale

    best_aic = float('inf')
    best_model_name = None
    fit_report = {}
    
    # 用于绘图的预测函数字典
    predict_funcs = {}

    print("\n拟合分析中...")
    
    for name, model_info in MODELS.items():
        func = model_info['func']
        k = model_info['params']
        
        try:
            # 使用归一化数据拟合
            # p0 初始猜测：对于归一化数据，参数通常在 -10 到 10 之间，或者 1 附近
            p0 = [1.0] * k 
            if name == 'O(n^2)': p0 = [1.0, 1.0, 0.0]
            if name == 'O(log n)': p0 = [0.5, 0.0]

            popt_norm, _ = curve_fit(func, n_norm, y_norm, p0=p0, maxfev=10000)
            
            # 在原始尺度上计算预测值和误差，以确保AIC的可比性
            # 预测流程：输入raw -> 归一化 -> 模型预测norm -> 反归一化 -> 输出raw
            def make_predictor(f, params, ns, ys):
                return lambda x: f(x / ns, *params) * ys

            predictor = make_predictor(func, popt_norm, n_scale, y_scale)
            predict_funcs[name] = predictor
            
            y_pred_raw = predictor(n_raw)
            
            # 计算 RSS (Residual Sum of Squares)
            residuals = y_raw - y_pred_raw
            rss = np.sum(residuals**2)
            
            # 计算 R^2
            ss_tot = np.sum((y_raw - np.mean(y_raw))**2)
            r2 = 1 - (rss / ss_tot) if ss_tot > 0 else 0
            
            # 计算 AIC (带惩罚项)
            aic = calculate_aic(len(n_raw), rss, k)
            
            fit_report[name] = {
                'r2': r2,
                'aic': aic,
                'params_norm': popt_norm.tolist(),
                'rss': rss
            }
            
            if aic < best_aic:
                best_aic = aic
                best_model_name = name
                
        except Exception as e:
            # print(f"拟合 {name} 失败: {e}")
            pass

    # 4. 绘图 (修复坐标轴和曲线)
    plt.figure(figsize=(12, 7))
    
    # 绘制原始数据点
    plt.scatter(n_raw, y_raw, color='black', s=20, alpha=0.6, label='Measured Data', zorder=5)
    
    # 生成平滑的X轴数据用于画线
    x_smooth = np.linspace(min(n_raw), max(n_raw), 500)
    
    # 颜色映射
    colors = plt.cm.tab10(np.linspace(0, 1, len(MODELS)))
    
    # 按AIC排序绘制图例
    sorted_models = sorted(fit_report.items(), key=lambda x: x[1]['aic'])
    
    for idx, (name, metrics) in enumerate(sorted_models):
        if name not in predict_funcs: continue
        
        # 使用闭包predictor直接计算原始尺度的Y
        y_smooth = predict_funcs[name](x_smooth)
        
        # 样式设置
        is_best = (name == best_model_name)
        linewidth = 3 if is_best else 1.5
        alpha = 1.0 if is_best else 0.4
        linestyle = '-' if is_best else '--'
        label = f"{name} (AIC={metrics['aic']:.1f}, R²={metrics['r2']:.4f})"
        
        if is_best:
            label = "★ " + label
            
        plt.plot(x_smooth, y_smooth, label=label, 
                 linewidth=linewidth, alpha=alpha, linestyle=linestyle, zorder=10 if is_best else 1)

    plt.title(f'Time Complexity Analysis: {base_name}\nBest Fit: {best_model_name}', fontsize=14)
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Bytecode Instructions', fontsize=12)
    
    # 格式化Y轴为科学计数法或K/M格式
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
    
    print(f"分析完成。最佳模型: {best_model_name} (AIC={best_aic:.2f})")
    print(f"结果已保存至: {result_dir}")

def main():
    folder_path = config.linear_folder_path
    python_files = sorted([os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.py')])
    
    print(f"找到 {len(python_files)} 个文件。")
    for i, path in enumerate(python_files):
        print(f"\n--- 处理文件 {i+1}/{len(python_files)}: {os.path.basename(path)} ---")
        process_code_file(path, force_reanalyze=True)
        

if __name__ == "__main__":
    main()
    print(f"2当前时间是: {time.strftime('%H:%M:%S')}")
