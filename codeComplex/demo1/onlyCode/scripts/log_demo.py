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

# 时间单位转换函数
def format_time(time_in_seconds):
    """根据时间大小选择合适的时间单位并格式化
    
    Args:
        time_in_seconds: float, 时间（秒）
        
    Returns:
        tuple: (格式化的时间字符串, 时间单位, 转换后的时间值)
    """
    if time_in_seconds < 1e-9:
        return f"{time_in_seconds * 1e12:.3f}", "ps", time_in_seconds * 1e12
    elif time_in_seconds < 1e-6:
        return f"{time_in_seconds * 1e9:.3f}", "ns", time_in_seconds * 1e9
    elif time_in_seconds < 1e-3:
        return f"{time_in_seconds * 1e6:.3f}", "μs", time_in_seconds * 1e6
    elif time_in_seconds < 1:
        return f"{time_in_seconds * 1e3:.3f}", "ms", time_in_seconds * 1e3
    else:
        return f"{time_in_seconds:.6f}", "s", time_in_seconds

# 动态字节码计数函数
def count_dynamic_bytecode(code_str, globals_dict, locals_dict):
    """执行代码并统计动态字节码指令数
    
    Args:
        code_str: str, 要执行的代码字符串
        globals_dict: dict, 全局命名空间
        locals_dict: dict, 局部命名空间
        
    Returns:
        int: 动态执行的字节码指令总数
    """
    # 编译代码
    compiled_code = compile(code_str, '<string>', 'exec')
    
    # 指令计数
    instruction_count = 0
    
    # 创建从(代码对象, 行号)到该行指令数的映射
    line_instruction_counts = {}
    
    # 统计每行指令数的函数
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
        
        # 存储到全局映射中
        for line, count in line_counts.items():
            line_instruction_counts[(code_obj, line)] = count
    
    # 递归处理所有代码对象
    def process_code_objects(code_obj):
        # 统计该代码对象每行的指令数
        count_instructions_per_line(code_obj)
        
        # 处理嵌套的代码对象（函数内部的函数）
        for const in code_obj.co_consts:
            if hasattr(const, 'co_code'):
                process_code_objects(const)
    
    # 从主代码对象开始处理
    process_code_objects(compiled_code)
    
    # 跟踪函数 - 统计每次行执行时的指令数
    def trace_function(frame, event, arg):
        nonlocal instruction_count
        
        if event == 'line':
            # 获取当前代码对象和行号
            code_obj = frame.f_code
            line_num = frame.f_lineno
            
            # 查找该代码对象和行号的指令数并累加
            if (code_obj, line_num) in line_instruction_counts:
                instruction_count += line_instruction_counts[(code_obj, line_num)]
        
        return trace_function
    
    try:
        # 设置跟踪函数
        original_trace = sys.gettrace()
        sys.settrace(trace_function)
        
        # 执行代码 - 使用相同的字典作为全局和局部命名空间以支持递归
        exec(compiled_code, globals_dict, globals_dict)
        
        # 恢复原始跟踪函数
        sys.settrace(original_trace)
        
        return instruction_count
    except Exception as e:
        # 恢复原始跟踪函数
        sys.settrace(original_trace)
        print(f"动态跟踪计数错误: {e}")
        
        # 使用备用方法：执行并统计所有指令
        instruction_count = 0
        
        # 执行代码
        exec(compiled_code, globals_dict, globals_dict)
        
        # 统计所有静态指令
        def count_all_instructions(code_obj):
            nonlocal instruction_count
            for inst in dis.get_instructions(code_obj):
                instruction_count += 1
            # 递归处理嵌套的代码对象
            for const in code_obj.co_consts:
                if hasattr(const, 'co_code'):
                    count_all_instructions(const)
        
        count_all_instructions(compiled_code)
        
        return instruction_count

# 定义不同时间复杂度的函数模型
# 导入配置文件
import config

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

