import time
import re
import json
import matplotlib.pyplot as plt
import numpy as np
import ast
import os
import sys
from scipy.optimize import curve_fit

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

# 静态分析模块 - AST分析和控制流分析
class StaticAnalyzer:
    """静态代码分析器，使用AST和简单的CFG分析预测时间复杂度"""
    
    def __init__(self, code):
        self.code = code
        self.tree = ast.parse(code)
        self.loop_info = {
            'loop_count': 0,
            'nested_depth': 0,
            'max_nested_depth': 0,
            'loop_types': {}
        }
        self.data_structures = set()
        self.advanced_features = set()
        self.current_depth = 0
    
    def analyze(self):
        """执行完整的静态分析"""
        self._analyze_ast(self.tree)
        return self._predict_complexity()
    
    def _analyze_ast(self, node, depth=0):
        """递归分析AST节点"""
        # 分析循环结构
        if isinstance(node, (ast.For, ast.While)):
            loop_type = 'for' if isinstance(node, ast.For) else 'while'
            self.loop_info['loop_count'] += 1
            self.loop_info['loop_types'][loop_type] = self.loop_info['loop_types'].get(loop_type, 0) + 1
            
            # 更新嵌套深度
            self.current_depth = depth + 1
            if self.current_depth > self.loop_info['max_nested_depth']:
                self.loop_info['max_nested_depth'] = self.current_depth
        
        # 分析数据结构使用
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                func_name = node.func.id
                if func_name in ['list', 'dict', 'set', 'tuple']:
                    self.data_structures.add(func_name)
                elif func_name in ['sort', 'sorted', 'append', 'extend', 'insert', 'pop', 'remove']:
                    self.data_structures.add('list_operations')
                elif func_name in ['keys', 'values', 'items', 'get']:
                    self.data_structures.add('dict_operations')
                elif func_name in ['add', 'discard', 'union', 'intersection']:
                    self.data_structures.add('set_operations')
            
            # 检查方法调用（如obj.method()）
            elif isinstance(node.func, ast.Attribute):
                attr_name = node.func.attr
                if attr_name in ['append', 'extend', 'insert', 'pop', 'remove', 'sort']:
                    self.data_structures.add('list_operations')
                elif attr_name in ['keys', 'values', 'items', 'get']:
                    self.data_structures.add('dict_operations')
                elif attr_name in ['add', 'discard', 'union', 'intersection']:
                    self.data_structures.add('set_operations')
        
        # 分析高级语言特性
        if isinstance(node, ast.Lambda):
            self.advanced_features.add('lambda')
        elif isinstance(node, (ast.ListComp, ast.DictComp, ast.SetComp)):
            self.advanced_features.add('comprehension')
        elif isinstance(node, ast.GeneratorExp):
            self.advanced_features.add('generator')
        
        # 递归分析子节点
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.For, ast.While)):
                self._analyze_ast(child, depth + 1)
            else:
                self._analyze_ast(child, depth)
    
    def _predict_complexity(self):
        """基于AST分析结果预测时间复杂度"""
        max_depth = self.loop_info['max_nested_depth']
        loop_count = self.loop_info['loop_count']
        
        # 基于循环嵌套深度预测复杂度
        if max_depth == 0:
            return 'Constant'
        elif max_depth == 1:
            # 检查是否包含对数操作
            if 'sort' in str(self.code) or 'sorted' in str(self.code):
                return 'Linearithmic'  # O(n log n)
            return 'Linear'  # O(n)
        elif max_depth == 2:
            return 'Quadratic'  # O(n²)
        elif max_depth == 3:
            return 'Cubic'  # O(n³)
        else:
            return 'Polynomial'  # O(n^k), k>3
    
    def get_analysis_details(self):
        """返回详细的分析结果"""
        return {
            'loop_info': self.loop_info,
            'data_structures': list(self.data_structures),
            'advanced_features': list(self.advanced_features),
            'ast_tree': ast.dump(self.tree, indent=2)
        }

# 简化的CFG构建和分析
def build_simple_cfg(ast_tree):
    """构建简单的控制流图"""
    cfg = {}
    node_id = 0
    
    def traverse(node, parent_id=None):
        nonlocal node_id
        current_id = node_id
        node_id += 1
        
        # 记录节点类型和父节点
        cfg[current_id] = {
            'type': type(node).__name__,
            'parent': parent_id,
            'children': []
        }
        
        # 遍历子节点
        for child in ast.iter_child_nodes(node):
            child_id = traverse(child, current_id)
            cfg[current_id]['children'].append(child_id)
        
        return current_id
    
    traverse(ast_tree)
    return cfg

