# //读取data/python_data.jsonl文件
import json
import os

python_file = 'd:/MyResearch/codeComplex/data/python_data.jsonl'
# 读取文件内容
with open(python_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    # 打印前5行
    for line in lines[:5]:
        print(line.strip())