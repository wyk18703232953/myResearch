#!/usr/bin/env python3
"""
分析Python代码文件的输入类型分布
"""

import os
import re
import ast
from collections import defaultdict, Counter
from pathlib import Path

def extract_input_patterns(file_path):
    """提取文件中的输入模式"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        return []
    
    patterns = []
    
    # 查找所有input()调用
    input_patterns = re.findall(r'input\(\s*\)', content)
    
    # 查找input().split()模式
    input_split_patterns = re.findall(r'input\(\s*\)\.split\(\s*\)', content)
    
    # 查找map(int, input().split())模式
    map_int_patterns = re.findall(r'map\(\s*int\s*,\s*input\(\s*\)\.split\(\s*\)\s*\)', content)
    
    # 查找tuple(map(int, input().split()))模式
    tuple_map_patterns = re.findall(r'tuple\(\s*map\(\s*int\s*,\s*input\(\s*\)\.split\(\s*\)\s*\)\s*\)', content)
    
    # 查找其他变体
    # list(map(int, input().split()))
    list_map_patterns = re.findall(r'list\(\s*map\(\s*int\s*,\s*input\(\s*\)\.split\(\s*\)\s*\)\s*\)', content)
    
    return {
        'input_basic': len(input_patterns),
        'input_split': len(input_split_patterns),
        'map_int': len(map_int_patterns),
        'tuple_map': len(tuple_map_patterns),
        'list_map': len(list_map_patterns)
    }

def analyze_input_structure(file_path):
    """分析输入结构，尝试识别具体的输入类型"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception:
        return "unknown"
    
    # 查找前50行中的输入相关代码
    relevant_lines = []
    for i, line in enumerate(lines[:50]):
        if 'input(' in line or 'map(int' in line or '.split()' in line:
            relevant_lines.append((i+1, line.strip()))
    
    if not relevant_lines:
        return "no_input"
    
    # 分析输入模式
    input_calls = []
    map_int_calls = []
    
    for line_num, line in relevant_lines:
        # 基本input()调用
        if re.search(r'input\(\s*\)', line):
            # 检查是否是直接读取简单值
            if 'split()' not in line and 'map(' not in line:
                input_calls.append(f"line_{line_num}: simple_input")
        
        # map(int, input().split()) 调用
        if re.search(r'map\(\s*int\s*,\s*input\(\s*\)\.split\(\s*\)\s*\)', line):
            map_int_calls.append(line_num)
    
    # 根据发现的模式分类
    if not input_calls and not map_int_calls:
        # 检查其他可能的输入模式
        for line_num, line in relevant_lines:
            if '.split()' in line and 'input()' in line:
                input_calls.append(f"line_{line_num}: split_input")
    
    # 尝试推断具体的输入类型
    if map_int_calls:
        # 统计map(int, input().split())的调用次数
        count = len(map_int_calls)
        
        # 尝试从代码上下文推断输入类型
        for line_num, line in relevant_lines:
            line_lower = line.lower()
            
            # 检查是否有关于数组长度或数量的信息
            if 'n =' in line or 'N =' in line or 'len(' in line:
                return f"int_n_list_{count}_inputs"
            
            # 检查是否有多个变量的读取
            if 'map(int, input().split())' in line:
                # 尝试确定参数个数
                if 'a, b' in line or 'm, n' in line or 'x, y' in line:
                    return f"int_2_params"
                elif 'a, b, c' in line or 'x, y, z' in line:
                    return f"int_3_params"
                else:
                    return f"int_multiple_params"
        
        return f"int_list_{count}_inputs"
    
    elif input_calls:
        simple_count = len([call for call in input_calls if 'simple' in call])
        split_count = len([call for call in input_calls if 'split' in call])
        
        if simple_count > 0 and split_count == 0:
            return f"simple_input_{simple_count}_times"
        elif split_count > 0:
            return f"split_input_{split_count}_times"
        else:
            return f"mixed_input_{len(input_calls)}_times"
    
    return "complex_input"

