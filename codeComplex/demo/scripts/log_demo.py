import time
import re
import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit, least_squares
import os
import sys
import signal
from openai import OpenAI

# 全局变量用于存储统计信息
global_stats = None

# 信号处理函数，确保在程序被中断时保存统计信息
def signal_handler(signum, frame):
    print(f"\n接收到信号 {signum}，正在保存统计信息...")
    if global_stats is not None:
        save_stats(global_stats)
    print("统计信息已保存，程序退出。")
    sys.exit(0)

# 设置信号处理
# signal.signal(signal.SIGINT, signal_handler)  # 捕获 Ctrl+C

# 保存统计信息的函数
def save_stats(stats_data):
    try:
        stats_dir = '/home/wuyankai/myResearch/codeComplex/demo/filteredData'
        os.makedirs(stats_dir, exist_ok=True)
        stats_file_path = os.path.join(stats_dir, 'linear_demo_stats.json')
        with open(stats_file_path, 'w', encoding='utf-8') as f:
            json.dump(stats_data, f, indent=2, ensure_ascii=False)
        print(f"统计信息已保存到：{stats_file_path}")
    except Exception as e:
        print(f"保存统计信息时发生错误: {e}")

# 导入配置文件
import config

# 定义不同时间复杂度的函数模型
def constant(n, a):
    return a * np.ones_like(n)

def linear(n, a, b):
    return a * n + b

def quadratic(n, a, b, c):
    return a * n**2 + c

def cubic(n, a, b, c, d):
    return a * n**3  + d

def logarithmic(n, a, b):
    return a * np.log(n) + b

def n_log_n(n, a, b):
    return a * n * np.log(n) + b

def exponential(n, a, b):
    return a * np.exp(b * n)

def power(n, a, b):
    return a * n**b

