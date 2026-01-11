import os
import json
import glob

def get_best_fit_model(report_path):
    """从analysis_report.json中获取bestfit模型（r2最高的模型）"""
    with open(report_path, 'r') as f:
        report = json.load(f)
    
    best_model = None
    best_r2 = -float('inf')
    
    for model_name, model_data in report.items():
        r2 = model_data.get('r2', -float('inf'))
        if r2 > best_r2:
            best_r2 = r2
            best_model = model_name
    
    return best_model

def normalize_model_name(model_name):
    """将模型名称标准化为与JSON中model_raw_output一致的格式"""
    model_mapping = {
        "Constant": "constant",
        "Linear": "linear",
        "Quadratic": "quadratic",
        "Cubic": "cubic",
        "Logarithmic": "logn",
        "N Log N": "nlogn"
    }
    return model_mapping.get(model_name, model_name.lower())

def main():
    # 设置路径
    base_dir = "/home/wuyankai/myResearch/codeComplex/demo/filteredData/python"
    json_path = "/home/wuyankai/myResearch/codeComplex/results/LLM/ast_llm_results1.json"
    
    # 读取JSON文件，构建complexity_id到model_raw_output的映射
    with open(json_path, 'r') as f:
        json_data = json.load(f)
    
    # 创建complexity_id到model_raw_output的映射字典
    complexity_map = {}
    for record in json_data['detailed_records']:
        complexity_id = record.get('complexity_id')
        model_output = record.get('model_raw_output')
        if complexity_id and model_output:
            complexity_map[complexity_id] = model_output
    
    # 初始化比较结果
    comparison_results = {
        'total': 0,
        'matched': 0,
        'unmatched': 0,
        'not_found': 0,
        'details': []
    }
    
    # 遍历四个复杂度目录
    complexity_types = ['linear', 'logn', 'nlogn', 'quadratic']
    
    for complexity_type in complexity_types:
        dir_path = os.path.join(base_dir, complexity_type)
        
        # 找到所有results_python_xxx_xxxx子目录
        result_dirs = glob.glob(os.path.join(dir_path, "results_python_*"))
        
        for result_dir in result_dirs:
            # 提取complexity_id
            dir_name = os.path.basename(result_dir)
            complexity_id = dir_name.replace("results_", "")
            
            # 读取analysis_report.json
            report_path = os.path.join(result_dir, "analysis_report.json")
            if not os.path.exists(report_path):
                print(f"Warning: analysis_report.json not found in {result_dir}")
                continue
            
            # 获取bestfit模型
            best_fit_model = get_best_fit_model(report_path)
            normalized_bestfit = normalize_model_name(best_fit_model)
            
            # 获取model_raw_output
            if complexity_id in complexity_map:
                model_raw_output = complexity_map[complexity_id]
                is_match = normalized_bestfit == model_raw_output
            else:
                model_raw_output = "Not Found"
                is_match = False
            
            # 记录结果
            comparison_results['total'] += 1
            if is_match:
                comparison_results['matched'] += 1
            elif model_raw_output == "Not Found":
                comparison_results['not_found'] += 1
            else:
                comparison_results['unmatched'] += 1
            
            comparison_results['details'].append({
                'complexity_id': complexity_id,
                'bestfit_model': best_fit_model,
                'normalized_bestfit': normalized_bestfit,
                'model_raw_output': model_raw_output,
                'is_match': is_match
            })
    
    # 生成报告
    print("=== Bestfit vs Model Raw Output Comparison ===")
    print(f"Total records: {comparison_results['total']}")
    print(f"Matched: {comparison_results['matched']}")
    print(f"Unmatched: {comparison_results['unmatched']}")
    print(f"Not Found in JSON: {comparison_results['not_found']}")
    print(f"Match rate: {comparison_results['matched'] / comparison_results['total'] * 100:.2f}%" if comparison_results['total'] > 0 else "No records found")
    
    # 保存详细结果到文件
    output_path = "/home/wuyankai/myResearch/codeComplex/bestfit_comparison_results.json"
    with open(output_path, 'w') as f:
        json.dump(comparison_results, f, indent=2)
    
    print(f"\nDetailed results saved to: {output_path}")
    
    # 打印前10个不匹配的结果作为示例
    print("\n=== First 10 Unmatched Results ===")
    unmatched_count = 0
    for result in comparison_results['details']:
        if not result['is_match'] and result['model_raw_output'] != "Not Found":
            print(f"ID: {result['complexity_id']}, Bestfit: {result['normalized_bestfit']}, Model Output: {result['model_raw_output']}")
            unmatched_count += 1
            if unmatched_count >= 10:
                break

if __name__ == "__main__":
    main()