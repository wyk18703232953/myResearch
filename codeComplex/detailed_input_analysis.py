#!/usr/bin/env python3
"""
按照具体输入类型重新分析和统计Python代码文件
"""

import os
import re
import ast
from collections import defaultdict, Counter
from pathlib import Path

def analyze_specific_input_types(file_path):
    """分析具体的输入类型"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception:
        return "读取错误"
    
    # 移除注释来更好地分析
    content_no_comments = re.sub(r'#.*$', '', content, flags=re.MULTILINE)
    
    # 查找所有input()相关的内容
    input_patterns = []
    
    # 查找input()调用
    input_calls = re.findall(r'input\(\s*\)', content_no_comments)
    
    # 查找map(int, input().split())模式
    map_int_patterns = re.findall(r'map\(\s*int\s*,\s*input\(\s*\)\.split\(\s*\)\s*\)', content_no_comments)
    
    # 查找tuple(map(int, input().split()))模式
    tuple_map_patterns = re.findall(r'tuple\(\s*map\(\s*int\s*,\s*input\(\s*\)\.split\(\s*\)\s*\)\s*\)', content_no_comments)
    
    # 查找字符串相关输入
    str_input_patterns = re.findall(r'input\(\s*\)', content_no_comments)
    
    # 查找list(map(int, input().split()))模式
    list_map_patterns = re.findall(r'list\(\s*map\(\s*int\s*,\s*input\(\s*\)\.split\(\s*\)\s*\)\s*\)', content_no_comments)
    
    # 分析前20行来推断输入结构
    lines = content_no_comments.split('\n')[:30]
    
    input_analysis = {
        'total_input_calls': len(input_calls),
        'map_int_calls': len(map_int_patterns),
        'tuple_map_calls': len(tuple_map_patterns),
        'list_map_calls': len(list_map_patterns),
        'has_n_length': False,
        'has_m_n': False,
        'has_m_n_k': False,
        'has_four_ints': False,
        'has_string_input': False,
        'multiple_int_params': False,
        'complex_structure': False
    }
    
    # 检查是否有关于n, N的变量定义
    for line in lines:
        if re.search(r'\b[nN]\s*=\s*\d+', line):
            input_analysis['has_n_length'] = True
        if re.search(r'\b[mM]\s*=\s*\d+', line):
            input_analysis['has_m_n'] = True
    
    # 检查是否有多参数输入模式
    for line in lines:
        # 检查是否有多个整数参数的输入
        if 'map(int, input().split())' in line:
            # 尝试确定参数个数
            if re.search(r'\b[aA]\s*,\s*[bB]\s*=|[mM]\s*,\s*[nN]\s*=|[xX]\s*,\s*[yY]\s*=', line):
                input_analysis['has_m_n'] = True
            elif re.search(r'\b[aA]\s*,\s*[bB]\s*,\s*[cC]\s*=|[xX]\s*,\s*[yY]\s*,\s*[zZ]\s*=', line):
                input_analysis['has_m_n_k'] = True
            elif re.search(r'\b[aA]\s*,\s*[bB]\s*,\s*[cC]\s*,\s*[dD]\s*=', line):
                input_analysis['has_four_ints'] = True
    
    # 检查是否只读取字符串（没有map(int, ...)）
    has_only_string_input = False
    for line in lines:
        if 'input()' in line and 'map(int' not in line and 'split()' not in line:
            has_only_string_input = True
    
    input_analysis['has_string_input'] = has_only_string_input
    
    # 根据分析结果分类
    if input_analysis['total_input_calls'] == 0:
        return "无输入"
    
    # 特殊情况：只有字符串输入
    if input_analysis['has_string_input'] and input_analysis['map_int_calls'] == 0:
        if input_analysis['total_input_calls'] == 1:
            return "单个字符串"
        elif input_analysis['total_input_calls'] == 2:
            return "2个字符串"
        else:
            return f"{input_analysis['total_input_calls']}个字符串"
    
    # 根据map(int, input().split())的调用次数和结构分类
    if input_analysis['map_int_calls'] >= 1:
        if input_analysis['has_n_length']:
            # 这种模式通常是：int n，然后 list<n> arr
            return "int:n + list<int> arr"
        elif input_analysis['has_m_n']:
            return "int m + int n"
        elif input_analysis['has_m_n_k']:
            return "int m + int n + int k"
        elif input_analysis['has_four_ints']:
            return "4个整数"
        elif input_analysis['map_int_calls'] == 1:
            # 单行多整数输入
            return "单行多个整数"
        elif input_analysis['map_int_calls'] == 2:
            return "2行整数输入"
        elif input_analysis['map_int_calls'] == 3:
            return "3行整数输入"
        else:
            return f"{input_analysis['map_int_calls']}行整数输入"
    
    # 其他情况：基本input()调用
    elif input_analysis['total_input_calls'] == 1:
        return "单个整数"
    elif input_analysis['total_input_calls'] == 2:
        return "2个整数"
    elif input_analysis['total_input_calls'] == 3:
        return "3个整数"
    elif input_analysis['total_input_calls'] == 4:
        return "4个整数"
    else:
        return f"{input_analysis['total_input_calls']}个整数"
    
    return "复杂输入结构"

def analyze_directory_detailed(directory_path):
    """详细分析目录下的Python文件"""
    python_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    print(f"找到 {len(python_files)} 个Python文件")
    
    # 按具体输入类型分类统计
    input_categories = Counter()
    pattern_analysis = defaultdict(list)
    
    for i, file_path in enumerate(python_files):
        if i % 1000 == 0:
            print(f"已处理 {i}/{len(python_files)} 个文件")
        
        input_type = analyze_specific_input_types(file_path)
        input_categories[input_type] += 1
        
        # 收集一些样本
        if len(pattern_analysis[input_type]) < 5:
            relative_path = os.path.relpath(file_path, directory_path)
            pattern_analysis[input_type].append(relative_path)
    
    return input_categories, pattern_analysis

def main():
    directory = "/home/wuyankai/myResearch/codeComplex/data/onlyCode/python"
    
    print("开始详细分析Python文件的具体输入类型...")
    categories, samples = analyze_directory_detailed(directory)
    
    print("\n" + "="*60)
    print("Python代码文件输入类型详细统计")
    print("="*60)
    print(f"总文件数: {sum(categories.values())}")
    print()
    
    # 按数量排序显示
    sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)
    
    print("输入类型分布（按数量排序）:")
    print("-" * 40)
    for input_type, count in sorted_categories:
        percentage = (count / sum(categories.values())) * 100
        print(f"{input_type:25} : {count:4d} ({percentage:5.2f}%)")
    
    print("\n" + "="*60)
    print("各类输入类型样本文件:")
    print("="*60)
    
    for input_type, count in sorted_categories[:15]:  # 显示前15种类型
        if count > 0:
            print(f"\n{input_type} ({count} 个文件):")
            if input_type in samples:
                for sample in samples[input_type]:
                    print(f"  - {sample}")
    
    # 保存详细结果
    with open('/home/wuyankai/myResearch/codeComplex/detailed_input_analysis.txt', 'w', encoding='utf-8') as f:
        f.write("Python代码文件输入类型详细分析结果\n")
        f.write("="*60 + "\n\n")
        f.write(f"总文件数: {sum(categories.values())}\n\n")
        
        f.write("输入类型分布（按数量排序）:\n")
        f.write("-" * 40 + "\n")
        for input_type, count in sorted_categories:
            percentage = (count / sum(categories.values())) * 100
            f.write(f"{input_type:25} : {count:4d} ({percentage:5.2f}%)\n")
        
        f.write("\n" + "="*60 + "\n")
        f.write("各类输入类型样本文件:\n")
        f.write("="*60 + "\n")
        
        for input_type, count in sorted_categories:
            if count > 0:
                f.write(f"\n{input_type} ({count} 个文件):\n")
                if input_type in samples:
                    for sample in samples[input_type]:
                        f.write(f"  - {sample}\n")
    
    print(f"\n详细分析结果已保存到: /home/wuyankai/myResearch/codeComplex/detailed_input_analysis.txt")

if __name__ == "__main__":
    main()