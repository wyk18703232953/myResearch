#!/usr/bin/env python3
"""
统计各复杂度类型的分析正确率
"""

import os
import json
from collections import defaultdict

# 定义期望的复杂度映射（基于文件夹名称）
expected_complexity_map = {
    'constant': 'O(1)',
    'linear': 'O(n)',
    'logn': 'O(log n)',
    'nlogn': 'O(n log n)',
    'quadratic': 'O(n^2)',
    'cubic': 'O(n^3)',
    'np': 'O(n^p)'
}

# 复杂度名称映射（从报告到标准名称）
complexity_name_map = {
    'O(1)': 'O(1)',
    'O(n)': 'O(n)',
    'O(log n)': 'O(log n)',
    'O(n log n)': 'O(n log n)',
    'O(n^2)': 'O(n^2)',
    'O(n^3)': 'O(n^3)',
    'O(2^n)': 'O(2^n)',
    'O(n^p)': 'O(n^p)'
}

def extract_expected_complexity(folder_name):
    """从文件夹名称提取期望的复杂度"""
    # results_python_linear_0001 -> linear
    parts = folder_name.split('_')
    # 找到 'python' 和期望复杂度之间的索引
    for i, part in enumerate(parts):
        if part == 'python' and i + 1 < len(parts):
            complexity = parts[i + 1]
            if complexity in expected_complexity_map:
                return complexity
    return None

def normalize_complexity(model_name):
    """标准化复杂度名称"""
    return complexity_name_map.get(model_name, model_name)

def analyze_results(base_path):
    """分析所有结果文件夹"""
    results = defaultdict(lambda: {
        'total': 0,
        'correct': 0,
        'details': []
    })
    
    # 遍历所有复杂度类型目录
    for complexity_type in expected_complexity_map.keys():
        complexity_path = os.path.join(base_path, complexity_type)
        if not os.path.exists(complexity_path) or not os.path.isdir(complexity_path):
            continue
        
        expected_model = expected_complexity_map[complexity_type]
        print(f"\n处理 {complexity_type} (期望: {expected_model})...")
        
        # 遍历该类型下的结果文件夹
        for item in os.listdir(complexity_path):
            item_path = os.path.join(complexity_path, item)
            if not os.path.isdir(item_path):
                continue
            
            # 读取报告
            report_path = os.path.join(item_path, 'report.json')
            if not os.path.exists(report_path):
                continue
            
            try:
                with open(report_path, 'r', encoding='utf-8') as f:
                    report = json.load(f)
                
                best_model = normalize_complexity(report.get('best_model', ''))
                
                results[complexity_type]['total'] += 1
                
                is_correct = (best_model == expected_model)
                if is_correct:
                    results[complexity_type]['correct'] += 1
                
                if len(results[complexity_type]['details']) < 5:  # 只记录前5个详情
                    results[complexity_type]['details'].append({
                        'folder': item,
                        'expected': expected_model,
                        'predicted': best_model,
                        'correct': is_correct
                    })
                
            except Exception as e:
                print(f"  警告：无法读取 {item_path}: {e}")
                continue
    
    return results

def print_statistics(results):
    """打印统计结果"""
    print("\n" + "="*80)
    print("各复杂度类型分析正确率统计")
    print("="*80)
    
    total_correct = 0
    total_files = 0
    
    for complexity_type in ['constant', 'linear', 'logn', 'nlogn', 'quadratic', 'cubic', 'np']:
        if complexity_type not in results:
            continue
            
        data = results[complexity_type]
        total = data['total']
        correct = data['correct']
        total_files += total
        total_correct += correct
        
        accuracy = (correct / total * 100) if total > 0 else 0
        
        expected = expected_complexity_map[complexity_type]
        print(f"\n{complexity_type:12s} (期望: {expected:10s}): {correct:4d}/{total:4d} 正确")
        print(f"           正确率: {accuracy:6.2f}%")
    
    overall_accuracy = (total_correct / total_files * 100) if total_files > 0 else 0
    
    print("\n" + "="*80)
    print(f"总体统计: {total_correct:4d}/{total_files:4d} 正确")
    print(f"总体正确率: {overall_accuracy:.2f}%")
    print("="*80)
    
    # 打印错误分析
    print("\n常见误分类:")
    misclassifications = defaultdict(int)
    for complexity_type, data in results.items():
        for detail in data['details']:
            if not detail['correct']:
                key = f"{detail['expected']} -> {detail['predicted']}"
                misclassifications[key] += 1
    
    for misclass, count in sorted(misclassifications.items(), key=lambda x: -x[1])[:10]:
        print(f"  {misclass}: {count} 次")

if __name__ == "__main__":
    base_path = "/home/wuyankai/myResearch/codeComplex/demo/filteredData/python"
    
    print("开始分析结果...")
    results = analyze_results(base_path)
    print_statistics(results)
