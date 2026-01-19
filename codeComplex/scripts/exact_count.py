#!/usr/bin/env python3
"""
精确统计y_llm和y_fit都等于expected_complexity的记录数
"""

import json

report_path = "/home/wuyankai/myResearch/codeComplex/results/fusion_llm_report_universal_v14.json"

try:
    with open(report_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    detailed_records = data.get('detailed_records', [])
    total_records = len(detailed_records)
    
    # 精确统计用户要求的情况：y_llm和y_fit都等于expected_complexity
    count = 0
    
    for i, record in enumerate(detailed_records):
        expected = record.get('expected_complexity')
        y_llm = record.get('y_llm')
        y_fit = record.get('y_fit')
        
        # 只检查这三个字段是否都相等
        if y_llm == expected or y_fit == expected:
            count += 1
    
    print(f"精确统计结果：")
    print(f"总记录数 (detailed_records长度): {total_records}")
    print(f"满足条件的记录数 (y_llm == expected_complexity AND y_fit == expected_complexity): {count}")
    print(f"比例: {count/total_records*100:.2f}%")
    
    # 再检查前10条记录进行验证
    print("\n前10条记录验证：")
    for i, record in enumerate(detailed_records[:10]):
        expected = record.get('expected_complexity')
        y_llm = record.get('y_llm')
        y_fit = record.get('y_fit')
        matches = y_llm == expected and y_fit == expected
        print(f"记录 #{i+1}: expected={expected}, y_llm={y_llm}, y_fit={y_fit}, 符合条件={matches}")
        
except Exception as e:
    print(f"错误: {str(e)}")
