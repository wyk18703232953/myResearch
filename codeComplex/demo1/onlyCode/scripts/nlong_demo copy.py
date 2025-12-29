import sys
import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import os
import dis
from io import StringIO
from openai import OpenAI

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
        api_key (str, optional): OpenAI API密钥
        base_url (str, optional): API基础URL
        
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
    9. main(n)函数必须有返回值或执行完整的计算逻辑
    
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
        if model_raw_output.startswith('```python'):
            model_raw_output = model_raw_output[10:]
        if model_raw_output.endswith('```'):
            model_raw_output = model_raw_output[:-3]
        
        return model_raw_output.strip()
        
    except Exception as e:
        error_msg = str(e)
        print(f"调用大模型时出错: {error_msg}")
        raise Exception(f"调用大模型失败: {error_msg}") from e

# 统计字节码数量的函数
def count_bytecode_instructions(code_str, n):
    """统计执行代码时的字节码指令数量
    
    Args:
        code_str: str, 要执行的代码字符串
        n: int, 测试规模
        
    Returns:
        int: 字节码指令数量
    """
    try:
        # 构造完整的测试代码
        test_code = f"""{code_str}

# 执行测试
main({n})
"""
        
        # 编译代码
        compiled_code = compile(test_code, '<string>', 'exec')
        
        # 统计字节码指令数
        instruction_count = 0
        
        # 递归统计所有代码对象的指令数
        def count_instructions(code_obj):
            count = len(list(dis.get_instructions(code_obj)))
            # 递归统计嵌套的代码对象
            for const in code_obj.co_consts:
                if hasattr(const, 'co_code'):
                    count += count_instructions(const)
            return count
        
        instruction_count = count_instructions(compiled_code)
        
        return instruction_count
        
    except Exception as e:
        print(f"统计字节码时出错: {e}")
        raise

