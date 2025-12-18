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
with open(r'd:\MyResearch\codeComplex\data\onlyCode\python\cubic\python_cubic_0002.py', 'r', encoding='utf-8') as f:
    original_code = f.read()

# 创建测试结果文件
test_results = []
max_n = 100  # 减小n的最大值以避免过长的运行时间
step = 1  # 使用更小的间隔

try:
    # 对于每个n值（从1到100，间隔1）
    for n in range(1, max_n + 1, step):
        m = 1  # 根据代码逻辑，m初始为1即可
        
        # 修改代码中的输入部分
        modified_code = re.sub(r'n, m = map\(int, input\(\).split\(\)\)', 
                             f'n, m = {n}, {m}', 
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
            
        # 每10个点保存一次数据，防止程序中断导致数据丢失
        if n % 10 == 0:
            np.savez(r'd:\MyResearch\codeComplex\test\temp_results.npz', results=test_results)
            
finally:
    # 保存最终结果
    np.savez(r'd:\MyResearch\codeComplex\test\time_results_small.npz', results=test_results)

# 加载结果
loaded_results = np.load(r'd:\MyResearch\codeComplex\test\time_results_small.npz')['results']
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

plt.xlabel('n')
plt.ylabel('Run Time (seconds)')
plt.title('Time Complexity Analysis')
plt.legend()
plt.grid(True)
plt.savefig(r'd:\MyResearch\codeComplex\test\time_complexity_plot.png')
plt.close()

# 绘制所有模型的拟合结果（除了指数模型，因为可能会导致数值溢出）
plt.figure(figsize=(12, 8))
plt.scatter(data['n'], data['time'], label='Actual Data', color='blue', alpha=0.5)

for model_name, result in fit_results.items():
    if model_name != 'Exponential':  # 跳过指数模型以避免数值问题
        plt.plot(plot_n, result['model'](plot_n, *result['popt']), 
                 label=f'{model_name} (R²={result["r_squared"]:.4f})')

plt.xlabel('n')
plt.ylabel('Run Time (seconds)')
plt.title('All Models Comparison')
plt.legend()
plt.grid(True)
plt.savefig(r'd:\MyResearch\codeComplex\test\all_models_comparison.png')
plt.close()

# 生成报告文件
with open(r'd:\MyResearch\codeComplex\test\time_complexity_report.txt', 'w', encoding='utf-8') as f:
    f.write('Time Complexity Analysis Report\n')
    f.write('=' * 50 + '\n')
    f.write(f'Number of data points: {len(data["n"])}\n')
    f.write(f'n range: {min(data["n"])} to {max(data["n"])}\n')
    f.write(f'Step size: {step}\n')
    f.write('\nFit Results:\n')
    f.write('-' * 30 + '\n')
    
    for model_name, result in fit_results.items():
        f.write(f'{model_name}:\n')
        f.write(f'  Parameters: {result["popt"]}\n')
        f.write(f'  R²: {result["r_squared"]:.6f}\n')
        f.write('\n')
    
    f.write('Best Fit Model:\n')
    f.write('-' * 30 + '\n')
    f.write(f'{best_model[0]} with R² = {best_model[1]["r_squared"]:.6f}\n')
    f.write(f'Parameters: {best_model[1]["popt"]}\n')

print('Time complexity analysis completed!')
print(f'Report saved to: d:\\MyResearch\\codeComplex\\test\\time_complexity_report.txt')
print(f'Plots saved to: d:\\MyResearch\\codeComplex\\test\\time_complexity_plot.png')
print(f'                d:\\MyResearch\\codeComplex\\test\\all_models_comparison.png')
