import time
import re
import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import os
import sys
import dis
from openai import OpenAI

# 尝试导入你的配置文件，如果不存在则使用默认配置
try:
    import config
except ImportError:
    class MockConfig:
        nlogn_results_base_dir = "results"
        max_n = 500
        step = 10
        start_n = 10
        nlogn_folder_path = "./codes"
    config = MockConfig()

# ==========================================
# 1. 复杂度模型库
# ==========================================
def constant(n, a):
    return a * np.ones_like(n)

def logarithmic(n, a, b):
    return a * np.log2(np.maximum(n, 1.1)) + b

def linear(n, a, b):
    return a * n + b

def n_log_n(n, a, b):
    return a * n * np.log2(np.maximum(n, 1.1)) + b

def quadratic(n, a, b, c):
    return a * n**2 + b * n + c

def cubic(n, a, b, c, d):
    return a * n**3 + b * n**2 + c * n + d

def power(n, a, b):
    return a * n**b

def exponential(n, a, b):
    return a * np.exp(np.clip(b * n, -700, 700))

# ==========================================
# 2. 统计学判定工具
# ==========================================
def calculate_aic(n_samples, rss, n_params):
    """计算赤池信息准则 (AIC)，值越小模型越好"""
    if n_samples <= n_params + 1:
        return float('inf')
    return n_samples * np.log(rss / n_samples) + 2 * n_params

def is_coefficient_significant(params, model_name, data_scale):
    """检查最高次项系数是否显著，防止将微小噪声拟合为高阶复杂度"""
    if len(params) == 0: return False
    leading_coeff = abs(params[0])
    
    # 如果高阶项在最大规模下的贡献不足 5%，则视为不显著
    if model_name == 'Quadratic':
        return (leading_coeff * (data_scale['max_n']**2)) > (data_scale['max_val'] * 0.05)
    if model_name == 'Cubic':
        return (leading_coeff * (data_scale['max_n']**3)) > (data_scale['max_val'] * 0.05)
    if model_name == 'Power':
        exponent = params[1]
        return 0.5 < exponent < 5.0 # 限制合理的幂次范围
    return True

# ==========================================
# 3. 核心分析逻辑（替代原有的拟合循环）
# ==========================================
def perform_robust_analysis(n_values, time_values):
    n = np.array(n_values, dtype=float)
    t = np.array(time_values, dtype=float)
    num_samples = len(n)
    max_n, max_val = np.max(n), np.max(t)
    data_scale = {'max_n': max_n, 'max_val': max_val}

    models_config = {
        'Constant': (constant, 1),
        'Logarithmic': (logarithmic, 2),
        'Linear': (linear, 2),
        'n_log_n': (n_log_n, 2),
        'Quadratic': (quadratic, 3),
        'Cubic': (cubic, 4),
        'Power': (power, 2),
        'Exponential': (exponential, 2)
    }

    fit_results = {}
    for name, (func, n_params) in models_config.items():
        try:
            # 智能设置初始参数 p0 提高拟合成功率
            p0 = None
            if name == 'Linear': p0 = [max_val/max_n, 0]
            elif name == 'n_log_n': p0 = [max_val/(max_n * np.log2(max_n)), 0]
            elif name == 'Power': p0 = [max_val/(max_n**1.5), 1.5]
            
            popt, _ = curve_fit(func, n, t, p0=p0, maxfev=10000)
            residuals = t - func(n, *popt)
            rss = np.sum(residuals**2) or 1e-20
            
            aic = calculate_aic(num_samples, rss, n_params)
            ss_tot = np.sum((t - np.mean(t))**2)
            r2 = 1 - (rss / ss_tot) if ss_tot != 0 else 1.0

            # 显著性检查
            if not is_coefficient_significant(popt, name, data_scale):
                aic = float('inf')

            fit_results[name] = {'params': popt.tolist(), 'aic': aic, 'r_squared': r2, 'success': True}
        except:
            fit_results[name] = {'success': False, 'aic': float('inf'), 'r_squared': 0}

    # 决策逻辑：奥卡姆剃刀原则
    valid_models = {k: v for k, v in fit_results.items() if v['success'] and v['aic'] != float('inf')}
    if not valid_models: return "Unknown", fit_results

    # 按 AIC 排序
    sorted_by_aic = sorted(valid_models.items(), key=lambda x: x[1]['aic'])
    best_name, best_info = sorted_by_aic[0]
    
    # 复杂度排序 (越简单越优先)
    rank = {'Constant': 0, 'Logarithmic': 1, 'Linear': 2, 'n_log_n': 3, 'Power': 4, 'Quadratic': 5, 'Cubic': 6, 'Exponential': 7}
    final_best = best_name
    
    # 如果两个模型 AIC 差距小于 10，选择更简单的那个
    for name, info in sorted_by_aic[1:3]:
        if (info['aic'] - best_info['aic'] < 10) and (rank[name] < rank[final_best]):
            final_best = name
            
    # 特殊逻辑：修正 nlogn 和 Power 的模糊区
    if final_best == 'Power':
        exponent = fit_results['Power']['params'][1]
        if 0.9 <= exponent <= 1.1: 
            final_best = 'Linear'
        elif 1.1 < exponent <= 1.4 and fit_results['n_log_n']['success']: 
            final_best = 'n_log_n'

    return final_best, fit_results