# 处理单个代码文件的函数
def process_code_file(code_path, expected_models):
    """处理单个代码文件，执行完整的时间复杂度分析流程
    
    Args:
        code_path: str, 代码文件路径
        expected_models: list, 预期的复杂度模型列表
    
    Returns:
        bool: 处理是否成功
    """
    if not os.path.exists(code_path):
        print(f"错误：文件 {code_path} 不存在")
        return False
    
    # 读取原始代码
    with open(code_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    print(f"\n1. 读取原始代码：\n{code_path}")
    print(f"代码长度：{len(code)} 字符")
    
    # 提取文件名作为结果目录名
    file_name = os.path.basename(code_path)
    base_name = os.path.splitext(file_name)[0]
    # 使用配置文件中的结果目录
    result_dir = f"{config.linear_results_base_dir}/results_{base_name}"  # 修复目录名拼写错误
    os.makedirs(result_dir, exist_ok=True)
    # 创建测试结果文件
    test_results = []
    # 使用配置文件中的测试参数
    max_n = config.max_n  # 测试规模的最大值
    step = config.step    # 间隔为1
    
    # 检查是否已经有部分结果
    temp_results_path = os.path.join(result_dir, "temp_results.npz")
    if os.path.exists(temp_results_path):
        loaded_data = np.load(temp_results_path)
        test_results = loaded_data['results'].tolist()
        start_n = int(test_results[-1][0]) + step if test_results else 1
        print(f"继续从n={start_n}开始分析")
    else:
        # 使用配置文件中的初始测试规模
        start_n = config.start_n
    
    try:
        # 对于每个测试规模n（从start_n到max_n，间隔step）
        print(f"\n3. 执行时间测试：n = {start_n} 到 {max_n}，步长 {step}")
        for n in range(start_n, max_n + 1, step):
        # for n in [10**3, 10**4, 10**5, 10**6, 10**7, 10**8 ]:
                # 构造完整的测试代码
            test_code = f"""{code}

# 执行测试
main({n})
"""
            
            # 记录开始时间
            start_time = time.perf_counter()
            # print(f"当前测试规模n={n}")
            # print(f"当前测试代码：")
            # print(test_code)
            # 创建一个临时环境并执行代码
            exec_globals = {}
            exec(test_code, exec_globals)
            
            # 记录结束时间
            end_time = time.perf_counter()
            
            # 计算运行时间
            run_time = end_time - start_time
            run_time_ms = run_time * 1000
            
            # 保存结果
            test_results.append((n, run_time_ms))
            # print(f"n={n}, time={run_time_ms:.6f}ms")
            
            # 记录当前分析的数据点数量
            current_datapoints = len(test_results)
            
            # 输出进度（每10个点或最后一个点）
            # 当前已分析 {current_datapoints} 个数据点
            # if n % 10 == 0 or n == max_n:
            #     print(f'Completed n={n}, time={run_time:.6f}s')
            #     print(f'当前已分析 {current_datapoints} 个数据点')
            
            # 每10个点保存一次临时数据，防止程序中断导致数据丢失
            if current_datapoints % 10000 == 0:
                np.savez(temp_results_path, results=test_results)
                # 临时数据已保存到：{temp_results_path}
                # print(f'临时数据已保存到 {temp_results_path}')
                
    except KeyboardInterrupt:
        print("\n分析被用户中断，保存已收集的数据...")
    except Exception as e:
        print(f"\n分析过程中发生错误: {e}")
        import traceback
        traceback.print_exc()
    finally:
        # 保存最终结果
        final_results_path = os.path.join(result_dir, "time_results.npz")
        np.savez(final_results_path, results=test_results)
        print(f'最终数据已保存到 \n{final_results_path}')
    
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
        
        # 创建权重数组，让大N的数据点权重更高
        # 权重与n成正比，可以根据需要调整权重函数
        weights = n_values / n_values.max()  # 归一化到[0,1]范围
        # 或者使用更激进的权重：权重与n的平方成正比
        # weights = (n_values / n_values.max()) ** 2
        # 为权重添加一个小偏移，确保即使n=0也有一定权重
        weights = weights + 0.1
        # 归一化权重，使总和为1
        weights = weights / weights.sum()
        # 将权重转换为sigma参数（curve_fit中sigma是标准差，与权重成反比）
        sigma = 1.0 / weights
        
        # 尝试拟合不同的模型
        models = {
            'Constant': constant,
            'Linear': linear,
            'Quadratic': quadratic,
            'Cubic': cubic,
            'Logarithmic': logarithmic,
            'n_log_n': n_log_n,
            'Exponential': exponential,
            'Power': power
        }
        
        # 保存拟合结果
        fit_results = {}
        
        print("\n4. 开始进行时间复杂度拟合分析...")
        for model_name, model_func in models.items():
            try:
                # 定义残差函数，用于稳健回归
                def residual_func(params, n, y):
                    # 计算残差 = (观测值 - 模型预测值) / 权重
                    # 这样可以保持大N数据点的高权重
                    return (y - model_func(n, *params)) * weights
                
                # 使用稳健回归（least_squares）代替curve_fit
                if model_name == 'Constant':
                    result = least_squares(residual_func, x0=[np.mean(data['time'])], args=(data['n'], data['time']), loss='soft_l1')
                    popt = result.x
                elif model_name == 'Linear':
                    result = least_squares(residual_func, x0=[1e-9, 0], args=(data['n'], data['time']), loss='soft_l1')
                    popt = result.x
                elif model_name == 'Quadratic':
                    # 增大二次项系数a的初始值，减小低阶项系数的初始值
                    result = least_squares(residual_func, x0=[1e-10, 1e-12, 1e-14], args=(data['n'], data['time']), loss='soft_l1')
                    popt = result.x
                elif model_name == 'Cubic':
                    # 增大三次项系数a的初始值，减小低阶项系数的初始值
                    result = least_squares(residual_func, x0=[1e-13, 1e-15, 1e-17, 1e-19], args=(data['n'], data['time']), loss='soft_l1')
                    popt = result.x
                elif model_name == 'Logarithmic':
                    result = least_squares(residual_func, x0=[1e-6, 0], args=(data['n'], data['time']), loss='soft_l1')
                    popt = result.x
                elif model_name == 'n_log_n':
                    result = least_squares(residual_func, x0=[1e-9, 0], args=(data['n'], data['time']), loss='soft_l1')
                    popt = result.x
                elif model_name == 'Exponential':
                    result = least_squares(residual_func, x0=[1e-6, 1e-6], args=(data['n'], data['time']), loss='soft_l1')
                    popt = result.x
                elif model_name == 'Power':
                    result = least_squares(residual_func, x0=[1e-9, 1], args=(data['n'], data['time']), loss='soft_l1')
                    popt = result.x
                
                # 计算R²值
                residuals = data['time'] - model_func(data['n'], *popt)
                ss_res = np.sum(residuals**2)
                ss_tot = np.sum((data['time'] - np.mean(data['time']))**2)
                if ss_tot == 0:  # 处理所有时间相同的情况
                    r_squared = 1.0
                else:
                    r_squared = 1 - (ss_res / ss_tot)
                
                # 计算BIC和AIC
                n_samples = len(data['n'])
                k_params = len(popt)
                
                # BIC (贝叶斯信息准则): BIC = n * ln(SSR/n) + k * ln(n)
                bic = n_samples * np.log(ss_res / n_samples) + k_params * np.log(n_samples)
                
                # AIC (赤池信息准则): AIC = 2k + n * ln(SSR/n)
                aic = 2 * k_params + n_samples * np.log(ss_res / n_samples)
                
                # 保存拟合结果
                fit_results[model_name] = {
                    'params': popt.tolist(),
                    'r_squared': r_squared,
                    'bic': bic,
                    'aic': aic,
                    'success': True
                }
                
                # 注释掉所有模型的详细输出，只保留最佳拟合模型的信息
                # print(f"{model_name}: R² = {r_squared:.6f}, BIC = {bic:.6f}, AIC = {aic:.6f}, 参数 = {popt}")
                
            except Exception as e:
                fit_results[model_name] = {
                    'params': [],
                    'r_squared': 0,
                    'success': False,
                    'error': str(e)
                }
                print(f"{model_name}: 拟合失败 - {e}")
        
        # 找出最佳拟合模型
        # 首先筛选出成功拟合的模型
        successful_models = {name: results for name, results in fit_results.items() if results['success']}
        if successful_models:
            # 使用BIC选择最佳模型（BIC值越小越好）
            best_model = min(successful_models.items(), key=lambda x: x[1]['bic'])
            best_model_name = best_model[0]
            print(f"\n最佳拟合模型: {best_model_name} (基于BIC最小选择)")
            print(f"  BIC值: {best_model[1]['bic']:.6f}")
            print(f"  AIC值: {best_model[1]['aic']:.6f}")
            print(f"  R²值: {best_model[1]['r_squared']:.6f}")
        else:
            best_model_name = None
            print("\n没有成功拟合的模型")
        
        # 保存拟合结果
        fit_results_path = os.path.join(result_dir, "fit_results.json")
        with open(fit_results_path, 'w', encoding='utf-8') as f:
            json.dump(fit_results, f, indent=2, ensure_ascii=False)
        
        # 绘制原始数据和最佳拟合曲线
        plt.figure(figsize=(12, 8))
        plt.scatter(data['n'], data['time'], label='Actual Data', color='blue', alpha=0.5)
        
        # 绘制最佳拟合曲线
        if best_model[0] in ['Logarithmic', 'n_log_n', ]:
            # 对于对数模型，只在n>0时绘制
            plot_n = np.linspace(1, max(data['n']), 1000)
        else:
            plot_n = np.linspace(min(data['n']), max(data['n']), 1000)
        
        plt.plot(plot_n, models[best_model[0]](plot_n, *best_model[1]['params']), 
                 label=f'Best Fit: {best_model[0]}', color='red', linewidth=2)
        
        plt.xlabel('Test Size (n)')
        plt.ylabel('Run Time (seconds)')
        plt.title(f'Time Complexity Analysis - {base_name}')
        plt.legend()
        plt.grid(True)
        plot_path = os.path.join(result_dir, f"time_complexity_plot_{base_name}.png")
        plt.savefig(plot_path)
        plt.close()
        print(f'最佳拟合曲线已保存到 {plot_path}')
        
        # 绘制所有模型的拟合结果（除了指数模型，因为可能会导致数值溢出）
        plt.figure(figsize=(12, 8))
        plt.scatter(data['n'], data['time'], label='Actual Data', color='blue', alpha=0.5)
        
        for model_name, result in fit_results.items():
            if result['success'] and model_name not in ['Exponential', 'Sqrt_Exponential']:  # 跳过指数模型以避免数值问题
                plt.plot(plot_n, models[model_name](plot_n, *result['params']), 
                         label=f'{model_name} (R²={result["r_squared"]:.4f})')
        
        plt.xlabel('Test Size (n)')
        plt.ylabel('Run Time (seconds)')
        plt.title(f'All Models Comparison - {base_name}')
        plt.legend()
        plt.grid(True)
        comparison_path = os.path.join(result_dir, f"all_models_comparison_{base_name}.png")
        plt.savefig(comparison_path)
        plt.close()
        print(f'所有模型对比图已保存到 {comparison_path}')
        
        # 生成报告
        report_path = os.path.join(result_dir, f"time_complexity_report_{base_name}.txt")
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"时间复杂度分析报告\n")
            f.write(f"====================\n\n")
            f.write(f"分析文件: {code_path}\n")
            f.write(f"分析时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"测试参数: n = {start_n} 到 {max_n}, 步长 {step}\n")
            f.write(f"数据点数量: {len(test_results)}\n\n")
            f.write(f"模型拟合结果:\n\n")
            
            # 按R²值排序输出
            sorted_models = sorted(fit_results.items(), key=lambda x: x[1]['r_squared'] if x[1]['success'] else 0, reverse=True)
            for model_name, result in sorted_models:
                if result['success']:
                    f.write(f"{model_name}:\n")
                    f.write(f"  R²值: {result['r_squared']:.6f}\n")
                    f.write(f"  参数: {result['params']}\n")
                else:
                    f.write(f"{model_name}: 拟合失败 - {result['error']}\n")
                f.write("\n")
            
            f.write(f"最佳拟合模型: {best_model[0]} (基于BIC最小选择)\n")
            f.write(f"BIC值: {best_model[1]['bic']:.6f}\n")
            f.write(f"AIC值: {best_model[1]['aic']:.6f}\n")
            f.write(f"R²值: {best_model[1]['r_squared']:.6f}\n")
        
        print(f"\n分析报告已保存到 {report_path}")
        print(f"所有结果已保存到目录 {result_dir}")
        
        # 根据预期模型列表判断处理是否成功
        return best_model_name in expected_models
    else:
        print(f"\n数据点不足 ({len(test_results)} 个)，无法进行拟合分析")
        return False
    

# 主函数：执行完整的时间复杂度分析流程
def main():
    global global_stats
    
    # 选择要处理的文件夹类型：'logn' 或 'cubic'
    folder_type = 'quadratic'  # 可以修改为 'cubic' 或 'quadratic' 来处理不同类型的文件夹
    
    # 根据选择的类型设置文件夹路径
    if folder_type == 'logn':
        folder_path = config.logn_folder_path
        expected_models = ['Logarithmic', 'logn','constant', 'Power','Constant',"n_log_n"]  # logn类型文件的预期模型
    elif folder_type == 'linear':
        folder_path = config.linear_folder_path
        expected_models = ["linear"]  # linear类型文件的预期模型
    elif folder_type == 'cubic':
        folder_path = config.cubic_folder_path
        expected_models = ['Cubic']  # cubic类型文件的预期模型
    elif folder_type == 'quadratic':
        folder_path = config.quadratic_folder_path
        expected_models = ['Quadratic']  # quadratic类型文件的预期模型
    else:
        print(f"不支持的文件夹类型: {folder_type}")
        return
    
    # 获取文件夹中所有的Python文件
    python_files = []
    for file in os.listdir(folder_path):
        if file.endswith('.py'):
            python_files.append(os.path.join(folder_path, file))
    
    # 按文件名排序
    python_files.sort()
    
    print(f"找到 {len(python_files)} 个Python文件，开始处理...")
    
    # 初始化计数器
    total_files = len(python_files)
    success_count = 0
    failed_count = 0
    success_files = []
    failed_files = []
    
    # 创建初始统计数据
    global_stats = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'total_files': total_files,
        'success_count': success_count,
        'failed_cout': failed_count,
        'success_files': success_files,
        'failed_files': failed_files,
        'folder_path': folder_path
    }
    
    # 遍历所有Python文件，逐个处理
    for i, code_path in enumerate(python_files, 1):
        # if(i>=582-3):
        if(i>=0):
            print(f"\n{'='*60}")
            print(f"处理文件 {i}/{len(python_files)}")
            print(f"{'='*60}")
            try:
                success = process_code_file(code_path, expected_models)
                if success:
                    success_count += 1
                    success_files.append(os.path.basename(code_path))
                else:
                    failed_count += 1
                    failed_files.append(os.path.basename(code_path))
            except Exception as e:
                print(f"处理文件 {code_path} 时发生异常: {e}")
                import traceback
                traceback.print_exc()
                failed_count += 1
                failed_files.append(os.path.basename(code_path))
        # 更新全局统计信息
        global_stats['success_count'] = success_count
        global_stats['failed_count'] = failed_count
        global_stats['success_files'] = success_files
        global_stats['failed_files'] = failed_files
        global_stats['timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"\n{'='*60}")
    print("所有文件处理完成！")
    print(f"{'='*60}")
    
    # 生成统计信息
    print(f"\n统计信息：")
    print(f"总文件数：{total_files}")
    print(f"成功处理：{success_count}")
    print(f"处理失败：{failed_count}")
    
    # 保存统计信息
    save_stats(global_stats)

if __name__ == "__main__":
    main()
