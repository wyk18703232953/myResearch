import time
import re
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import os

# 定义不同时间复杂度的函数模型
def constant(n, a):
    return a * np.ones_like(n)

def linear(n, a, b):
    return a * n + b

def quadratic(n, a, b, c):
    return a * n**2 + b * n + c

def cubic(n, a, b, c, d):
    return a * n**3 + b * n**2 + c * n + d

def logarithmic(n, a, b):
    return a * np.log(n) + b

def n_log_n(n, a, b):
    return a * n * np.log(n) + b

def exponential(n, a, b):
    return a * np.exp(b * n)

def sqrt_exponential(n, a, b):
    return a * np.exp(b * n / 2)

def power(n, a, b):
    return a * n**b

# 读取原始代码
with open(r'd:\MyResearch\codeComplex\data\onlyCode\python\cubic\python_cubic_0004.py', 'r', encoding='utf-8') as f:
    original_code = f.read()

# 创建测试结果文件
test_results = []
max_n = 100  # 字符串长度的最大值
step = 1  # 间隔为1

# 检查是否已经有部分结果
temp_results_path = r'D:/MyResearch/codeComplex/demo/onlyCode/python/cubic/results_0004/temp_results.npz'
if os.path.exists(temp_results_path):
    loaded_data = np.load(temp_results_path)
    test_results = loaded_data['results'].tolist()
    start_n = int(test_results[-1][0]) + step if test_results else 1
    print(f"继续从n={start_n}开始分析")
else:
    start_n = 1

try:
    # 对于每个字符串长度n（从start_n到max_n，间隔step）
    for n in range(start_n, max_n + 1, step):
        # 生成测试字符串，使用重复的"a"来确保有大量重复子串
        test_str = "a" * n
        
        # 修改代码中的输入部分
        modified_code = re.sub(r's=input\(\)', 
                             f's="{test_str}"', 
                             original_code)
        
        # 记录开始时间
        start_time = time.time()
        
        # 创建一个临时环境并执行代码
        exec_globals = {}
        exec(modified_code, exec_globals)
        
        # 记录结束时间
        end_time = time.time()
        
        # 计算运行时间
        run_time = end_time - start_time
        
        # 保存结果
        test_results.append((n, run_time))
        
        # 输出进度
        if n % 10 == 0:
            print(f'Completed n={n}, time={run_time:.6f}s')
            print(f'当前已分析 {len(test_results)} 个数据点')
        
        # 每10个点保存一次临时数据，防止程序中断导致数据丢失
        if len(test_results) % 10 == 0:
            np.savez(temp_results_path, results=test_results)
            print(f'临时数据已保存到 {temp_results_path}')
            
except KeyboardInterrupt:
    print("\n分析被用户中断，保存已收集的数据...")
except Exception as e:
    print(f"\n分析过程中发生错误: {e}")
    import traceback
    traceback.print_exc()
finally:
    # 保存最终结果
    final_results_path = r'D:/MyResearch/codeComplex/demo/onlyCode/python/cubic/results_0004/time_results.npz'
    np.savez(final_results_path, results=test_results)
    print(f'最终数据已保存到 {final_results_path}')

