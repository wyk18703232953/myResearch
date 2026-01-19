#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新LLM结果JSON文件，从ast_accuracy_summary.json获取信息并更新到ast_llm_results1_demo_filtered.json
"""
import json
import os
import sys

# 配置文件路径
ACCURACY_SUMMARY_PATH = "/home/wuyankai/myResearch/codeComplex/results/LLM/ast_accuracy_summary.json"
LLM_RESULTS_SOURCE_PATH = "/home/wuyankai/myResearch/codeComplex/results/LLM/ast_llm_results.json"
LLM_RESULTS_PATH = "/home/wuyankai/myResearch/codeComplex/results/LLM/ast_llm_results1_demo_filtered.json"
DATA_ROOT = "/home/wuyankai/myResearch/codeComplex/data/filteredData/python"


def get_existing_files():
    """
    获取data目录下所有存在的Python文件
    
    返回:
    存在的complexity_id集合
    """
    existing_files = set()
    
    # 遍历所有复杂度类型目录
    complexity_types = ["constant","logn", "linear", "nlogn", "quadratic", "cubic","np"]
    
    for type_name in complexity_types:
        type_dir = os.path.join(DATA_ROOT, type_name)
        if not os.path.exists(type_dir):
            print(f"目录不存在: {type_dir}")
            continue
            
        # 获取该类型下所有Python文件
        for filename in os.listdir(type_dir):
            if filename.endswith(".py"):
                # 提取complexity_id（去掉.py扩展名）
                complexity_id = filename[:-3]
                existing_files.add(complexity_id)
    
    return existing_files


def update_llm_results():
    """
    更新LLM结果JSON文件：
    1. 根据data目录下的实际Python文件过滤记录
    2. 从ast_llm_results1.json获取detailed_records
    """
    # 读取现有文件列表
    existing_files = get_existing_files()
    print(f"找到 {len(existing_files)} 个现有文件")
    
    # 读取LLM结果源文件
    if not os.path.exists(LLM_RESULTS_SOURCE_PATH):
        print(f"LLM结果源文件不存在: {LLM_RESULTS_SOURCE_PATH}")
        return False
    
    with open(LLM_RESULTS_SOURCE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    detailed_records = data.get("detailed_records", [])
    print(f"源JSON文件中包含 {len(detailed_records)} 条记录")
    
    # 过滤记录，只保留存在对应Python文件的记录
    filtered_records = []
    for record in detailed_records:
        complexity_id = record.get("complexity_id")
        if (complexity_id in existing_files or complexity_id.startswith("python_np")):
            filtered_records.append(record)
    
    print(f"过滤后保留 {len(filtered_records)} 条记录")
    
    # 更新JSON数据
    data["detailed_records"] = filtered_records
    
    # 保存更新后的JSON文件
    backup_path = f"{LLM_RESULTS_PATH}.bak"
    # 如果目标文件已存在，先备份
    if os.path.exists(LLM_RESULTS_PATH):
        os.rename(LLM_RESULTS_PATH, backup_path)
        print(f"已创建备份: {backup_path}")
    
    with open(LLM_RESULTS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"已更新文件: {LLM_RESULTS_PATH}")
    return True


if __name__ == "__main__":
    print("开始更新LLM结果文件...")
    success = update_llm_results()
    if success:
        print("更新完成！")
    else:
        print("更新失败！")
        sys.exit(1)