def classify_input_type(file_path):
    """分类输入类型"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception:
        return "error_reading"
    
    # 统计各种输入模式
    patterns = extract_input_patterns(file_path)
    
    # 查找变量定义来推断输入结构
    var_patterns = re.findall(r'(\w+)\s*=\s*(?:int\(|map\(int|,|\s*)(?:input\(\)|input\(\)\.split\(\))', content, re.IGNORECASE)
    
    # 分析输入结构
    input_structure = analyze_input_structure(file_path)
    
    # 基于发现的内容进行分类
    if patterns['map_int'] > 0:
        if patterns['map_int'] == 1:
            # 单个map(int, input().split())调用
            # 检查是否有关于数组长度的信息
            if re.search(r'\bN\b.*=.*\d+|\bn\b.*=.*\d+|\bsize\b.*=.*\d+', content, re.IGNORECASE):
                return "int_n_list_arr"
            else:
                return "int_single_line"
        elif patterns['map_int'] == 2:
            return "int_2_lines"
        elif patterns['map_int'] == 3:
            return "int_3_lines"
        else:
            return f"int_{patterns['map_int']}_lines"
    
    elif patterns['input_basic'] > 0:
        if patterns['input_basic'] == 1:
            return "single_input"
        elif patterns['input_basic'] == 2:
            return "two_inputs"
        elif patterns['input_basic'] == 3:
            return "three_inputs"
        else:
            return f"{patterns['input_basic']}_inputs"
    
    elif patterns['input_split'] > 0:
        return f"split_input_{patterns['input_split']}_times"
    
    elif input_structure != "no_input":
        return input_structure
    
    else:
        return "no_detectable_input"

def analyze_directory(directory_path):
    """分析整个目录下的Python文件"""
    python_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    print(f"找到 {len(python_files)} 个Python文件")
    
    # 分类统计
    categories = Counter()
    detailed_results = []
    
    for i, file_path in enumerate(python_files):
        if i % 1000 == 0:
            print(f"已处理 {i}/{len(python_files)} 个文件")
        
        input_type = classify_input_type(file_path)
        categories[input_type] += 1
        
        # 记录详细信息（只记录前100个作为样本）
        if len(detailed_results) < 100:
            relative_path = os.path.relpath(file_path, directory_path)
            detailed_results.append({
                'file': relative_path,
                'input_type': input_type,
                'patterns': extract_input_patterns(file_path)
            })
    
    return categories, detailed_results

def main():
    directory = "/home/wuyankai/myResearch/codeComplex/data/onlyCode/python"
    
    print("开始分析Python文件的输入类型分布...")
    categories, detailed_results = analyze_directory(directory)
    
    print("\n=== 输入类型分布统计 ===")
    print(f"总文件数: {sum(categories.values())}")
    print("\n各类输入类型及其数量:")
    
    # 按数量排序显示
    sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)
    
    for input_type, count in sorted_categories:
        percentage = (count / sum(categories.values())) * 100
        print(f"  {input_type}: {count} ({percentage:.2f}%)")
    
    print("\n=== 详细样本分析（前20个） ===")
    for result in detailed_results[:20]:
        print(f"文件: {result['file']}")
        print(f"  输入类型: {result['input_type']}")
        print(f"  模式统计: {result['patterns']}")
        print()
    
    # 保存结果到文件
    with open('/home/wuyankai/myResearch/codeComplex/input_analysis_results.txt', 'w', encoding='utf-8') as f:
        f.write("Python文件输入类型分布分析结果\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"总文件数: {sum(categories.values())}\n\n")
        
        f.write("各类输入类型及其数量:\n")
        for input_type, count in sorted_categories:
            percentage = (count / sum(categories.values())) * 100
            f.write(f"  {input_type}: {count} ({percentage:.2f}%)\n")
        
        f.write(f"\n详细样本分析:\n")
        for result in detailed_results:
            f.write(f"文件: {result['file']}\n")
            f.write(f"  输入类型: {result['input_type']}\n")
            f.write(f"  模式统计: {result['patterns']}\n\n")
    
    print(f"\n分析结果已保存到: /home/wuyankai/myResearch/codeComplex/input_analysis_results.txt")

if __name__ == "__main__":
    main()