# 处理单个数据记录的函数
def process_single_record(record_id, src_code, result_dir):
    """处理单个数据记录，执行完整的时间复杂度分析流程
    
    Args:
        record_id: int, 记录ID
        src_code: str, 原始源代码
        result_dir: str, 结果保存目录
    """
    print(f"\n{'='*60}")
    print(f"处理记录 ID: {record_id}")
    print(f"{'='*60}")
    
    # 创建该记录的结果目录
    record_dir = os.path.join(result_dir, f"record_{record_id}")
    os.makedirs(record_dir, exist_ok=True)
    
    # 保存原始代码
    original_code_path = os.path.join(record_dir, "original_code.py")
    with open(original_code_path, 'w', encoding='utf-8') as f:
        f.write(src_code)
    print(f"1. 原始代码已保存: {original_code_path}")
    
    # 构建生成程序的文件路径
    generated_code_path = os.path.join(record_dir, "generated_code.py")
    
    # 检查是否已经存在生成的程序文件
    if os.path.exists(generated_code_path):
        print(f"2. 检测到已存在生成的程序，直接读取: {generated_code_path}")
        with open(generated_code_path, 'r', encoding='utf-8') as f:
            generated_code = f.read()
    else:
        # 调用大模型生成可执行程序
        print("2. 调用大模型生成可执行程序...")
        try:
            generated_code = call_large_model(src_code)
            print("生成成功")
            
            # 保存生成的程序
            with open(generated_code_path, 'w', encoding='utf-8') as f:
                f.write(generated_code)
            print(f"生成的程序已保存到: {generated_code_path}")
        except Exception as e:
            print(f"生成代码失败: {e}")
            return
    
    # 创建测试结果文件
    test_results = []
    max_n = config.max_n
    step = config.step
    start_n = config.start_n
    
    # 检查是否已经有部分结果
    temp_results_path = os.path.join(record_dir, "temp_results.npz")
    if os.path.exists(temp_results_path):
        loaded_data = np.load(temp_results_path)
        test_results = loaded_data['results'].tolist()
        start_n = int(test_results[-1][0]) + step if test_results else start_n
        print(f"继续从n={start_n}开始分析")
    
    try:
        # 对于每个测试规模n
        print(f"\n3. 执行字节码计数测试: n = {start_n} 到 {max_n}, 步长 {step}")
        for n in range(start_n, max_n + 1, step):
            try:
                # 统计字节码指令数
                bytecode_count = count_bytecode_instructions(generated_code, n)
                
                # 保存结果
                test_results.append((n, bytecode_count))
                
                # 输出进度
                if n % 100 == 0 or n == max_n:
                    print(f'完成 n={n}, 字节码数={bytecode_count}')
                
                # 每10个点保存一次临时数据
                if len(test_results) % 10 == 0:
                    np.savez(temp_results_path, results=test_results)
                    
            except Exception as e:
                print(f"测试 n={n} 时出错: {e}")
                continue
                
    except KeyboardInterrupt:
        print("\n分析被用户中断，保存已收集的数据...")
    except Exception as e:
        print(f"\n分析过程中发生错误: {e}")
        import traceback
        traceback.print_exc()
    finally:
        # 保存最终结果
        final_results_path = os.path.join(record_dir, "bytecode_results.npz")
        np.savez(final_results_path, results=test_results)
        print(f'最终数据已保存到 {final_results_path}')
    
    # 如果收集到的数据点足够，进行拟合分析
    if len(test_results) >= 3:
        # 加载结果
        loaded_results = np.array(test_results)
        n_values = loaded_results[:, 0]
        bytecode_values = loaded_results[:, 1]
        
        # 对不同的时间复杂度模型进行拟合
        data = {
            'n': n_values,
            'bytecode': bytecode_values
        }
        
        # 尝试拟合不同的模型
        models = {
            'Constant': constant,
            'Linear': linear,
            'Quadratic': quadratic,
            'Cubic': cubic,
            'Logarithmic': logarithmic,
            'n_log_n': n_log_n,
            'Power': power
        }
        
        # 保存拟合结果
        fit_results = {}
        
        print("\n4. 开始进行复杂度拟合分析...")
        for model_name, model_func in models.items():
            try:
                # 尝试拟合
                if model_name == 'Constant':
                    popt, pcov = curve_fit(model_func, data['n'], data['bytecode'], p0=[np.mean(data['bytecode'])])
                elif model_name == 'Linear':
                    popt, pcov = curve_fit(model_func, data['n'], data['bytecode'], p0=[1, 0])
                elif model_name == 'Quadratic':
                    popt, pcov = curve_fit(model_func, data['n'], data['bytecode'], p0=[0.001, 1, 0])
                elif model_name == 'Cubic':
                    popt, pcov = curve_fit(model_func, data['n'], data['bytecode'], p0=[0.00001, 0.001, 1, 0])
                elif model_name == 'Logarithmic':
                    popt, pcov = curve_fit(model_func, data['n'], data['bytecode'], p0=[100, 0])
                elif model_name == 'n_log_n':
                    popt, pcov = curve_fit(model_func, data['n'], data['bytecode'], p0=[1, 0])
                elif model_name == 'Power':
                    popt, pcov = curve_fit(model_func, data['n'], data['bytecode'], p0=[1, 1])
                
                # 计算R²值
                residuals = data['bytecode'] - model_func(data['n'], *popt)
                ss_res = np.sum(residuals**2)
                ss_tot = np.sum((data['bytecode'] - np.mean(data['bytecode']))**2)
                if ss_tot == 0:
                    r_squared = 1.0
                else:
                    r_squared = 1 - (ss_res / ss_tot)
                
                # 保存拟合结果
                fit_results[model_name] = {
                    'params': popt.tolist(),
                    'r_squared': r_squared,
                    'success': True
                }
                
                print(f"{model_name}: R² = {r_squared:.6f}, 参数 = {popt}")
                
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
        fit_results_path = os.path.join(record_dir, "fit_results.json")
        with open(fit_results_path, 'w', encoding='utf-8') as f:
            json.dump(fit_results, f, indent=2, ensure_ascii=False)
        
        # 绘制原始数据和最佳拟合曲线
        plt.figure(figsize=(12, 8))
        plt.scatter(data['n'], data['bytecode'], label='Actual Data', color='blue', alpha=0.5)
        
        # 绘制最佳拟合曲线
        if best_model[0] in ['Logarithmic', 'n_log_n']:
            plot_n = np.linspace(1, max(data['n']), 1000)
        else:
            plot_n = np.linspace(min(data['n']), max(data['n']), 1000)
        
        plt.plot(plot_n, models[best_model[0]](plot_n, *best_model[1]['params']), 
                 label=f'Best Fit: {best_model[0]}', color='red', linewidth=2)
        
        plt.xlabel('Test Size (n)')
        plt.ylabel('Bytecode Instruction Count')
        plt.title(f'Complexity Analysis - Record {record_id}')
        plt.legend()
        plt.grid(True)
        plot_path = os.path.join(record_dir, f"complexity_plot.png")
        plt.savefig(plot_path)
        plt.close()
        print(f'最佳拟合曲线已保存到 {plot_path}')
        
        # 绘制所有模型的拟合结果
        plt.figure(figsize=(12, 8))
        plt.scatter(data['n'], data['bytecode'], label='Actual Data', color='blue', alpha=0.5)
        
        for model_name, result in fit_results.items():
            if result['success']:
                try:
                    plt.plot(plot_n, models[model_name](plot_n, *result['params']), 
                             label=f'{model_name} (R²={result["r_squared"]:.4f})')
                except:
                    pass
        
        plt.xlabel('Test Size (n)')
        plt.ylabel('Bytecode Instruction Count')
        plt.title(f'All Models Comparison - Record {record_id}')
        plt.legend()
        plt.grid(True)
        comparison_path = os.path.join(record_dir, f"all_models_comparison.png")
        plt.savefig(comparison_path)
        plt.close()
        print(f'所有模型对比图已保存到 {comparison_path}')
        
        # 生成报告
        report_path = os.path.join(record_dir, f"complexity_report.txt")
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"时间复杂度分析报告\n")
            f.write(f"====================\n\n")
            f.write(f"记录ID: {record_id}\n")
            f.write(f"测试参数: n = {config.start_n} 到 {max_n}, 步长 {step}\n")
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
                    f.write(f"{model_name}: 拟合失败 - {result.get('error', 'Unknown error')}\n")
                f.write("\n")
            
            f.write(f"最佳拟合模型: {best_model[0]}\n")
            f.write(f"最佳R²值: {best_model[1]['r_squared']:.6f}\n")
            f.write(f"\n推断的时间复杂度: O({best_model[0]})\n")
        
        print(f"\n分析报告已保存到 {report_path}")
        print(f"所有结果已保存到目录 {record_dir}")
    else:
        print(f"\n数据点不足 ({len(test_results)} 个)，无法进行拟合分析")

# 主函数：处理数据集的前5条记录
def main():
    # 读取数据集
    dataset_path = config.nlogn_folder_path  # 需要在config中配置数据集路径
    
    print(f"读取数据集: {dataset_path}")
    
    # 读取JSONL数据集
    try:
        dataset = []
        with open(dataset_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    dataset.append(json.loads(line.strip()))
    except Exception as e:
        print(f"读取数据集失败: {e}")
        return
    
    # 获取前5条记录
    records = dataset[:5] if len(dataset) >= 5 else dataset
    print(f"获取到 {len(records)} 条记录")
    
    # 创建结果目录
    result_dir = config.nlogn_results_base_dir
    os.makedirs(result_dir, exist_ok=True)
    
    # 遍历每条记录
    for i, record in enumerate(records):
        record_id = record.get('id', i)
        src_code = record.get('src', '')
        
        if not src_code:
            print(f"记录 {record_id} 没有src字段，跳过")
            continue
        
        # 处理单条记录
        try:
            process_single_record(record_id, src_code, result_dir)
        except Exception as e:
            print(f"处理记录 {record_id} 时发生错误: {e}")
            import traceback
            traceback.print_exc()
            continue
        break
    
    print(f"\n{'='*60}")
    print("所有记录处理完成！")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()