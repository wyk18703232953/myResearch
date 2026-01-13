import json
import os

def calculate_accuracy(json_file_path, exclude_types=None):
    """
    计算LLM复杂度预测的准确率
    
    参数:
    json_file_path: JSON结果文件的路径
    exclude_types: 要排除的复杂度类型列表
    
    返回:
    accuracy: 准确率 (百分比)
    total_records: 总记录数
    correct_records: 正确记录数
    """
    if not os.path.exists(json_file_path):
        print(f"文件不存在: {json_file_path}")
        return 0.0, 0, 0
    
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    detailed_records = data.get('detailed_records', [])
    
    total_records = 0
    correct_records = 0
    
    for record in detailed_records:
        expected = record.get('expected_complexity', '').strip().lower()
        
        # 检查是否需要排除当前类型
        if exclude_types and expected in exclude_types:
            continue
        
        total_records += 1
        is_match = record.get('is_match', False)
        
        if is_match:
            correct_records += 1
    
    if total_records == 0:
        print("没有符合条件的记录")
        return 0.0, 0, 0
    
    accuracy = (correct_records / total_records) * 100
    
    return accuracy, total_records, correct_records

if __name__ == "__main__":
    # 设置JSON文件路径
    json_file = "/home/wuyankai/myResearch/codeComplex/results/LLM/ast_llm_results1_demo_filtered.json"
    
    # 计算整体准确率
    accuracy_all, total_all, correct_all = calculate_accuracy(json_file)
    print("=== 整体准确率 ===")
    print(f"总记录数: {total_all}")
    print(f"正确记录数: {correct_all}")
    print(f"准确率: {accuracy_all:.2f}%")
    print()
    
    # 计算排除np和constant类型后的准确率
    exclude_types = ['np', 'constant']
    accuracy_filtered, total_filtered, correct_filtered = calculate_accuracy(json_file, exclude_types)
    print("=== 排除 np 和 constant 类型后的准确率 ===")
    print(f"总记录数: {total_filtered}")
    print(f"正确记录数: {correct_filtered}")
    print(f"准确率: {accuracy_filtered:.2f}%")
    print()
    
    # 可以根据需要添加更多类型的统计
    print("=== 各类型统计 ===")
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    detailed_records = data.get('detailed_records', [])
    
    type_stats = {}
    
    for record in detailed_records:
        expected = record.get('expected_complexity', '').strip().lower()
        is_match = record.get('is_match', False)
        
        if expected not in type_stats:
            type_stats[expected] = {'total': 0, 'correct': 0}
        
        type_stats[expected]['total'] += 1
        if is_match:
            type_stats[expected]['correct'] += 1
    
    # 按总记录数降序排序
    sorted_types = sorted(type_stats.items(), key=lambda x: x[1]['total'], reverse=True)
    
    for complexity_type, stats in sorted_types:
        total = stats['total']
        correct = stats['correct']
        accuracy = (correct / total) * 100 if total > 0 else 0
        print(f"{complexity_type:<15} 总: {total:5d} 正确: {correct:5d} 准确率: {accuracy:6.2f}%")