# 如果收集到的数据点足够，进行拟合分析
if len(test_results) >= 3:
    # 加载结果
    loaded_results = np.array(test_results)
    n_values = loaded_results[:, 0]
    time_values = loaded_results[:, 1]
    
    # 对不同的时间复杂度模型进行拟合
    data = {
        'n': n_values,
        'time': time_values
    }
    
    # 尝试拟合不同的模型
    models = {
        'Constant': constant,
        'Linear': linear,
        'Quadratic': quadratic,
        'Cubic': cubic,
        'Logarithmic': logarithmic,
        'n_log_n': n_log_n,
        'Exponential': exponential,
        'Sqrt_Exponential': sqrt_exponential,
        'Power': power
    }
    
    # 保存拟合结果
    fit_results = {}
    
    print("\n开始进行时间复杂度拟合分析...")
    for model_name, model_func in models.items():
        try:
            # 尝试拟合
            if model_name == 'Constant':
                popt, pcov = curve_fit(model_func, data['n'], data['time'], p0=[np.mean(data['time'])])
            elif model_name == 'Linear':
                popt, pcov = curve_fit(model_func, data['n'], data['time'], p0=[1e-9, 0])
            elif model_name == 'Quadratic':
                popt, pcov = curve_fit(model_func, data['n'], data['time'], p0=[1e-12, 1e-9, 0])
            elif model_name == 'Cubic':
                popt, pcov = curve_fit(model_func, data['n'], data['time'], p0=[1e-15, 1e-12, 1e-9, 0])
            elif model_name == 'Logarithmic':
                popt, pcov = curve_fit(model_func, data['n'], data['time'], p0=[1e-6, 0])
            elif model_name == 'n_log_n':
                popt, pcov = curve_fit(model_func, data['n'], data['time'], p0=[1e-9, 0])
            elif model_name == 'Exponential':
                popt, pcov = curve_fit(model_func, data['n'], data['time'], p0=[1e-6, 1e-6])
            elif model_name == 'Sqrt_Exponential':
                popt, pcov = curve_fit(model_func, data['n'], data['time'], p0=[1e-6, 1e-6])
            elif model_name == 'Power':
                popt, pcov = curve_fit(model_func, data['n'], data['time'], p0=[1e-6, 1])
            
            # 计算R²值
            residuals = data['time'] - model_func(data['n'], *popt)
            ss_res = np.sum(residuals**2)
            ss_tot = np.sum((data['time'] - np.mean(data['time']))**2)
            if ss_tot == 0:  # 处理所有时间相同的情况
                r_squared = 1.0
            else:
                r_squared = 1 - (ss_res / ss_tot)
            
            fit_results[model_name] = {
                'popt': popt,
                'r_squared': r_squared,
                'model': model_func
            }
            
            print(f'{model_name} fit: R² = {r_squared:.6f}')
            
        except Exception as e:
            print(f'{model_name} fit failed: {e}')
    
    # 找出最佳拟合模型
    if fit_results:
        best_model = max(fit_results.items(), key=lambda x: x[1]['r_squared'])
        print(f'\nBest fit model: {best_model[0]} with R² = {best_model[1]["r_squared"]:.6f}')
        
        # 绘制原始数据和最佳拟合曲线
        plt.figure(figsize=(12, 8))
        plt.scatter(data['n'], data['time'], label='Actual Data', color='blue', alpha=0.5)
        
        # 绘制最佳拟合曲线
        if best_model[0] in ['Logarithmic', 'n_log_n']:
            # 对于对数模型，只在n>0时绘制
            plot_n = np.linspace(1, max(data['n']), 1000)
        else:
            plot_n = np.linspace(min(data['n']), max(data['n']), 1000)
        
        plt.plot(plot_n, best_model[1]['model'](plot_n, *best_model[1]['popt']), 
                 label=f'Best Fit: {best_model[0]}', color='red', linewidth=2)
        
        plt.xlabel('String Length (n)')
        plt.ylabel('Run Time (seconds)')
        plt.title('Time Complexity Analysis - python_cubic_0004.py')
        plt.legend()
        plt.grid(True)
        plot_path = r'D:/MyResearch/codeComplex/demo/onlyCode/python/cubic/results_0004/time_complexity_plot.png'
        plt.savefig(plot_path)
        plt.close()
        print(f'最佳拟合曲线已保存到 {plot_path}')
        
        # 绘制所有模型的拟合结果（除了指数模型，因为可能会导致数值溢出）
        plt.figure(figsize=(12, 8))
        plt.scatter(data['n'], data['time'], label='Actual Data', color='blue', alpha=0.5)
        
        for model_name, result in fit_results.items():
            if model_name not in ['Exponential', 'Sqrt_Exponential']:  # 跳过指数模型以避免数值问题
                plt.plot(plot_n, result['model'](plot_n, *result['popt']), 
                         label=f'{model_name} (R²={result["r_squared"]:.4f})')
        
        plt.xlabel('String Length (n)')
        plt.ylabel('Run Time (seconds)')
        plt.title('All Models Comparison - python_cubic_0004.py')
        plt.legend()
        plt.grid(True)
        comparison_path = r'D:/MyResearch/codeComplex/demo/onlyCode/python/cubic/results_0004/all_models_comparison.png'
        plt.savefig(comparison_path)
        plt.close()
        print(f'所有模型对比图已保存到 {comparison_path}')
        
        # 生成报告文件
        report_path = r'D:/MyResearch/codeComplex/demo/onlyCode/python/cubic/results_0004/time_complexity_report.txt'
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write('Time Complexity Analysis Report\n')
            f.write('=' * 50 + '\n')
            f.write(f'分析的代码文件: python_cubic_0004.py\n')
            f.write(f'Number of data points: {len(data["n"])}\n')
            f.write(f'String length range: {min(data["n"])} to {max(data["n"])}\n')
            f.write(f'Step size: {step}\n')
            f.write('\nFit Results:\n')
            f.write('-' * 30 + '\n')
            
            for model_name, result in sorted(fit_results.items(), key=lambda x: x[1]['r_squared'], reverse=True):
                f.write(f'{model_name}:\n')
                f.write(f'  Parameters: {["{:.6e}".format(p) for p in result["popt"]]}\n')
                f.write(f'  R²: {result["r_squared"]:.6f}\n')
                f.write('\n')
            
            f.write('Best Fit Model:\n')
            f.write('-' * 30 + '\n')
            f.write(f'{best_model[0]} with R² = {best_model[1]["r_squared"]:.6f}\n')
            f.write(f'Parameters: {["{:.6e}".format(p) for p in best_model[1]["popt"]]}\n')
        
        print(f'分析报告已保存到 {report_path}')
else:
    print("\n收集的数据点不足（至少需要3个），无法进行拟合分析")
    print(f"当前仅收集到 {len(test_results)} 个数据点")

print('\n时间复杂度分析脚本执行完成！')
