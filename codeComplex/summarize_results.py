import json
import os
import re

def load_json_file(file_path):
    """加载JSON文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def read_file_content(file_path):
    """读取文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None
    except UnicodeDecodeError:
        # 尝试用其他编码方式读取
        try:
            with open(file_path, 'r', encoding='latin-1') as f:
                return f.read()
        except:
            return None

def main():
    # 定义文件路径
    stats_files = {
        'cubic': '/home/wuyankai/myResearch/codeComplex/demo/filteredData/python/cubic/stats_cubic.json',
        'linear': '/home/wuyankai/myResearch/codeComplex/demo/filteredData/python/linear/stats_linear.json',
        'logn': '/home/wuyankai/myResearch/codeComplex/demo/filteredData/python/logn/stats_logn.json',
        'nlogn': '/home/wuyankai/myResearch/codeComplex/demo/filteredData/python/nlogn/stats_nlogn.json',
        'quadratic': '/home/wuyankai/myResearch/codeComplex/demo/filteredData/python/quadratic/stats_quadratic.json'
    }
    
    # 加载LLM结果
    llm_results_file = '/home/wuyankai/myResearch/codeComplex/results/LLM/ast_llm_results1.json'
    llm_data = load_json_file(llm_results_file)
    
    # 创建LLM结果的映射字典，以complexity_id为键
    llm_map = {}
    for record in llm_data.get('detailed_records', []):
        complexity_id = record.get('complexity_id')
        if complexity_id:
            llm_map[complexity_id] = {
                'model_raw_output': record.get('model_raw_output'),
                'expected_complexity': record.get('expected_complexity'),
                'problem': record.get('problem')
            }
    
    # 构建最终结果列表
    all_results = []
    
    # 处理每个stats文件
    for complexity_type, stats_file_path in stats_files.items():
        stats_data = load_json_file(stats_file_path)
        
        # 获取失败的文件列表
        failed_files = stats_data.get('failed_files', [])
        
        for file_id in failed_files:
            # 构建complexity_id，格式为 'python_{complexity_type}_{id}'
            # 例如: python_cubic_0001.py -> python_cubic_0001
            # 从ID中提取类型和编号部分
            # ID格式是: python_{type}_{number}.py
            parts = file_id.split('_')
            if len(parts) >= 3 and file_id.endswith('.py'):
                # 提取类型和编号，如: python_cubic_0001.py -> python_cubic_0001
                complexity_type_from_id = parts[1]  # cubic
                file_number = '_'.join(parts[2:]).replace('.py', '')  # 0001 (remove .py)
                complexity_id = f"python_{complexity_type_from_id}_{file_number}"
            else:
                # 如果格式不符合预期，尝试直接使用文件名（去掉.py）
                if file_id.endswith('.py'):
                    file_base = file_id[:-3]  # 移除 '.py' 后缀
                else:
                    file_base = file_id
                complexity_id = file_base
            
            # 获取LLM结果
            llm_info = llm_map.get(complexity_id, {})
            
            # 构建文件路径
            filtered_data_path = f"/home/wuyankai/myResearch/codeComplex/data/filteredData/python/{complexity_type}/{file_id}"
            only_code_path = f"/home/wuyankai/myResearch/codeComplex/data/onlyCode/python/{complexity_type}/{file_id}"
            
            # 读取文件内容
            filtered_data_content = read_file_content(filtered_data_path)
            only_code_content = read_file_content(only_code_path)
            
            # 查找bestfit_output - 在对应的结果文件夹中的analysis_report.json
            # 根据ID构建结果文件夹名，例如: python_cubic_0001.py -> results_python_cubic_0001
            folder_name = f"results_{file_id.replace('.py', '')}"
            
            # 遍历可能的复杂度类型目录查找结果文件夹
            bestfit_output = ""
            demo_filtered_data_dir = "/home/wuyankai/myResearch/codeComplex/demo/filteredData/python"
            for complexity_type_check in ['cubic', 'linear', 'logn', 'nlogn', 'quadratic']:
                analysis_report_path = os.path.join(demo_filtered_data_dir, complexity_type_check, folder_name, 'analysis_report.json')
                if os.path.exists(analysis_report_path):
                    try:
                        with open(analysis_report_path, 'r', encoding='utf-8') as f:
                            analysis_report = json.load(f)
                        
                        # 找到R²值最高的模型
                        best_model = ""
                        best_r2 = -float('inf')
                        for model_name, model_data in analysis_report.items():
                            if 'r2' in model_data and model_data['r2'] > best_r2:
                                best_r2 = model_data['r2']
                                best_model = model_name
                        
                        # 将最佳拟合模型名称转换为小写并替换空格为下划线
                        bestfit_output = best_model.lower().replace(' ', '_')
                        break  # 找到就退出循环
                    except Exception as e:
                        print(f"Error reading {analysis_report_path}: {e}")
                        bestfit_output = ""
            
            # 构建结果项
            result_item = {
                'ID': file_id,
                'model_raw_output': llm_info.get('model_raw_output'),
                'expected_complexity': llm_info.get('expected_complexity'),
                'problem': llm_info.get('problem'),
                'filteredData': filtered_data_content,
                'onlyCode': only_code_content,
                'bestfit_output': bestfit_output
            }
            
            all_results.append(result_item)
    
    # 输出结果到JSON文件
    output_file = '/home/wuyankai/myResearch/codeComplex/summarized_results.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    
    print(f"成功汇总了 {len(all_results)} 个失败的文件结果")
    print(f"结果已保存到 {output_file}")

if __name__ == "__main__":
    main()