# ==========================================
# 4. 指令统计与文件处理
# ==========================================
def count_bytecode_instructions(test_code, n):
    try:
        instruction_count = 0
        def trace_func(frame, event, arg):
            nonlocal instruction_count
            if event == 'line':
                code_obj = frame.f_code
                offset = frame.f_lasti
                while offset < len(code_obj.co_code):
                    instruction_count += 1
                    op = code_obj.co_code[offset]
                    offset += 2 if op >= dis.HAVE_ARGUMENT else 1
            return trace_func
        
        old_trace = sys.gettrace()
        sys.settrace(trace_func)
        try:
            exec(test_code, {})
        finally:
            sys.settrace(old_trace)
        return instruction_count
    except Exception as e:
        print(f"字节码统计出错: {e}")
        raise

def process_code_file(code_path):
    if not os.path.exists(code_path): return
    with open(code_path, 'r', encoding='utf-8') as f:
        original_code = f.read()
    
    base_name = os.path.splitext(os.path.basename(code_path))[0]
    result_dir = f"{config.nlogn_results_base_dir}/results_{base_name}"
    os.makedirs(result_dir, exist_ok=True)
    
    print(f"\n>>> 正在处理: {base_name}")
    
    # (此处省略大模型调用部分，保留你原有的生成的代码逻辑)
    generated_code_path = os.path.join(result_dir, f"generated_{base_name}.py")
    if os.path.exists(generated_code_path):
        with open(generated_code_path, 'r', encoding='utf-8') as f:
            generated_code = f.read()
    else:
        # 假设 call_large_model 函数已定义
        print("调用模型生成代码...")
        # generated_code = call_large_model(original_code) 
        # with open(generated_code_path, 'w') as f: f.write(generated_code)
        return # 如果没有模型 key 暂时跳过

    # 执行测试
    test_results = []
    for n in range(config.start_n, config.max_n + 1, config.step):
        test_code = f"{generated_code}\nmain({n})"
        count = count_bytecode_instructions(test_code, n)
        test_results.append((n, count))
        if n % 100 == 0: print(f"进度: n={n}")

    # 稳健性分析
    n_vals, t_vals = zip(*test_results)
    best_model, all_fits = perform_robust_analysis(n_vals, t_vals)
    
    print(f"分析完成！判定复杂度为: {best_model}")

    # 绘图保存
    plt.figure(figsize=(10, 6))
    plt.scatter(n_vals, t_vals, label='Actual Data', alpha=0.5)
    
    # 准备绘图函数映射
    models_map = {'Constant': constant, 'Logarithmic': logarithmic, 'Linear': linear, 
                  'n_log_n': n_log_n, 'Quadratic': quadratic, 'Cubic': cubic, 
                  'Power': power, 'Exponential': exponential}
    
    plot_n = np.linspace(min(n_vals), max(n_vals), 200)
    plt.plot(plot_n, models_map[best_model](plot_n, *all_fits[best_model]['params']), 
             'r-', label=f'Best Fit: {best_model} (AIC minimal)')
    
    plt.xlabel('Size (n)')
    plt.ylabel('Bytecode Instructions')
    plt.title(f"Complexity Analysis for {base_name}\nDetected: {best_model}")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(result_dir, f"final_plot_{base_name}.png"))
    plt.close()

def main():
    # 逻辑同你的原程序
    pass

if __name__ == "__main__":
    # 示例运行
    # process_code_file("your_script.py")
    pass