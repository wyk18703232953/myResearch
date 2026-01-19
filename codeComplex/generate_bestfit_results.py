import os
import json
import glob
from collections import defaultdict

# 定义复杂度类型映射
COMPLEXITY_TYPES = {
    'constant': 'Constant',
    'linear': 'Linear',
    'logarithmic': 'Logarithmic',
    'nlogn': 'N Log N',
    'quadratic': 'Quadratic',
    'cubic': 'Cubic'
}

# 标准化模型名称映射
NORMALIZE_MAP = {
    'Constant': 'constant',
    'Linear': 'linear',
    'Logarithmic': 'logn',
    'N Log N': 'nlogn',
    'Quadratic': 'quadratic',
    'Cubic': 'cubic'
}

def get_bestfit_model(models):
    """从models字典中找到confidence_score最高的模型"""
    if not models:
        return None
    
    best_model = None
    best_score = -1
    
    for model_name, model_data in models.items():
        score = model_data.get('confidence_score', 0)
        if score > best_score:
            best_score = score
            best_model = model_name
    
    return best_model

def main():
    # 定义输入和输出路径
    input_dir = '/home/wuyankai/myResearch/codeComplex/demo/filteredData/python'
    output_file = '/home/wuyankai/myResearch/codeComplex/bestfit_comparison_results_new.json'
    
    # 初始化统计变量
    total = 0
    matched = 0
    unmatched = 0
    not_found = 0
    details = []
    
    # 遍历所有复杂度类型目录
    for complexity_type in os.listdir(input_dir):
        type_dir = os.path.join(input_dir, complexity_type)
        if not os.path.isdir(type_dir):
            continue
        
        # 遍历该类型下的所有results目录
        results_dirs = glob.glob(os.path.join(type_dir, f'results_python_{complexity_type}_*'))
        for results_dir in results_dirs:
            # 提取complexity_id
            dir_name = os.path.basename(results_dir)
            complexity_id = f'python_{complexity_type}_{dir_name.split("_")[-1]}'
            
            # 找到analysis_report.json文件
            report_file = os.path.join(results_dir, 'analysis_report.json')
            if not os.path.exists(report_file):
                not_found += 1
                continue
            
            # 读取分析报告
            try:
                with open(report_file, 'r') as f:
                    report_data = json.load(f)
            except json.JSONDecodeError:
                not_found += 1
                continue
            except Exception as e:
                print(f"Error reading {report_file}: {e}")
                not_found += 1
                continue
            
            # 获取最佳拟合模型
            models = report_data.get('models', {})
            bestfit_model = get_bestfit_model(models)
            
            if bestfit_model is None:
                not_found += 1
                continue
            
            # 计算is_match
            expected_model = COMPLEXITY_TYPES.get(complexity_type, complexity_type)
            is_match = (bestfit_model == expected_model)
            
            # 获取标准化名称
            normalized_bestfit = NORMALIZE_MAP.get(bestfit_model, bestfit_model.lower())
            
            # 构建详细信息
            detail = {
                'complexity_id': complexity_id,
                'bestfit_model': bestfit_model,
                'normalized_bestfit': normalized_bestfit,
                'model_raw_output': normalized_bestfit,  # 这里使用标准化后的结果作为raw_output
                'is_match': is_match
            }
            
            # 更新统计信息
            total += 1
            if is_match:
                matched += 1
            else:
                unmatched += 1
            
            details.append(detail)
    
    # 构建最终结果
    result = {
        'total': total,
        'matched': matched,
        'unmatched': unmatched,
        'not_found': not_found,
        'details': details
    }
    
    # 写入输出文件
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"Generated bestfit comparison results:")
    print(f"Total: {total}")
    print(f"Matched: {matched}")
    print(f"Unmatched: {unmatched}")
    print(f"Not Found: {not_found}")
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()