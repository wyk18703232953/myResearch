#!/usr/bin/env python3
"""
按照输入类型重新组织Python文件
"""

import os
import shutil
import re
from collections import defaultdict, Counter
from pathlib import Path

def analyze_specific_input_types(file_path):
    """分析具体的输入类型（修复版 - 支持多种输入方式）"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception:
        return "读取错误"
    
    # 移除注释来更好地分析
    content_no_comments = re.sub(r'#.*$', '', content, flags=re.MULTILINE)
    
    # 初始化分析结果字典
    input_analysis = {
        'total_input_calls': 0,
        'input_calls': 0,
        'sys_stdin_readline_calls': 0,
        'sys_stdin_read_calls': 0,
        'sys_stdin_buffer_read_calls': 0,
        'sys_stdin_readlines_calls': 0,
        'stdin_readlines_calls': 0,
        'stdin_read_calls': 0,
        'sys_argv_usage': False,
        'stdin_assignments': 0,
        'input_reassignment': 0,
        'map_int_calls': 0,
        'tuple_map_calls': 0,
        'list_map_calls': 0,
        'has_n_length': False,
        'has_m_n': False,
        'has_m_n_k': False,
        'has_four_ints': False,
        'has_string_input': False,
        'has_stdin_input': False,
        'multiple_int_params': False,
        'complex_structure': False
    }
    
    # 检测所有可能的输入方式
    input_sources = []
    lambda_names = []  # 定义lambda_names变量
    lambda_calls = {}  # 存储lambda函数名称及其调用次数
    
    # 特殊标记：防止重复计算输入
    counted_input_patterns = set()
    
    # 1. 查找带类型转换的input()调用
    # int(input())
    int_input_calls = re.findall(r'int\(\s*input\(\s*\)\s*\)', content_no_comments)
    input_sources.extend([('int(input())', call) for call in int_input_calls])
    
    # float(input())
    float_input_calls = re.findall(r'float\(\s*input\(\s*\)\s*\)', content_no_comments)
    input_sources.extend([('float(input())', call) for call in float_input_calls])
    
    # str(input())
    str_input_calls = re.findall(r'str\(\s*input\(\s*\)\s*\)', content_no_comments)
    input_sources.extend([('str(input())', call) for call in str_input_calls])
    
    # 2. 查找input()调用（包括带参数的）
    # 无参数：input()
    input_calls = re.findall(r'input\(\s*\)', content_no_comments)
    input_sources.extend([('input()', call) for call in input_calls])
    
    # 带参数：input(""), input("请输入..."), input()等
    input_with_args = re.findall(r'input\(\s*["\'].*["\']\s*\)', content_no_comments)
    input_sources.extend([('input("")', call) for call in input_with_args])
    
    # 2. 查找sys.stdin.readline()调用（包括带类型转换的）
    # 直接调用
    sys_stdin_readline = re.findall(r'sys\.stdin\.readline\(\s*\)', content_no_comments)
    input_sources.extend([('sys.stdin.readline()', call) for call in sys_stdin_readline])
    
    # 带类型转换的调用：int(sys.stdin.readline()), float(sys.stdin.readline())等
    typed_sys_stdin_readline = re.findall(r'(int|float|str)\(\s*sys\.stdin\.readline\(\s*\)\s*\)', content_no_comments)
    for match in typed_sys_stdin_readline:
        input_sources.extend([(f'{match}(sys.stdin.readline())', f'{match}(sys.stdin.readline())')])
    
    # 3. 查找stdin.readline()调用（包括带类型转换的）
    # 直接调用
    stdin_readline = re.findall(r'stdin\.readline\(\s*\)', content_no_comments)
    input_sources.extend([('stdin.readline()', call) for call in stdin_readline])
    
    # 带类型转换的调用：int(stdin.readline()), float(stdin.readline())等
    typed_stdin_readline = re.findall(r'(int|float|str)\(\s*stdin\.readline\(\s*\)\s*\)', content_no_comments)
    for match in typed_stdin_readline:
        input_sources.extend([(f'{match}(stdin.readline())', f'{match}(stdin.readline())')])
    
    # 4. 查找sys.stdin.read()调用
    sys_stdin_read = re.findall(r'sys\.stdin\.read\(\s*\)', content_no_comments)
    input_sources.extend([('sys.stdin.read()', call) for call in sys_stdin_read])
    
    # 4. 查找sys.stdin.buffer.read()调用
    sys_stdin_buffer_read = re.findall(r'sys\.stdin\.buffer\.read\(\s*\)', content_no_comments)
    input_sources.extend([('sys.stdin.buffer.read()', call) for call in sys_stdin_buffer_read])
    
    # 4.1. 查找sys.stdin.buffer.readline()调用（包括带类型转换的）
    # 直接调用
    sys_stdin_buffer_readline = re.findall(r'sys\.stdin\.buffer\.readline\(\s*\)', content_no_comments)
    input_sources.extend([('sys.stdin.buffer.readline()', call) for call in sys_stdin_buffer_readline])
    
    # 带类型转换的调用：int(sys.stdin.buffer.readline()), float(sys.stdin.buffer.readline())等
    typed_sys_stdin_buffer_readline = re.findall(r'(int|float|str)\(\s*sys\.stdin\.buffer\.readline\(\s*\)\s*\)', content_no_comments)
    for match in typed_sys_stdin_buffer_readline:
        input_sources.extend([(f'{match}(sys.stdin.buffer.readline())', f'{match}(sys.stdin.buffer.readline())')])
    
    # 查找在函数定义中使用了stdin相关操作的情况
    # 检测包含stdin.buffer.readline的函数定义
    function_stdin_buffer_defs = re.findall(r'def\s+\w+\([^)]*\):\s*.*?sys\.stdin\.buffer\.readline\(\s*\)', content_no_comments, re.DOTALL)
    for func_def in function_stdin_buffer_defs:
        input_sources.append(('function_with_stdin_buffer_readline()', func_def))
    
    # 检测包含stdin.readline的函数定义
    function_stdin_defs = re.findall(r'def\s+\w+\([^)]*\):\s*.*?stdin\.readline\(\s*\)', content_no_comments, re.DOTALL)
    for func_def in function_stdin_defs:
        input_sources.append(('function_with_stdin_readline()', func_def))
    
    # 8. 检测next()函数调用（通常是stdin的迭代器）
    # 查找类似 cin = sys.stdin; next(cin) 的模式
    # 首先查找将stdin赋值给其他变量的模式
    stdin_assignments = re.findall(r'(\w+)\s*=\s*sys\.stdin', content_no_comments)
    stdin_assignments.extend(re.findall(r'(\w+)\s*=\s*stdin', content_no_comments))
    
    # 对于每个可能的stdin变量，查找next()调用
    for var_name in stdin_assignments:
        next_calls = re.findall(rf'next\(\s*{re.escape(var_name)}\s*\)', content_no_comments)
        input_sources.extend([(f'next({var_name})', call) for call in next_calls])
    
    # 查找直接的next()调用（可能是迭代器模式）
    direct_next_calls = re.findall(r'next\(\s*(\w+)\s*\)', content_no_comments)
    for var_name in direct_next_calls:
        # 检查这个变量是否可能是stdin相关的
        if var_name in ['cin', 'f', 'file', 'stream', 'reader']:
            input_sources.append((f'next({var_name})', f'next({var_name})'))
    
    # 特别检测 next(sys.stdin) 这种直接模式
    next_sys_stdin_calls = re.findall(r'next\(\s*sys\.stdin\s*\)', content_no_comments)
    input_sources.extend([('next(sys.stdin)', call) for call in next_sys_stdin_calls])
    
    # 检测 next(stdin) 这种模式（如果已经导入了stdin）
    next_stdin_calls = re.findall(r'next\(\s*stdin\s*\)', content_no_comments)
    input_sources.extend([('next(stdin)', call) for call in next_stdin_calls])
    
    # 检测 next(sys.stdin.readline()) 这种模式
    next_sys_stdin_readline_calls = re.findall(r'next\(\s*sys\.stdin\.readline\(\s*\)\s*\)', content_no_comments)
    input_sources.extend([('next(sys.stdin.readline())', call) for call in next_sys_stdin_readline_calls])
    
    # 检测包含sys.stdin.readline的函数定义
    function_sys_stdin_defs = re.findall(r'def\s+\w+\([^)]*\):\s*.*?sys\.stdin\.readline\(\s*\)', content_no_comments, re.DOTALL)
    for func_def in function_sys_stdin_defs:
        input_sources.append(('function_with_sys_stdin_readline()', func_def))
    
    # 检测包含stdin.buffer.read的函数定义
    function_stdin_buffer_read_defs = re.findall(r'def\s+\w+\([^)]*\):\s*.*?sys\.stdin\.buffer\.read\(\s*\)', content_no_comments, re.DOTALL)
    for func_def in function_stdin_buffer_read_defs:
        input_sources.append(('function_with_stdin_buffer_read()', func_def))
    
    # 检测包含stdin.read的函数定义
    function_stdin_read_defs = re.findall(r'def\s+\w+\([^)]*\):\s*.*?stdin\.read\(\s*\)', content_no_comments, re.DOTALL)
    for func_def in function_stdin_read_defs:
        input_sources.append(('function_with_stdin_read()', func_def))
    
    # 检测包含sys.stdin.read的函数定义
    function_sys_stdin_read_defs = re.findall(r'def\s+\w+\([^)]*\):\s*.*?sys\.stdin\.read\(\s*\)', content_no_comments, re.DOTALL)
    for func_def in function_sys_stdin_read_defs:
        input_sources.append(('function_with_sys_stdin_read()', func_def))
    
    # 检测lambda函数中的stdin操作
    # 检测包含stdin.buffer.readline的lambda函数
    lambda_stdin_buffer_defs = re.findall(r'\w+\s*=\s*lambda\s+[^:]*:\s*.*?sys\.stdin\.buffer\.readline\(\s*\)', content_no_comments, re.DOTALL)
    for func_def in lambda_stdin_buffer_defs:
        input_sources.append(('lambda_with_stdin_buffer_readline()', func_def))
    
    # 检测包含stdin.readline的lambda函数
    lambda_stdin_defs = re.findall(r'\w+\s*=\s*lambda\s+[^:]*:\s*.*?stdin\.readline\(\s*\)', content_no_comments, re.DOTALL)
    for func_def in lambda_stdin_defs:
        input_sources.append(('lambda_with_stdin_readline()', func_def))
    
    # 5. 查找sys.stdin.readlines()调用
    sys_stdin_readlines = re.findall(r'sys\.stdin\.readlines\(\s*\)', content_no_comments)
    input_sources.extend([('sys.stdin.readlines()', call) for call in sys_stdin_readlines])
    
    # 6. 查找stdin.readlines()调用（已导入stdin）
    stdin_readlines = re.findall(r'stdin\.readlines\(\s*\)', content_no_comments)
    input_sources.extend([('stdin.readlines()', call) for call in stdin_readlines])
    
    # 7. 查找stdin.read()调用（已导入stdin）
    stdin_read = re.findall(r'stdin\.read\(\s*\)', content_no_comments)
    input_sources.extend([('stdin.read()', call) for call in stdin_read])
    
    # 7.1. 检测自定义输入函数
    # 首先检测可能的自定义输入函数定义，例如: def ReadNext(fileObject):
    # 使用更宽松的模式来捕获类似ReadNext(r)的函数定义
    # 查找可能带"read"、"get"等关键词的函数定义
    read_func_defs = re.findall(r'def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\([^)]*\):', content_no_comments)
    # 从这些函数中筛选出可能用于读取的函数
    potential_read_funcs = []
    for func_name in read_func_defs:
        # 查找函数体内的内容
        func_pattern = rf'def\s+{re.escape(func_name)}\s*\([^)]*\):\s*(.*?)(?=\ndef|\Z)'
        func_body = re.search(func_pattern, content_no_comments, re.DOTALL)
        if func_body and func_body.group(1):
            # 检查函数体是否包含读取操作
            if re.search(r'\.read\(|\.readline\(|\.readlines\(', func_body.group(1)):
                potential_read_funcs.append(func_name)
    
    # 对可能的读取函数进行调用检测
    for func_name in potential_read_funcs:
        # 检测直接调用
        func_calls = re.findall(rf'{re.escape(func_name)}\([^)]*\)', content_no_comments)
        for call in func_calls:
            input_sources.append((f'{func_name}()', call))
        
        # 检测带类型转换的调用，例如: int(ReadNext(r))
        typed_calls = re.findall(rf'(int|float|str)\(\s*{re.escape(func_name)}\([^)]*\)\s*\)', content_no_comments)
        for match in typed_calls:
            input_sources.append((f'{match}({func_name}())', f'{match}({func_name}())'))
    
    # 7.2. 直接检测可能的ReadNext函数模式
    # 查找类似 ReadNext(r) 的调用
    readnext_calls = re.findall(r'ReadNext\([^)]+\)', content_no_comments)
    input_sources.extend([('ReadNext()', call) for call in readnext_calls])
    
    # 查找类似 int(ReadNext(r)) 的调用
    typed_readnext_calls = re.findall(r'(int|float|str)\(\s*ReadNext\([^)]+\)\s*\)', content_no_comments)
    for match in typed_readnext_calls:
        input_sources.append((f'{match}(ReadNext())', f'{match}(ReadNext())'))
    
    # 8. 查找sys.argv使用（命令行参数）
    sys_argv_patterns = re.findall(r'sys\.argv', content_no_comments)
    
    # 8. 查找其他可能的输入模式
    # 检查是否有stdin相关的赋值
    stdin_assignments = re.findall(r'(\w+)\s*=\s*sys\.stdin\.readline', content_no_comments)
    stdin_assignments.extend(re.findall(r'(\w+)\s*=\s*sys\.stdin\.read', content_no_comments))
    stdin_assignments.extend(re.findall(r'(\w+)\s*=\s*sys\.stdin\.readlines', content_no_comments))
    stdin_assignments.extend(re.findall(r'(\w+)\s*=\s*stdin\.readlines', content_no_comments))
    stdin_assignments.extend(re.findall(r'(\w+)\s*=\s*stdin\.read', content_no_comments))
    
    # 特别检测input=sys.stdin.readline这种模式
    # 需要特别处理，因为input被重赋值后，之前的input()调用检测会失效
    input_reassignment = re.findall(r'(\w+)\s*=\s*sys\.stdin\.readline', content_no_comments)
    # 检查是否有重命名stdin.readline的情况，如 input=stdin.readline
    input_reassignment.extend(re.findall(r'(\w+)\s*=\s*stdin\.readline', content_no_comments))
    # 检查是否有重命名其他输入函数的情况
    input_reassignment.extend(re.findall(r'(\w+)\s*=\s*input\s*\(', content_no_comments))
    # 特别处理 f=input 这种简单赋值模式
    input_reassignment.extend(re.findall(r'(\w+)\s*=\s*input\s*$', content_no_comments, re.MULTILINE))
    
    # 特别处理 input_file = sys.stdin 这种模式
    input_reassignment.extend(re.findall(r'(\w+)\s*=\s*sys\.stdin\s*$', content_no_comments, re.MULTILINE))
    # 确保将stdin_assignments中的值也加入input_reassignment
    input_reassignment.extend(stdin_assignments)
    input_reassignment.extend(re.findall(r'(\w+)\s*=\s*sys\.stdin\.readlines', content_no_comments))
    input_reassignment.extend(re.findall(r'(\w+)\s*=\s*stdin\.readlines', content_no_comments))
    # 特别处理 readline = sys.stdin.buffer.readline 这种模式
    input_reassignment.extend(re.findall(r'(\w+)\s*=\s*sys\.stdin\.buffer\.readline', content_no_comments))
    # 检查其他可能的buffer.readline重赋值模式
    input_reassignment.extend(re.findall(r'(\w+)\s*=\s*\.buffer\.readline', content_no_comments))
    
    # 对于input=sys.stdin.readline这种情况，需要特别处理
    # 因为后续使用input()实际上是使用sys.stdin.readline()
    input_as_stdin_readline = re.findall(r'(\w+)\s*=\s*sys\.stdin\.readline', content_no_comments)
    # 如果变量名为input，则需要特殊处理
    if 'input' in input_as_stdin_readline:
        # 计算代码中input()的调用次数
        input_calls_in_code = re.findall(r'input\(\s*\)', content_no_comments)
        # 将这些调用视为sys.stdin.readline()的调用
        for call in input_calls_in_code:
            input_sources.append(('sys.stdin.readline()', call))
        
        # 检查是否有类型转换的input()调用
        typed_input_calls = re.findall(r'(int|float|str)\(\s*input\(\s*\)\s*\)', content_no_comments)
        for match in typed_input_calls:
            input_sources.append((f'{match}(sys.stdin.readline())', f'{match}(sys.stdin.readline())'))
    
    # 7. 检测通过函数调用的stdin使用（如lambda函数）
    # 查找lambda或其他函数定义中使用了stdin相关变量
    lambda_stdin_usage = re.findall(r'(?:lambda|def)\s+\w+\s*:\s*\w+\(\)', content_no_comments)
    # 如果lambda函数调用的变量名在stdin_assignments中出现过
    for lambda_func in lambda_stdin_usage:
        for assigned_var in stdin_assignments:
            if assigned_var in lambda_func:
                input_sources.extend([('lambda_stdin_call', lambda_func)])
    
    # 7.1. 检测lambda函数中的stdin调用（包括带类型转换的）
    # 检测int(stdin.readline())等类型转换模式
    lambda_typed_stdin = re.findall(r'lambda\s*:\s*(int|float|str)\(\s*stdin\.readline\(\s*\)\s*\)', content_no_comments)
    for match in lambda_typed_stdin:
        input_sources.extend([(f'lambda: {match}(stdin.readline())', f'lambda: {match}(stdin.readline())')])
    
    # 检测stdin.readline()直接调用
    lambda_stdin = re.findall(r'lambda\s*:\s*stdin\.readline\(\s*\)', content_no_comments)
    input_sources.extend([('lambda: stdin.readline()', call) for call in lambda_stdin])
    
    # 检测lambda函数中调用了stdin.readlines()
    lambda_stdin_readlines = re.findall(r'lambda\s*:\s*stdin\.readlines\(\s*\)', content_no_comments)
    input_sources.extend([('lambda: stdin.readlines()', call) for call in lambda_stdin_readlines])
    
    # 检测lambda函数中调用了stdin.read()
    lambda_stdin_read = re.findall(r'lambda\s*:\s*stdin\.read\(\s*\)', content_no_comments)
    input_sources.extend([('lambda: stdin.read()', call) for call in lambda_stdin_read])
    
    # 检测lambda函数中的map(int, stdin.readline().split())模式
    lambda_map_int_stdin = re.findall(r'lambda\s*:\s*list\(\s*map\(\s*int\s*,\s*stdin\.readline\(\s*\)\.split\(\s*\)\s*\)\s*\)', content_no_comments)
    input_sources.extend([('lambda: list(map(int, stdin.readline().split()))', call) for call in lambda_map_int_stdin])
    
    # 检测直接定义的lambda函数
    lambda_defs = re.findall(r'(\w+)\s*=\s*lambda\s*:', content_no_comments)
    for name in lambda_defs:
        if name not in lambda_names:
            lambda_names.append(name)
            lambda_calls[name] = 0  # 初始化计数
    
    # 检查lambda函数是否被调用
    for name in lambda_names:
        # 查找name()的调用
        calls = re.findall(rf'{re.escape(name)}\(\)', content_no_comments)
        lambda_calls[name] = len(calls)
    
    # 8. 查找其他可能的函数调用模式
    # 检查是否有直接调用通过stdin赋值的变量
    for assigned_var in stdin_assignments:
        # 查找assigned_var()的调用
        calls = re.findall(rf'{re.escape(assigned_var)}\(\)', content_no_comments)
        input_sources.extend([(f'{assigned_var}()', call) for call in calls])
    
    # 特别处理input重赋值的情况，例如 input=sys.stdin.readline
    # 需要单独统计这种重赋值后的函数调用次数
    # 因为这些调用可能不会被input()检测到
    reassignment_calls = {}
    for var_name in input_reassignment:
        # 计算该变量被调用的次数
        calls = re.findall(rf'{re.escape(var_name)}\(\)', content_no_comments)
        reassignment_calls[var_name] = len(calls)
        input_sources.extend([(f'{var_name}()', f'{var_name}()') for _ in calls])
        
        # 对于input重赋值的情况，检查是否有类型转换
        # 例如: a = int(input()) 
        typed_calls = re.findall(rf'(int|float|str)\(\s*{re.escape(var_name)}\(\)\s*\)', content_no_comments)
        for typed_call in typed_calls:
            input_sources.extend([(f'{typed_call}({var_name}())', f'{typed_call}({var_name}())')])
            
        # 特别处理eval(f())这种嵌套调用模式
        eval_calls = re.findall(rf'eval\(\s*{re.escape(var_name)}\(\s*\)\s*\)', content_no_comments)
        for eval_call in eval_calls:
            input_sources.extend([(f'eval({var_name}())', eval_call)])
            
        # 处理eval(f()) with parameters的情况
        eval_with_params = re.findall(rf'eval\(\s*{re.escape(var_name)}\([^)]*\)\s*\)', content_no_comments)
        for eval_call in eval_with_params:
            input_sources.extend([(f'eval({var_name}(...))', eval_call)])
            
    # 更新input_analysis统计信息
    input_analysis['input_reassignment'] = len(input_reassignment)
    
    # 对重赋值情况下的输入调用进行单独计数
    # 特别处理input=sys.stdin.readline这种情况
    # 需要将代码中的input()调用计算为stdin.readline()调用
    if 'input' in input_reassignment:
        # 计算input()调用的次数
        input_calls_count = len(re.findall(r'input\(\s*\)', content_no_comments))
        # 计算类型转换的input()调用次数
        typed_input_calls = len(re.findall(r'(int|float|str)\(\s*input\(\s*\)\s*\)', content_no_comments))
        
        # 更新计数
        if 'input_reassignment' not in input_analysis:
            input_analysis['input_reassignment'] = 0
        input_analysis['input_reassignment'] += input_calls_count + typed_input_calls
        
        # 在counted_input_patterns中记录这些调用
        for i in range(input_calls_count):
            counted_input_patterns.add(f'input_reassignment_{i}')
        for i in range(typed_input_calls):
            counted_input_patterns.add(f'typed_input_reassignment_{i}')
    
    # 9. 检查lambda函数是否被调用
    # 检查lambda_names中的函数是否被调用
    for lambda_name in lambda_names:
        lambda_calls = re.findall(rf'{re.escape(lambda_name)}\(\)', content_no_comments)
        input_sources.extend([(f'{lambda_name}()', call) for call in lambda_calls])
    # 9. 检查文件读取相关的输入（如果可能是从文件获取数据）
    # 注意：这里主要关注的是用户输入，而不是文件读取
    
    # 查找map(int, input().split())模式
    map_int_patterns = []
    for input_type, _ in input_sources:
        if input_type == 'input()':
            # 检查input()相关的map模式
            patterns = re.findall(r'map\(\s*int\s*,\s*input\(\s*\)\.split\(\s*\)\s*\)', content_no_comments)
            map_int_patterns.extend(patterns)
    
    # 查找tuple(map(int, input().split()))模式
    tuple_map_patterns = []
    for input_type, _ in input_sources:
        if input_type == 'input()':
            patterns = re.findall(r'tuple\(\s*map\(\s*int\s*,\s*input\(\s*\)\.split\(\s*\)\s*\)\s*\)', content_no_comments)
            tuple_map_patterns.extend(patterns)
    
    # 查找字符串相关输入
    str_input_patterns = []
    for input_type, call in input_sources:
        if input_type == 'input()':
            str_input_patterns.append(call)
    
    # 查找list(map(int, input().split()))模式
    list_map_patterns = []
    for input_type, _ in input_sources:
        if input_type == 'input()':
            patterns = re.findall(r'list\(\s*map\(\s*int\s*,\s*input\(\s*\)\.split\(\s*\)\s*\)\s*\)', content_no_comments)
            list_map_patterns.extend(patterns)
    
    # 分析前20行来推断输入结构
    lines = content_no_comments.split('\n')[:30]
    
    input_analysis = {
        'total_input_calls': len(input_sources),
        'input_calls': len(input_calls),
        'sys_stdin_readline_calls': len(sys_stdin_readline),
        'sys_stdin_read_calls': len(sys_stdin_read),
        'sys_stdin_buffer_read_calls': len(sys_stdin_buffer_read),
        'sys_stdin_readlines_calls': len(sys_stdin_readlines),
        'stdin_readlines_calls': len(stdin_readlines),
        'stdin_read_calls': len(stdin_read),
        'sys_argv_usage': len(sys_argv_patterns) > 0,
        'stdin_assignments': len(stdin_assignments),
        'input_reassignments': len(input_reassignment),
        'map_int_calls': len(map_int_patterns),
        'tuple_map_calls': len(tuple_map_patterns),
        'list_map_calls': len(list_map_patterns),
        'has_n_length': False,
        'has_m_n': False,
        'has_m_n_k': False,
        'has_four_ints': False,
        'has_string_input': False,
        'has_stdin_input': len(sys_stdin_readline) > 0 or len(sys_stdin_readlines) > 0 or len(stdin_readlines) > 0 or len(stdin_read) > 0 or len(stdin_assignments) > 0,
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
    
    # 检查输入类型的转换
    has_int_input = False
    has_float_input = False
    has_str_input = False
    has_raw_input = False
    
    for line in lines:
        # 检查是否有类型转换的input()调用
        if 'int(input())' in line or 'int(' in line and 'input()' in line:
            has_int_input = True
        elif 'float(input())' in line or 'float(' in line and 'input()' in line:
            has_float_input = True
        elif 'str(input())' in line or 'str(' in line and 'input()' in line:
            has_str_input = True
        elif 'input()' in line and 'int(' not in line and 'float(' not in line and 'str(' not in line:
            has_raw_input = True
    
    # 检查是否只读取字符串（没有map(int, ...)）
    has_only_string_input = False
    if has_str_input or has_raw_input:
        if not has_int_input and not has_float_input and input_analysis['map_int_calls'] == 0:
            has_only_string_input = True
    
    # 更新输入调用统计，包含带参数的input()
    total_input_calls = len(input_sources)
    input_analysis['total_input_calls'] = total_input_calls
    
    input_analysis['has_string_input'] = has_only_string_input
    
    # 根据输入类型进行更精确的分类
    # 1. 首先检查是否有任何输入
    if input_analysis['total_input_calls'] == 0 and not input_analysis['has_stdin_input']:
        return "01_无输入"
    
    # 2. 检查是否主要是整数输入
    # 特别关注类型转换的stdin.readline()调用
    has_typed_stdin_readline = re.findall(r'(int|float|str)\(\s*stdin\.readline\(\s*\)\s*\)', content_no_comments)
    has_lambda_typed_stdin = re.findall(r'lambda\s*:\s*(int|float|str)\(\s*stdin\.readline\(\s*\)\s*\)', content_no_comments)
    
    # 处理简单的stdin.readline() + 数值操作的情况
    # 例如: n = int(stdin.readline()) + 1
    simple_stdin_op = re.findall(r'(int|float|str)\(\s*stdin\.readline\(\s*\)\s*\)\s*[+\-*/]\s*\d+', content_no_comments)
    
    # 特别关注单个整数输入情况
    # 避免将变量名误认为输入
    # 使用特殊标记来防止重复计算
    
    # 1. 收集所有真正的输入调用，不考虑变量赋值
    # 简单的stdin.readline()调用
    for pattern in re.findall(r'stdin\.readline\(\s*\)', content_no_comments):
        counted_input_patterns.add(f'stdin_readline:{pattern}')
    
    # 简单的sys.stdin.readline()调用
    for pattern in re.findall(r'sys\.stdin\.readline\(\s*\)', content_no_comments):
        counted_input_patterns.add(f'sys_stdin_readline:{pattern}')
    
    # 简单的input()调用
    for pattern in re.findall(r'input\(\s*\)', content_no_comments):
        counted_input_patterns.add(f'input:{pattern}')
    
    # 带类型转换的输入
    # int(input()), float(input()), str(input())
    for match in re.findall(r'(int|float|str)\(\s*input\(\s*\)\s*\)', content_no_comments):
        counted_input_patterns.add(f'typed_input:{match}')
    
    # int(stdin.readline()), float(stdin.readline()), str(stdin.readline())
    for match in re.findall(r'(int|float|str)\(\s*stdin\.readline\(\s*\)\s*\)', content_no_comments):
        counted_input_patterns.add(f'typed_stdin_readline:{match}')
    
    # int(sys.stdin.readline()), float(sys.stdin.readline()), str(sys.stdin.readline())
    for match in re.findall(r'(int|float|str)\(\s*sys\.stdin\.readline\(\s*\)\s*\)', content_no_comments):
        counted_input_patterns.add(f'typed_sys_stdin_readline:{match}')
    
    # 处理简单的stdin.readline() + 数值操作的情况
    for pattern in re.findall(r'(int|float|str)\(\s*stdin\.readline\(\s*\)\s*\)\s*[+\-*/]\s*\d+', content_no_comments):
        counted_input_patterns.add(f'stdin_op:{pattern}')
    
    # 添加重赋值的输入模式检测
    # 检测input=sys.stdin.readline这种模式
    for pattern in re.findall(r'(\w+)\s*=\s*sys\.stdin\.readline', content_no_comments):
        counted_input_patterns.add(f'sys_stdin_reassignment:{pattern}')
    
    # 检测input=stdin.readline这种模式
    for pattern in re.findall(r'(\w+)\s*=\s*stdin\.readline', content_no_comments):
        counted_input_patterns.add(f'stdin_reassignment:{pattern}')
    
    # 检测int(input())等类型转换的重赋值模式
    for pattern in re.findall(r'(\w+)\s*=\s*sys\.stdin\.readline', content_no_comments):
        typed_patterns = re.findall(rf'(int|float|str)\(\s*{re.escape(pattern)}\(\)\s*\)', content_no_comments)
        for typed_pattern in typed_patterns:
            counted_input_patterns.add(f'typed_{pattern}_reassignment:{typed_pattern}')
    
    # 检测其他输入重赋值模式
    for pattern in re.findall(r'(\w+)\s*=\s*sys\.stdin\.readlines', content_no_comments):
        counted_input_patterns.add(f'stdin_readlines_reassignment:{pattern}')
    
    for pattern in re.findall(r'(\w+)\s*=\s*stdin\.readlines', content_no_comments):
        counted_input_patterns.add(f'stdin_readlines_reassignment:{pattern}')
    
    # 计算真正的独立输入次数 - 避免重复计算
    real_input_calls = len(counted_input_patterns)
    
    # 检查是否有lambda函数调用
    lambda_calls_count = 0
    for lambda_name in lambda_names:
        calls = re.findall(rf'{re.escape(lambda_name)}\(\)', content_no_comments)
        lambda_calls_count += len(calls)
        for call in calls:
            counted_input_patterns.add(f'lambda_call:{lambda_name}')
    
    real_input_calls = len(counted_input_patterns)
    
    # 特别关注整数输入情况
    if (has_int_input or has_typed_stdin_readline or has_lambda_typed_stdin or simple_stdin_op) and input_analysis['map_int_calls'] == 0:
        if real_input_calls == 1:
            return "14_单个整数"
        elif real_input_calls == 2:
            return "15_2个整数"
        elif real_input_calls == 3:
            return "16_3个整数"
        elif real_input_calls == 4:
            return "17_4个整数"
        else:
            return f"18_{real_input_calls}个整数"
    
    # 3. 检查是否主要是浮点数输入
    if has_float_input and input_analysis['map_int_calls'] == 0:
        return "20_单个浮点数"  # 需要在目录结构中添加这个类别
    
    # 4. 检查是否主要是字符串输入
    if input_analysis['has_string_input'] and input_analysis['map_int_calls'] == 0:
        if input_analysis['total_input_calls'] == 1:
            return "02_单个字符串"
        elif input_analysis['total_input_calls'] == 2:
            return "03_2个字符串"
        elif input_analysis['total_input_calls'] == 3:
            return "04_3个字符串"
        else:
            return f"05_{input_analysis['total_input_calls']}个字符串"
    
    # 5. 检查stdin输入（没有input()调用）
    if input_analysis['has_stdin_input'] and input_analysis['input_calls'] == 0:
        # 检查stdin输入的复杂程度
        if input_analysis['sys_stdin_readlines_calls'] >= 1 or input_analysis['stdin_readlines_calls'] >= 1:
            # 使用readlines()通常意味着多行输入，需要进一步分析
            # 检查是否有input_type参数或类型转换
            has_type_conversion = 'input_type' in content_no_comments or 'int(' in content_no_comments
            if has_type_conversion:
                return "11_2行整数输入"  # 假设是2行整数输入（这是常见的模式）
            else:
                return "19_复杂输入结构"
        elif input_analysis['sys_stdin_readline_calls'] >= 1 or input_analysis['stdin_read_calls'] >= 1:
            # 单行stdin输入
            return "14_单个整数"
        elif input_analysis['stdin_assignments'] >= 1:
            # 通过变量赋值的stdin，需要进一步分析
            return "14_单个整数"
    
    # 6. 特殊情况：混合输入（stdin + input()）
    if input_analysis['has_stdin_input'] and input_analysis['input_calls'] > 0:
        # 这种复杂情况暂时归类为复杂输入结构
        return "19_复杂输入结构"
    
    # 7. 根据map(int, input().split())的调用次数和结构分类
    if input_analysis['map_int_calls'] >= 1:
        if input_analysis['has_n_length']:
            # 这种模式通常是：int n，然后 list<n> arr
            return "06_int_n_plus_list_arr"
        elif input_analysis['has_m_n']:
            return "07_int_m_plus_int_n"
        elif input_analysis['has_m_n_k']:
            return "08_int_m_plus_int_n_plus_int_k"
        elif input_analysis['has_four_ints']:
            return "09_4个整数"
        elif input_analysis['map_int_calls'] == 1:
            # 单行多整数输入
            return "10_单行多个整数"
        elif input_analysis['map_int_calls'] == 2:
            return "11_2行整数输入"
        elif input_analysis['map_int_calls'] == 3:
            return "12_3行整数输入"
        else:
            return f"13_{input_analysis['map_int_calls']}行整数输入"
    
    # 8. 其他情况：基本input()调用（未明确类型的）
    elif input_analysis['total_input_calls'] == 1:
        return "14_单个整数"  # 默认归类为整数
    elif input_analysis['total_input_calls'] == 2:
        return "15_2个整数"
    elif input_analysis['total_input_calls'] == 3:
        return "16_3个整数"
    elif input_analysis['total_input_calls'] == 4:
        return "17_4个整数"
    else:
        return f"18_{input_analysis['total_input_calls']}个整数"
    
    return "19_复杂输入结构"

def create_directory_structure(base_dir):
    """创建目录结构"""
    categories = [
        "01_无输入",
        "02_单个字符串",
        "03_2个字符串",
        "04_3个字符串",
        "05_5个字符串",
        "06_int_n_plus_list_arr",
        "07_int_m_plus_int_n",
        "08_int_m_plus_int_n_plus_int_k",
        "09_4个整数",
        "10_单行多个整数",
        "11_2行整数输入",
        "12_3行整数输入",
        "13_4行整数输入",
        "14_单个整数",
        "15_2个整数",
        "16_3个整数",
        "17_4个整数",
        "18_5个整数",
        "19_复杂输入结构",
        "20_单个浮点数"
    ]
    
    created_dirs = []
    for category in categories:
        dir_path = os.path.join(base_dir, category)
        os.makedirs(dir_path, exist_ok=True)
        created_dirs.append(dir_path)
    
    return created_dirs

def reorganize_files_by_input_type():
    """按照输入类型重新组织文件"""
    source_dir = "/home/wuyankai/myResearch/codeComplex/data/onlyCode/python"
    target_base_dir = "/home/wuyankai/myResearch/codeComplex/data/input_type_filteredData_v16"
    
    # 清理目标目录（如果存在）
    if os.path.exists(target_base_dir):
        print(f"清理旧的目录结构: {target_base_dir}")
        shutil.rmtree(target_base_dir)
    
    print("创建目录结构...")
    create_directory_structure(target_base_dir)
    
    # 统计信息
    stats = Counter()
    file_mapping = defaultdict(list)
    
    # 遍历所有Python文件
    python_files = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    print(f"找到 {len(python_files)} 个Python文件")
    
    # 分析和复制文件
    for i, file_path in enumerate(python_files):
        if i % 500 == 0:
            print(f"已处理 {i}/{len(python_files)} 个文件")
        
        # 分析输入类型
        input_type = analyze_specific_input_types(file_path)
        stats[input_type] += 1
        
        # 准备目标路径
        relative_path = os.path.relpath(file_path, source_dir)
        target_dir = os.path.join(target_base_dir, input_type)
        
        # 确保目标目录存在
        os.makedirs(target_dir, exist_ok=True)
        
        # 复制文件
        target_file = os.path.join(target_dir, relative_path)
        target_file_dir = os.path.dirname(target_file)
        os.makedirs(target_file_dir, exist_ok=True)
        
        try:
            shutil.copy2(file_path, target_file)
            file_mapping[input_type].append(relative_path)
        except Exception as e:
            print(f"复制文件失败: {file_path} -> {target_file}, 错误: {e}")
    
    print("\n=== 分类完成 ===")
    print(f"总文件数: {sum(stats.values())}")
    print("\n各类别文件数量:")
    
    for category, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        print(f"  {category}: {count} 个文件")
    
    # 保存统计信息
    with open('/home/wuyankai/myResearch/codeComplex/data/input_type_filteredData_v14/分类统计.txt', 'w', encoding='utf-8') as f:
        f.write("Python文件按输入类型重新分类统计\n")
        f.write("="*50 + "\n\n")
        f.write(f"总文件数: {sum(stats.values())}\n\n")
        f.write("各类别文件数量:\n")
        f.write("-"*30 + "\n")
        
        for category, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / sum(stats.values())) * 100
            f.write(f"{category}: {count} 个文件 ({percentage:.2f}%)\n")
        
        f.write("\n" + "="*50 + "\n")
        f.write("各类别样本文件:\n")
        f.write("="*50 + "\n")
        
        for category in sorted(stats.keys()):
            if file_mapping[category]:
                f.write(f"\n{category} ({stats[category]} 个文件):\n")
                for sample_file in file_mapping[category][:10]:  # 只显示前10个样本
                    f.write(f"  - {sample_file}\n")
                if len(file_mapping[category]) > 10:
                    f.write(f"  ... 还有 {len(file_mapping[category]) - 10} 个文件\n")
    
    print(f"\n分类结果已保存到: /home/wuyankai/myResearch/codeComplex/data/input_type_filteredData_v16/分类统计.txt")
    return stats

def main():
    print("开始按输入类型重新组织Python文件...")
    stats = reorganize_files_by_input_type()
    print("文件重新组织完成！")

if __name__ == "__main__":
    main()