import os
import json
import re
from collections import defaultdict

def extract_actual_complexity(folder_name):
    """从文件夹名称提取真实的复杂度类型"""
    match = re.search(r'results_python_(\w+)_', folder_name)
    if match:
        complexity_name = match.group(1)
        mapping = {
            'logn': 'O(log n)',
            'n': 'O(n)',
            'nlogn': 'O(n log n)',
            'n2': 'O(n^2)',
            'n3': 'O(n^3)',
            'linear': 'O(n)',
            'quadratic': 'O(n^2)',
            'cubic': 'O(n^3)',
            'constant': 'O(1)',
            'sqrt': 'O(sqrt(n))',
            'exp': 'O(2^n)',
        }
        return mapping.get(complexity_name, complexity_name)
    return None

def normalize_model_name(model_name):
    """标准化模型名称以便比较"""
    if model_name is None:
        return None
    
    name = model_name.lower().replace('o(', '').replace(')', '').replace('^', '').strip()
    
    # 清理参数
    name = re.sub(r'[0-9.]+', '', name)
    name = name.replace(' ', '')
    
    # 映射到标准名称
    if 'constant' in name or name == '1':
        return 'Constant'
    elif 'linear' in name or name == 'n':
        return 'Linear'
    elif 'quadratic' in name or name == 'n2':
        return 'Quadratic'
    elif 'cubic' in name or name == 'n3':
        return 'Cubic'
    elif 'log' in name:
        return 'Logarithmic'
    elif 'n log' in name or 'nlogn' in name:
        return 'n_log_n'
    elif 'power' in name:
        return 'Power'
    elif 'exp' in name or '2' in name:
        return 'Exponential'
    else:
        return model_name

def main():
    results_dir = r"d:\MyResearch\codeComplex\demo\onlyCode\results\logn"
    
    # 存储统计结果
    total_count = 0
    correct_count = 0
    error_cases = []
    missing_report_cases = []
    
    # 按真实复杂度类型统计
    complexity_stats = defaultdict(lambda: {'total': 0, 'correct': 0, 'details': []})
    
    # 遍历所有结果文件夹
    for folder_name in os.listdir(results_dir):
        folder_path = os.path.join(results_dir, folder_name)
        if not os.path.isdir(folder_name):
            continue
        
        # 提取真实的复杂度类型
        actual_complexity = extract_actual_complexity(folder_name)
        if actual_complexity is None:
            print(f"无法解析文件夹名称: {folder_name}")
            continue
        
        # 读取 report.json
        report_path = os.path.join(folder_path, 'report.json')
        if not os.path.exists(report_path):
            missing_report_cases.append(folder_name)
            continue
        
        try:
            with open(report_path, 'r', encoding='utf-8') as f:
                report = json.load(f)
            
            # 获取预测的最佳模型
            predicted_model = report.get('best_model', None)
            
            # 标准化模型名称
            actual_normalized = normalize_model_name(actual_complexity)
            predicted_normalized = normalize_model_name(predicted_model)
            
            total_count += 1
            complexity_stats[actual_complexity]['total'] += 1
            
            is_correct = actual_normalized == predicted_normalized
            if is_correct:
                correct_count += 1
                complexity_stats[actual_complexity]['correct'] += 1
            else:
                error_cases.append({
                    'folder': folder_name,
                    'actual': actual_complexity,
                    'predicted': predicted_model
                })
            
            complexity_stats[actual_complexity]['details'].append({
                'folder': folder_name,
                'actual': actual_complexity,
                'predicted': predicted_model,
                'correct': is_correct
            })
            
        except Exception as e:
            print(f"处理文件夹 {folder_name} 时出错: {e}")
            continue
    
    # 输出统计结果
    print("=" * 60)
    print("复杂度识别准确率统计")
    print("=" * 60)
    print(f"\n总体统计:")
    print(f"  总测试用例数: {total_count}")
    print(f"  正确识别数: {correct_count}")
    print(f"  准确率: {correct_count/total_count*100:.2f}%")
    
    print(f"\n缺失 report.json 的文件夹: {len(missing_report_cases)}")
    if missing_report_cases:
        print(f"  {missing_report_cases[:5]}...")
    
    print(f"\n按复杂度类型统计:")
    print("-" * 60)
    
    for complexity, stats in sorted(complexity_stats.items()):
        accuracy = stats['correct'] / stats['total'] * 100 if stats['total'] > 0 else 0
        print(f"  {complexity}: {stats['correct']}/{stats['total']} ({accuracy:.2f}%)")
    
    print(f"\n识别错误的案例 (前10个):")
    print("-" * 60)
    for i, case in enumerate(error_cases[:10]):
        print(f"  {case['folder']}: 实际={case['actual']}, 预测={case['predicted']}")
    
    # 保存详细结果到文件
    output_path = os.path.join(results_dir, 'accuracy_report.txt')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("复杂度识别准确率统计报告\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"总体统计:\n")
        f.write(f"  总测试用例数: {total_count}\n")
        f.write(f"  正确识别数: {correct_count}\n")
        f.write(f"  准确率: {correct_count/total_count*100:.2f}%\n\n")
        
        f.write("按复杂度类型统计:\n")
        f.write("-" * 60 + "\n")
        for complexity, stats in sorted(complexity_stats.items()):
            accuracy = stats['correct'] / stats['total'] * 100 if stats['total'] > 0 else 0
            f.write(f"  {complexity}: {stats['correct']}/{stats['total']} ({accuracy:.2f}%)\n")
        
        f.write(f"\n识别错误的案例:\n")
        f.write("-" * 60 + "\n")
        for case in error_cases:
            f.write(f"  {case['folder']}: 实际={case['actual']}, 预测={case['predicted']}\n")
    
    print(f"\n详细报告已保存到: {output_path}")

if __name__ == "__main__":
    main()
