#!/usr/bin/env python3
"""
时间复杂度分析程序
读取filteredData/python文件夹下的所有代码，使用time.perf_counter()测量执行时间，
根据BIC拟合时间复杂度函数，并保存结果。
"""

import time
import re
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from scipy.optimize import curve_fit
import os
import sys
import signal
import config

# ==========================================
# 超时处理相关函数
# ==========================================

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("执行超时")

def execute_with_timeout(code_str, globals_dict, locals_dict, timeout=120):
    """
    带超时的代码执行函数
    """
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)
    
    try:
        exec(code_str, globals_dict, locals_dict)
        return True, None
    except TimeoutError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)
    finally:
        signal.alarm(0)  # 取消闹钟

# ==========================================
# 核心工具函数
# ==========================================

def format_time(value):
    """格式化时间显示"""
    if value >= 1:
        return f"{value:.3f}s"
    elif value >= 1e-3:
        return f"{value*1e3:.2f}ms"
    elif value >= 1e-6:
        return f"{value*1e6:.2f}μs"
    else:
        return f"{value*1e9:.2f}ns"

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
# 模型选择指标
# ==========================================

def calculate_aic(n_samples, rss, num_params):
    """
    计算 AIC (Akaike Information Criterion)
    AIC = n * ln(RSS/n) + 2k
    """
    if n_samples <= num_params + 1 or rss <= 0:
        return float('inf')
    
    return n_samples * np.log(rss / n_samples) + 2 * num_params

def calculate_bic(n_samples, rss, num_params):
    """
    计算 BIC (Bayesian Information Criterion)
    BIC = n * ln(RSS/n) + k * ln(n)
    使用BIC作为惩罚项，更倾向于简单模型
    """
    if n_samples <= num_params + 1 or rss <= 0:
        return float('inf')
    
    return n_samples * np.log(rss / n_samples) + num_params * np.log(n_samples)

# ==========================================
# 核心分析逻辑
# ==========================================