# 大模型调用函数，基于OpenAI API
def call_large_model(original_code, api_key=None, base_url=None):
    """调用大模型生成可执行程序
    
    Args:
        original_code: str, 原始代码
        api_key (str, optional): OpenAI API密钥，如果不提供则使用默认密钥
        base_url (str, optional): API基础URL，如果不提供则使用默认URL
        
    Returns:
        str: 生成的无input()、可参数化规模n的Python程序
    """
    # 设置默认API参数
    if api_key is None:
        api_key = "sk-3sNQAO5ydpVp29WWoCqvM7Ajqzd1I5WKOpe29cpoT3DoMrZe"
    if base_url is None:
        base_url = "https://yunwu.ai/v1"
    
    # 创建OpenAI客户端
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    # 设计强约束提示词
    system_prompt = """你是一位算法专家，精通Python编程和时间复杂度分析。
    你的任务是将给定的Python程序转换为一个无input()、可参数化规模n的Python程序。
    """
    
    user_prompt = f"""请你将以下Python程序转换为一个无input()、可参数化规模n的Python程序。
    
    要求：
    1. 移除所有input()或等价的输入读取语句
    2. 添加一个函数main(n)，将程序逻辑封装在其中，n为测试规模参数
    3. 确保程序可以直接执行，无需任何外部输入
    4. 生成的程序应保留原始算法的时间复杂度特性
    5. 对于需要数据的地方，根据n生成合适的测试数据
    6. 只输出生成的Python代码，不要输出任何解释性文字
    7. 确保代码语法正确，可直接运行
    8. 不要包含任何额外的注释或说明
    
    示例输入：
    s = input()
    print(s.count('a'))
    
    示例输出：
    def main(n):
        s = 'a' * n
        return s.count('a')
    
    原始Python程序：
    ```python
    {original_code}
    ```
    """
    
    try:
        # 调用大模型API
        response = client.chat.completions.create(
            model="gpt-5.1",
            temperature=0.0,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            stream=False
        )
        
        # 提取模型原始回复
        model_raw_output = response.choices[0].message.content.strip()
        
        # 清理输出，确保只返回Python代码
        # 移除可能的代码块标记
        if model_raw_output.startswith('```python'):
            model_raw_output = model_raw_output[10:]
        if model_raw_output.endswith('```'):
            model_raw_output = model_raw_output[:-3]
        
        return model_raw_output.strip()
        
    except Exception as e:
        error_msg = str(e)
        print(f"调用大模型时出错: {error_msg}")
        # 直接抛出异常，让用户后期查看具体错误信息
        raise Exception(f"调用大模型失败: {error_msg}") from e

