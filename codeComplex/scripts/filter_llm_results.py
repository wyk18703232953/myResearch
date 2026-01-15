#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
过滤LLM结果JSON文件，只保留那些在data目录下存在对应Python文件的记录
"""
import json
import os
import sys

# 配置文件路径
INPUT_PATH = "/home/wuyankai/myResearch/codeComplex/results/LLM/ast_llm_results.json"
OUTPUT_PATH = "/home/wuyankai/myResearch/codeComplex/results/LLM/ast_llm_results1_demo_filtered.json"
DATA_ROOT = "/home/wuyankai/myResearch/codeComplex/data/filteredData/python"


def get_existing_complexity_ids():
    """
    获取data目录下所有存在的Python文件的complexity_id
    
    返回:
    存在的complexity_id集合
    """
    existing_ids = set()
    
    # 遍历所有复杂度类型目录
    for complexity_type in os.listdir(DATA_ROOT):
        type_dir = os.path.join(DATA_ROOT, complexity_type)
        if not os.path.isdir(type_dir):
            continue
            
        # 获取该类型下所有Python文件
        for filename in os.listdir(type_dir):
            if filename.endswith(".py"):
                # 提取complexity_id（去掉.py扩展名）
                complexity_id = filename[:-3]
                existing_ids.add(complexity_id)
    
    return existing_ids


def generate_complexity_id(expected_complexity, index):
    """
    根据预期复杂度和索引生成complexity_id
    
    参数:
    expected_complexity: 预期的复杂度类型
    index: 该复杂度类型内的索引
    
    返回:
    生成的complexity_id字符串
    """
    return f"python_{expected_complexity}_{index:04d}"


def filter_llm_results():
    """
    过滤LLM结果JSON文件
    """
    # 读取现有文件列表
    existing_ids = get_existing_complexity_ids()
    print(f"找到 {len(existing_ids)} 个现有文件")
    
    # 读取输入JSON文件
    if not os.path.exists(INPUT_PATH):
        print(f"输入文件不存在: {INPUT_PATH}")
        return False
    
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    detailed_records = data.get("detailed_records", [])
    print(f"输入JSON文件中包含 {len(detailed_records)} 条记录")
    
    # 按复杂度类型分组记录
    records_by_complexity = {}
    for record in detailed_records:
        complexity = record.get("expected_complexity")
        if complexity not in records_by_complexity:
            records_by_complexity[complexity] = []
        records_by_complexity[complexity].append(record)
    
    # 过滤记录并添加complexity_id字段
    filtered_records = []
    for complexity, records in records_by_complexity.items():
        # 跳过没有对应目录的复杂度类型
        if complexity not in os.listdir(DATA_ROOT):
            continue
            
        # 为每条记录生成complexity_id并检查是否存在
        for i, record in enumerate(records, 1):
            complexity_id = generate_complexity_id(complexity, i)
            if complexity_id in existing_ids:
                # 添加complexity_id字段
                record["complexity_id"] = complexity_id
                filtered_records.append(record)
    
    print(f"过滤后保留 {len(filtered_records)} 条记录")
    
    # 保存过滤后的JSON文件
    output_data = {"detailed_records": filtered_records}
    
    backup_path = f"{OUTPUT_PATH}.bak"
    if os.path.exists(OUTPUT_PATH):
        os.rename(OUTPUT_PATH, backup_path)
        print(f"已创建备份: {backup_path}")
    
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print(f"已保存过滤后的文件: {OUTPUT_PATH}")
    return True


if __name__ == "__main__":
    print("开始过滤LLM结果文件...")
    success = filter_llm_results()
    if success:
        print("过滤完成！")
    else:
        print("过滤失败！")
        sys.exit(1)