def process_code_file(code_path, folder_type, force_reanalyze=False):
    """
    处理单个代码文件，执行时间复杂度分析
    
    Args:
        code_path: 代码文件路径
        folder_type: 文件夹类型（如linear, cubic等）
        force_reanalyze: 是否强制重新分析
    """
    if not os.path.exists(code_path):
        print(f"错误：文件 {code_path} 不存在")
        return
    
    file_name = os.path.basename(code_path)
    base_name = os.path.splitext(file_name)[0]
    
    # 获取结果存储目录
    results_dir = getattr(config, f"{folder_type}_results_base_dir", "/tmp/results")
    result_dir = f"{results_dir}/results_{base_name}"
    os.makedirs(result_dir, exist_ok=True)
    
    # 1. 读取代码
    with open(code_path, 'r', encoding='utf-8') as f:
        original_code = f.read()
    
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
                # 构建测试代码
                test_code = f"""{original_code}

# 执行测试
main({n})
"""
                
                # 记录开始时间
                start_time = time.perf_counter()
                
                # 执行代码（带超时保护） - 使用同一个命名空间，确保函数定义和调用在同一个上下文中
                exec_namespace = {'__builtins__': __builtins__}
                success, error_msg = execute_with_timeout(test_code, exec_namespace, exec_namespace, timeout=20)
                
                # 记录结束时间
                end_time = time.perf_counter()
                execution_time = end_time - start_time
                
                if not success:
                    print(f"  代码执行失败或超时: {error_msg}")
                    raise Exception(f"代码执行失败: {error_msg}")
                
                test_results.append([n, execution_time])
                
                if len(test_results) % 5 == 0:
                    print(f"  n={n}, 时间={format_time(execution_time)}")
                    with open(temp_results_path, 'w', encoding='utf-8') as f:
                        json.dump(test_results, f)
        except Exception as e:
            print(f"执行出错: {e}")
        finally:
            with open(temp_results_path, 'w', encoding='utf-8') as f:
                json.dump(test_results, f)
    
    # 3. 拟合与分析
    if len(test_results) < 5:
        print(f"数据点不足，跳过拟合：{base_name}")
        return
    
    data = np.array(test_results)
    n_raw = data[:, 0]
    y_raw = data[:, 1]  # 执行时间，秒
    
    # 归一化因子
    n_scale = np.max(n_raw)
    y_scale = np.max(y_raw)
    
    n_norm = n_raw / n_scale
    y_norm = y_raw / y_scale
    
    best_bic = float('inf')
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
            p0 = [1.0] * k 
            if name == 'O(n^2)':
                p0 = [1.0, 1.0, 0.0]
            elif name == 'O(log n)':
                p0 = [0.5, 0.0]
            elif name == 'O(n^3)':
                p0 = [1.0, 1.0, 1.0, 0.0]

            popt_norm, pcov_norm = curve_fit(func, n_norm, y_norm, p0=p0, maxfev=10000)
            
            # 创建预测函数（处理归一化和反归一化）
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
            
            # 计算 AIC 和 BIC
            aic = calculate_aic(len(n_raw), rss, k)
            bic = calculate_bic(len(n_raw), rss, k)
            
            fit_report[name] = {
                'r2': r2,
                'aic': aic,
                'bic': bic,
                'params_norm': popt_norm.tolist(),
                'rss': rss
            }
            
            if bic < best_bic:
                best_bic = bic
                best_model_name = name
                
        except Exception as e:
            # print(f"拟合 {name} 失败: {e}")
            continue
    
    # 4. 绘图
    plt.figure(figsize=(12, 7))
    
    # 绘制原始数据点
    plt.scatter(n_raw, y_raw, color='black', s=20, alpha=0.6, label='Measured Data', zorder=5)
    
    # 生成平滑的X轴数据用于画线
    x_smooth = np.linspace(min(n_raw), max(n_raw), 500)
    
    # 颜色映射
    colors = plt.cm.tab10(np.linspace(0, 1, len(MODELS)))
    
    # 按BIC排序绘制图例
    sorted_models = sorted(fit_report.items(), key=lambda x: x[1]['bic'])
    
    for idx, (name, metrics) in enumerate(sorted_models):
        if name not in predict_funcs:
            continue
        
        # 使用闭包predictor直接计算原始尺度的Y
        y_smooth = predict_funcs[name](x_smooth)
        
        # 样式设置
        is_best = (name == best_model_name)
        linewidth = 3 if is_best else 1.5
        alpha = 1.0 if is_best else 0.4
        linestyle = '-' if is_best else '--'
        label = f"{name} (BIC={metrics['bic']:.1f}, R²={metrics['r2']:.4f})"
        
        if is_best:
            label = "★ " + label
            
        plt.plot(x_smooth, y_smooth, label=label, 
                 linewidth=linewidth, alpha=alpha, linestyle=linestyle, zorder=10 if is_best else 1)

    plt.title(f'Time Complexity Analysis: {base_name}\nBest Fit: {best_model_name}', fontsize=14)
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    
    # 格式化Y轴
    ax = plt.gca()
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format_time(x)))
    
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.legend()
    
    plot_path = os.path.join(result_dir, f"complexity_plot_{base_name}.png")
    plt.savefig(plot_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    # 5. 保存报告
    report_path = os.path.join(result_dir, "report.json")
    with open(report_path, 'w') as f:
        json.dump({
            'best_model': best_model_name,
            'best_bic': best_bic,
            'details': fit_report,
            'raw_data': test_results
        }, f, indent=2)
    
    print(f"分析完成。最佳模型: {best_model_name} (BIC={best_bic:.2f})")
    print(f"结果已保存至: {result_dir}")

# ==========================================
# 批量处理函数
# ==========================================

def process_folder(folder_path, folder_type, force_reanalyze=False):
    """
    批量处理指定目录下的所有Python文件
    
    Args:
        folder_path: Python文件目录路径
        folder_type: 文件夹类型（如linear, cubic等）
        force_reanalyze: 是否强制重新分析
    """
    if not os.path.exists(folder_path):
        print(f"错误：目录 {folder_path} 不存在")
        return
    
    python_files = sorted([os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.py')])
    
    print(f"\n--- 开始处理文件夹 {folder_type} ---\n")
    print(f"找到 {len(python_files)} 个Python文件")
    
    # 记录超时文件
    timeout_files = []
    
    for i, file_path in enumerate(python_files, 1):
        print(f"\n处理文件 {i}/{len(python_files)}: {os.path.basename(file_path)}")
        try:
            process_code_file(file_path, folder_type, force_reanalyze)
        except (TimeoutError, Exception) as e:
            error_msg = str(e)
            if "超时" in error_msg:
                print(f"  ⚠️  文件执行超时: {error_msg}")
                timeout_files.append({
                    'file_path': file_path,
                    'file_name': os.path.basename(file_path),
                    'error_type': 'timeout',
                    'error_message': error_msg,
                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
                })
            else:
                print(f"  ❌ 文件处理失败: {error_msg}")
                timeout_files.append({
                    'file_path': file_path,
                    'file_name': os.path.basename(file_path),
                    'error_type': 'error',
                    'error_message': error_msg,
                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
                })
            continue
    
    # 保存超时文件列表
    if timeout_files:
        # 创建结果目录下的timeout文件夹
        timeout_dir = os.path.join(os.path.dirname(folder_path), "timeout_records")
        os.makedirs(timeout_dir, exist_ok=True)
        
        # 保存超时文件记录
        timeout_file_path = os.path.join(timeout_dir, f"{folder_type}_timeout_files.json")
        with open(timeout_file_path, 'w', encoding='utf-8') as f:
            json.dump(timeout_files, f, indent=2, ensure_ascii=False)
        
        print(f"\n📋 {folder_type} 文件夹处理完成!")
        print(f"  总文件数: {len(python_files)}")
        print(f"  成功处理: {len(python_files) - len(timeout_files)}")
        print(f"  超时/失败文件: {len(timeout_files)}")
        print(f"  超时记录已保存到: {timeout_file_path}")
        
        # 打印超时文件列表
        if timeout_files:
            print(f"\n⚠️  超时/失败文件列表:")
            for file_info in timeout_files:
                print(f"    - {file_info['file_name']} ({file_info['error_type']})")
    else:
        print(f"\n✅ {folder_type} 文件夹处理完成! 所有 {len(python_files)} 个文件都成功处理。")

# ==========================================
# 主函数
# ==========================================

def main():
    """主函数，处理所有配置的文件夹"""
    print("时间复杂度分析程序启动...")
    print(f"当前时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 获取所有文件夹配置
    folder_types = getattr(config, 'all_folders', ['linear', 'cubic', 'quadratic', 'logn', 'nlogn', 'constant', 'np', 'jsonl'])
    
    for folder_type in folder_types:
        # 获取文件夹路径
        folder_path = getattr(config, f"{folder_type}_folder_path", None)
        if folder_path and os.path.exists(folder_path):
            process_folder(folder_path, folder_type, force_reanalyze=True)
        else:
            print(f"警告：文件夹路径配置不存在或目录不存在，跳过 {folder_type}")
    
    print(f"\n所有分析完成！当前时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