# 处理单个代码文件的函数
def process_code_file(code_path, force_reanalyze=False):
    """处理单个代码文件，执行完整的时间复杂度分析流程
    
    Args:
        code_path: str, 代码文件路径
    """
    if not os.path.exists(code_path):
        print(f"错误：文件 {code_path} 不存在")
        return
    
    # 读取原始代码
    with open(code_path, 'r', encoding='utf-8') as f:
        original_code = f.read()
    
    print(f"\n1. 读取原始代码：{code_path}")
    print(f"代码长度：{len(original_code)} 字符")
    
    # 提取文件名作为结果目录名
    file_name = os.path.basename(code_path)
    base_name = os.path.splitext(file_name)[0]
    # 使用配置文件中的结果目录
    result_dir = f"{config.logn_results_base_dir}/results_{base_name}"  # 修复目录名拼写错误
    os.makedirs(result_dir, exist_ok=True)
    
    # 构建生成程序的文件路径
    generated_code_path = os.path.join(result_dir, f"generated_{base_name}.py")
    
    # 检查是否已经存在生成的程序文件
    if os.path.exists(generated_code_path):
        print(f"\n2. 检测到已存在生成的程序，直接读取：{generated_code_path}")
        with open(generated_code_path, 'r', encoding='utf-8') as f:
            generated_code = f.read()
        print(f"读取到的程序：")
        print(generated_code)
    else:
        # 调用大模型生成可执行程序
        print("\n2. 调用大模型生成可执行程序...")
        generated_code = call_large_model(original_code)
        print(f"生成的程序：")
        print(generated_code)
        
        # 保存生成的程序
        with open(generated_code_path, 'w', encoding='utf-8') as f:
            f.write(generated_code)
        print(f"生成的程序已保存到：{generated_code_path}")
    
    # 创建测试结果文件
    test_results = []
    # 使用配置文件中的测试参数
    max_n = config.max_n  # 测试规模的最大值
    step = config.step    # 间隔为1
    
    # 检查是否已经有部分结果
    temp_results_path = os.path.join(result_dir, "temp_results.npz")
    time_results_path = os.path.join(result_dir, "time_results.npz")
    
    # 如果设置了强制重新分析，删除之前的结果文件
    if force_reanalyze:
        if os.path.exists(temp_results_path):
            os.remove(temp_results_path)
            print(f"已删除临时结果文件: {temp_results_path}")
        if os.path.exists(time_results_path):
            os.remove(time_results_path)
            print(f"已删除最终结果文件: {time_results_path}")
        start_n = config.start_n
    elif os.path.exists(temp_results_path):
        loaded_data = np.load(temp_results_path)
        test_results = loaded_data['results'].tolist()
        start_n = int(test_results[-1][0]) + step if test_results else 1
        print(f"继续从n={start_n}开始分析")
    else:
        # 使用配置文件中的初始测试规模
        start_n = config.start_n
    
    try:
        # 对于每个测试规模n（从start_n到max_n，间隔step）
        print(f"\n3. 执行字节码计数测试：n = {start_n} 到 {max_n}，步长 {step}")
        total_n = len(range(start_n, max_n + 1, step))
        for idx, n in enumerate(range(start_n, max_n + 1, step), 1):
            # 构造完整的测试代码
            test_code = f"""{generated_code}

# 执行测试
main({n})
"""
            
            # 使用动态字节码计数代替时间计数
            exec_globals = {}
            bytecode_count = count_dynamic_bytecode(test_code, exec_globals, exec_globals)
            
            # 保存结果（字节码指令数）
            test_results.append((n, bytecode_count))
            
            # 记录当前分析的数据点数量
            current_datapoints = len(test_results)
            
            # 输出进度
            progress = (idx / total_n) * 100
            print(f'Progress: {progress:.1f}% | n={n} | Bytecode Instructions={bytecode_count}')
            
            # 每10个点保存一次临时数据，防止程序中断导致数据丢失
            if current_datapoints % 10 == 0:
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
        final_results_path = os.path.join(result_dir, "time_results.npz")
        np.savez(final_results_path, results=test_results)
        print(f'最终数据已保存到 {final_results_path}')
    
    # 如果收集到的数据点足够，进行拟合分析
    if len(test_results) >= 3:
        # 加载结果
        loaded_results = np.array(test_results)
        n_values = loaded_results[:, 0]
        count_values = loaded_results[:, 1]
        
        # 准备基础数据
        data = {
            'n': n_values,
            'count': count_values,  # 使用原始字节码计数进行拟合
        }
        
        # 对n和time都进行缩放，使它们都处于合适的数量级（1到1000之间）
        # 避免数值问题，提高拟合稳定性和参数可读性
        
        # 缩放n：使其范围为[1, 1000]
        n_max = np.max(data['n'])
        n_min = np.min(data['n'])
        n_range = n_max - n_min
        if n_range == 0:  # 处理所有n相同的情况
            n_scale = 1.0
            scaled_n = data['n'].copy()
        else:
            n_scale = 999.0 / n_range  # 缩放因子，将n_range缩放到999
            scaled_n = (data['n'] - n_min) * n_scale + 1.0  # 缩放后范围为[1, 1000]
        
        # 缩放count：使其范围为[1, 1000]
        c_max = np.max(data['count'])
        c_min = np.min(data['count'])
        c_range = c_max - c_min
        if c_range == 0:  # 处理所有计数相同的情况
            c_scale = 1.0
            scaled_c = data['count'].copy()
        else:
            c_scale = 999.0 / c_range  # 缩放因子，将count_range缩放到999
            scaled_c = (data['count'] - c_min) * c_scale + 1.0  # 缩放后范围为[1, 1000]
        
        # 添加缩放后的数据和缩放因子到data字典
        data.update({
            'scaled_n': scaled_n,
            'scaled_c': scaled_c,
            'n_scale': n_scale,
            'n_min': n_min,
            'c_scale': c_scale,
            'c_min': c_min
        })
        
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
        
        print("\n4. 开始进行时间复杂度拟合分析...")
        for model_name, model_func in models.items():
            try:
                # 使用缩放后的数据进行拟合，提高数值稳定性
                n_data = data['scaled_n']
                c_data = data['scaled_c']  # 使用缩放后的字节码计数数据
                
                # 根据模型类型设置更合理的初始参数（基于实际数据范围）
                mean_count = np.mean(c_data)
                
                if model_name == 'Constant':
                    popt_scaled, pcov = curve_fit(model_func, n_data, c_data, p0=[mean_count])
                elif model_name == 'Linear':
                    # 线性模型初始参数：斜率约为0.1，截距约为均值
                    popt_scaled, pcov = curve_fit(model_func, n_data, c_data, p0=[0.1, mean_count])
                elif model_name == 'Quadratic':
                    popt_scaled, pcov = curve_fit(model_func, n_data, c_data, p0=[0.01, 0.1, mean_count])
                elif model_name == 'Cubic':
                    popt_scaled, pcov = curve_fit(model_func, n_data, c_data, p0=[0.001, 0.01, 0.1, mean_count])
                elif model_name == 'Logarithmic':
                    # 对数模型使用原始数据直接拟合，避免转换问题
                    try:
                        popt_original, pcov = curve_fit(model_func, data['n'], data['count'], 
                                                      p0=[mean_count, mean_count])
                        popt_scaled = popt_original
                    except Exception:
                        popt_scaled, pcov = curve_fit(model_func, n_data, c_data, p0=[1.0, mean_count])
                elif model_name == 'n_log_n':
                    # n_log_n模型使用原始数据直接拟合，避免转换问题
                    try:
                        popt_original, pcov = curve_fit(model_func, data['n'], data['count'], 
                                                      p0=[0.1, mean_count])
                        popt_scaled = popt_original
                    except Exception:
                        popt_scaled, pcov = curve_fit(model_func, n_data, c_data, p0=[0.1, mean_count])
                elif model_name == 'Exponential':
                    # 指数模型使用原始数据直接拟合
                    try:
                        popt_original, pcov = curve_fit(model_func, data['n'], data['count'], 
                                                      p0=[mean_count, 0.0])
                        popt_scaled = popt_original
                    except Exception:
                        popt_scaled, pcov = curve_fit(model_func, n_data, c_data, p0=[mean_count, 0.01])
                elif model_name == 'Sqrt_Exponential':
                    # 平方根指数模型使用原始数据直接拟合
                    try:
                        popt_original, pcov = curve_fit(model_func, data['n'], data['count'], 
                                                      p0=[mean_count, 0.0])
                        popt_scaled = popt_original
                    except Exception:
                        popt_scaled, pcov = curve_fit(model_func, n_data, c_data, p0=[mean_count, 0.01])
                elif model_name == 'Power':
                    # 幂函数模型使用原始数据直接拟合
                    try:
                        popt_original, pcov = curve_fit(model_func, data['n'], data['count'], 
                                                      p0=[mean_count, 1.0])
                        popt_scaled = popt_original
                    except Exception:
                        popt_scaled, pcov = curve_fit(model_func, n_data, c_data, p0=[mean_count, 1.0])
                
                # 将缩放后的参数转换回原始单位
                # 缩放关系：
                # scaled_n = (n - n_min) * n_scale + 1
                # 转换公式：
                # n = (scaled_n - 1) / n_scale + n_min
                
                popt = np.copy(popt_scaled)
                
                # 根据模型类型转换参数
                if model_name in ['Linear', 'Quadratic', 'Cubic']:
                    # 这些模型需要转换参数，因为n被缩放了
                    if model_name == 'Linear':
                        # Linear: y = a*n + b
                        # 转换为缩放后的数据：y = a*((scaled_n - 1)/n_scale + n_min) + b
                        # → y = a*(scaled_n - 1)/n_scale + a*n_min + b
                        # → y = (a/n_scale)*scaled_n + (-a/n_scale + a*n_min + b)
                        # 所以：
                        # a_scaled = a / n_scale
                        # b_scaled = -a/n_scale + a*n_min + b
                        # 解这个方程组得到原始参数：
                        a = popt_scaled[0] * data['n_scale']
                        b = popt_scaled[1] - a * (data['n_min'] - 1 / data['n_scale'])
                        popt[0] = a
                        popt[1] = b
                    elif model_name == 'Quadratic':
                        # Quadratic: y = a*n² + b*n + c
                        a = popt_scaled[0] * (data['n_scale'] ** 2)
                        b = popt_scaled[1] * data['n_scale'] - 2 * a * data['n_min']
                        c = popt_scaled[2] - a * (data['n_min'] ** 2) - b * data['n_min']
                        popt[0] = a
                        popt[1] = b
                        popt[2] = c
                    elif model_name == 'Cubic':
                        # Cubic: y = a*n³ + b*n² + c*n + d
                        a = popt_scaled[0] * (data['n_scale'] ** 3)
                        b = popt_scaled[1] * (data['n_scale'] ** 2) - 3 * a * (data['n_min'] ** 2)
                        c = popt_scaled[2] * data['n_scale'] - 2 * b * data['n_min'] - 3 * a * (data['n_min'] ** 2)
                        d = popt_scaled[3] - a * (data['n_min'] ** 3) - b * (data['n_min'] ** 2) - c * data['n_min']
                        popt[0] = a
                        popt[1] = b
                        popt[2] = c
                        popt[3] = d
                
                # 计算R²值（使用转换后的参数对原始数据进行拟合）
                predicted = model_func(data['n'], *popt)
                residuals = data['count'] - predicted
                ss_res = np.sum(residuals**2)
                ss_tot = np.sum((data['count'] - np.mean(data['count']))**2)
                if ss_tot == 0:  # 处理所有计数相同的情况
                    r_squared = 1.0
                else:
                    r_squared = 1 - (ss_res / ss_tot)
                
                # 保存拟合结果
                fit_results[model_name] = {
                    'params': popt.tolist(),  # 保存原始参数
                    'r_squared': r_squared,
                    'success': True
                }
                
                print(f"{model_name}: R² = {r_squared:.6f}, 参数 = {popt.tolist()}")
                
            except Exception as e:
                fit_results[model_name] = {
                    'params': [],
                    'r_squared': 0,
                    'success': False,
                    'error': str(e)
                }
                print(f"{model_name}: 拟合失败 - {e}")
        
        # 找出最佳拟合模型
        best_model = max(fit_results.items(), key=lambda x: x[1]['r_squared'] if x[1]['success'] else 0)
        print(f"\n最佳拟合模型: {best_model[0]}, R² = {best_model[1]['r_squared']:.6f}")
        
        # 保存拟合结果
        fit_results_path = os.path.join(result_dir, "fit_results.json")
        with open(fit_results_path, 'w', encoding='utf-8') as f:
            json.dump(fit_results, f, indent=2, ensure_ascii=False)
        
        # 绘制原始数据和最佳拟合曲线
        plt.figure(figsize=(12, 8))
        
        plt.scatter(data['n'], data['count'], label='Actual Data', color='blue', alpha=0.5)
        
        # 绘制最佳拟合曲线
        if best_model[0] in ['Logarithmic', 'n_log_n']:
            # 对于对数模型，只在n>0时绘制
            plot_n = np.linspace(1, max(data['n']), 1000)
        else:
            plot_n = np.linspace(min(data['n']), max(data['n']), 1000)
        
        # 绘制模型拟合结果
        best_fit_values = models[best_model[0]](plot_n, *best_model[1]['params'])
        
        plt.plot(plot_n, best_fit_values,
                 label=f'Best Fit: {best_model[0]}', color='red', linewidth=2)
        
        plt.xlabel('Test Size (n)')
        plt.ylabel('Bytecode Instructions')
        plt.title(f'Time Complexity Analysis - {base_name}')
        plt.legend()
        plt.grid(True)
        plt.ticklabel_format(style='plain', axis='y')
        plot_path = os.path.join(result_dir, f"time_complexity_plot_{base_name}.png")
        plt.savefig(plot_path)
        plt.close()
        print(f'最佳拟合曲线已保存到 {plot_path}')
        
        # 绘制所有模型的拟合结果（除了指数模型，因为可能会导致数值溢出）
        plt.figure(figsize=(12, 8))
        plt.scatter(data['n'], data['count'], label='Actual Data', color='blue', alpha=0.5)
        
        for model_name, result in fit_results.items():
            if result['success'] and model_name not in ['Exponential', 'Sqrt_Exponential']:  # 跳过指数模型以避免数值问题
                model_values = models[model_name](plot_n, *result['params'])
                
                plt.plot(plot_n, model_values, 
                         label=f'{model_name} (R²={result["r_squared"]:.4f})')
        
        plt.xlabel('Test Size (n)')
        plt.ylabel('Bytecode Instructions')
        plt.title(f'All Models Comparison - {base_name}')
        plt.legend()
        plt.grid(True)
        plt.ticklabel_format(style='plain', axis='y')
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
            f.write(f"生成文件: {generated_code_path}\n")
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
            
            f.write(f"最佳拟合模型: {best_model[0]}\n")
            f.write(f"最佳R²值: {best_model[1]['r_squared']:.6f}\n")
        
        print(f"\n分析报告已保存到 {report_path}")
        print(f"所有结果已保存到目录 {result_dir}")
    else:
        print(f"\n数据点不足 ({len(test_results)} 个)，无法进行拟合分析")

# 主函数：执行完整的时间复杂度分析流程
def main():
    # 使用配置文件中的文件夹路径
    folder_path = config.logn_folder_path
    
    # 获取文件夹中所有的Python文件
    python_files = []
    for file in os.listdir(folder_path):
        if file.endswith('.py'):
            python_files.append(os.path.join(folder_path, file))
    
    # 按文件名排序
    python_files.sort()
    
    print(f"找到 {len(python_files)} 个Python文件，开始处理...")
    
    # 遍历所有Python文件，逐个处理
    for i, code_path in enumerate(python_files, 1):
        if(i%1==0):
            print(f"\n{'='*60}")
            print(f"处理文件 {i}/{len(python_files)}")
            print(f"{'='*60}")
            process_code_file(code_path, force_reanalyze=True)
            break
        
    
    print(f"\n{'='*60}")
    print("所有文件处理完成！")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