def analyze_cfg_complexity(cfg):
    """分析CFG复杂度"""
    loop_nodes = [id for id, node in cfg.items() if node['type'] in ['For', 'While']]
    return {
        'total_nodes': len(cfg),
        'loop_nodes': len(loop_nodes),
        'branch_nodes': sum(1 for id, node in cfg.items() if node['type'] in ['If', 'Elif'])
    }

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
    from openai import OpenAI
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
def process_code_file(code_path):
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
    result_dir = f"{config.cubic_results_base_dir}/results_{base_name}"
    os.makedirs(result_dir, exist_ok=True)
    
    # 执行静态AST/CFG分析
    print(f"\n2. 执行静态AST/CFG分析...")
    static_analyzer = StaticAnalyzer(original_code)
    static_prediction = static_analyzer.analyze()
    static_details = static_analyzer.get_analysis_details()
    
    # 构建并分析CFG
    tree = ast.parse(original_code)
    cfg = build_simple_cfg(tree)
    cfg_complexity = analyze_cfg_complexity(cfg)
    
    print(f"静态分析预测的时间复杂度: {static_prediction}")
    print(f"循环信息: {static_details['loop_info']}")
    print(f"使用的数据结构: {static_details['data_structures']}")
    print(f"使用的高级特性: {static_details['advanced_features']}")
    print(f"CFG复杂度: {cfg_complexity}")
    
    # 保存静态分析结果
    static_analysis_path = os.path.join(result_dir, "static_analysis_results.json")
    with open(static_analysis_path, 'w', encoding='utf-8') as f:
        json.dump({
            'predicted_complexity': static_prediction,
            'loop_info': static_details['loop_info'],
            'data_structures': static_details['data_structures'],
            'advanced_features': static_details['advanced_features'],
            'cfg_complexity': cfg_complexity
        }, f, indent=2, ensure_ascii=False)
    
    # 构建生成程序的文件路径
    generated_code_path = os.path.join(result_dir, f"generated_{base_name}.py")
    
    # 检查是否已经存在生成的程序文件
    if os.path.exists(generated_code_path):
        print(f"\n3. 检测到已存在生成的程序，直接读取：{generated_code_path}")
        with open(generated_code_path, 'r', encoding='utf-8') as f:
            generated_code = f.read()
        print(f"读取到的程序：")
        print(generated_code)
    else:
        # 调用大模型生成可执行程序
        print(f"\n3. 调用大模型生成可执行程序...")
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
        print(f"\n4. 执行时间测试：n = {start_n} 到 {max_n}，步长 {step}")
        for n in range(start_n, max_n + 1, step):
            # 构造完整的测试代码
            test_code = f"""{generated_code}

# 执行测试
main({n})
"""
            
            # 记录开始时间
            start_time = time.time()
            # 创建一个临时环境并执行代码
            exec_globals = {}
            exec(test_code, exec_globals)
            
            # 记录结束时间
            end_time = time.time()
            
            # 计算运行时间
            run_time = end_time - start_time
            
            # 保存结果
            test_results.append((n, run_time))
            
            # 记录当前分析的数据点数量
            current_datapoints = len(test_results)
            
            # 每10个点保存一次临时数据，防止程序中断导致数据丢失
            if current_datapoints % 10 == 0:
                np.savez(temp_results_path, results=test_results)
                
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
        
        print(f"\n5. 开始进行时间复杂度拟合分析...")
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
        fit_results_path = os.path.join(result_dir, "fit_results.json")
        with open(fit_results_path, 'w', encoding='utf-8') as f:
            json.dump(fit_results, f, indent=2, ensure_ascii=False)
        
        # 绘制原始数据和最佳拟合曲线
        plt.figure(figsize=(12, 8))
        plt.scatter(data['n'], data['time'], label='Actual Data', color='blue', alpha=0.5)
        
        # 绘制最佳拟合曲线
        if best_model[0] in ['Logarithmic', 'n_log_n']:
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
            f.write(f"生成文件: {generated_code_path}\n")
            f.write(f"分析时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # 添加静态分析结果
            f.write(f"=== 静态AST/CFG分析结果 ===\n")
            f.write(f"预测的时间复杂度: {static_prediction}\n")
            f.write(f"循环信息: {static_details['loop_info']}\n")
            f.write(f"使用的数据结构: {static_details['data_structures']}\n")
            f.write(f"使用的高级特性: {static_details['advanced_features']}\n")
            f.write(f"CFG复杂度: {cfg_complexity}\n\n")
            
            f.write(f"=== 动态运行时间分析 ===\n")
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
            f.write(f"最佳R²值: {best_model[1]['r_squared']:.6f}\n\n")
            
            # 添加静态分析与动态分析对比
            f.write(f"=== 静态分析与动态分析对比 ===\n")
            f.write(f"静态分析预测: {static_prediction}\n")
            f.write(f"动态分析结果: {best_model[0]}\n")
            f.write(f"一致性: {'一致' if static_prediction == best_model[0] else '不一致'}\n")
        
        print(f"\n分析报告已保存到 {report_path}")
        print(f"所有结果已保存到目录 {result_dir}")
    else:
        print(f"\n数据点不足 ({len(test_results)} 个)，无法进行拟合分析")

# 主函数：执行完整的时间复杂度分析流程
def main():
    # 使用配置文件中的文件夹路径
    folder_path = config.cubic_folder_path
    
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
        if(i%12==0):
            print(f"\n{'='*60}")
            print(f"处理文件 {i}/{len(python_files)}")
            print(f"{'='*60}")
            process_code_file(code_path)
    
    print(f"\n{'='*60}")
    print("所有文件处理完成！")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()