import json
import os
import re
from typing import Dict, List, Optional

# 从fusion_llm_refine.py复制相关函数和配置
equivalence = {
    "constant": {"constant", "o(1)", "1"},
    "linear": {"linear", "o(n)", "n"},
    "logn": {"logn", "log n", "o(log n)", "o(logn)"},
    "nlogn": {"nlogn", "n log n", "o(n log n)", "o(n logn)"},
    "quadratic": {"quadratic", "o(n^2)", "n^2"},
    "cubic": {"cubic", "o(n^3)", "n^3"},
    "np": {"np", "o(n^p)", "n^p", "exponential", "o(2^n)", "2^n"},
}

def normalize_label(raw: Optional[str]) -> Optional[str]:
    if not raw:
        return None
    text = raw.strip().lower()
    text_compact = re.sub(r"\s+", "", text)

    # 优先检查完整匹配，然后检查包含关系
    # 按照复杂度的特异性排序，避免前缀匹配问题（如logn被误判为linear）
    sorted_keys = ["nlogn", "logn", "linear", "quadratic", "cubic", "constant", "np"]
    
    for key in sorted_keys:
        if key not in equivalence:
            continue
        variants = equivalence[key]
        
        # 优先检查精确匹配
        if text in variants or text_compact in variants:
            return key
        
        # 然后检查变体是否在文本中（完整单词匹配）
        for v in variants:
            if f" {v} " in f" {text} " or f" {v} " in f" {text_compact} ":
                return key
            # 检查变体是否是文本的开头或结尾
            if text.startswith(f"{v} ") or text.endswith(f" {v}"):
                return key
            if text_compact.startswith(f"{v}") or text_compact.endswith(f"{v}"):
                return key
    return None

def compare_complexity(actual: Optional[str], expected: str) -> bool:
    if not actual:
        return False
    expected = expected.strip().lower()
    if expected in equivalence:
        return actual in equivalence[expected] or actual == expected
    return actual == expected

if __name__ == "__main__":
    json_file = "/home/wuyankai/myResearch/codeComplex/results/LLM/ast_llm_results1_demo_filtered.json"
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    detailed_records = data.get('detailed_records', [])
    
    # 使用原始is_match字段计算准确率
    total_original = len(detailed_records)
    correct_original = sum(1 for record in detailed_records if record.get('is_match', False))
    accuracy_original = (correct_original / total_original) * 100 if total_original > 0 else 0
    
    # 使用fusion脚本的方法计算准确率
    correct_fusion = 0
    total_fusion = 0
    differences = []
    
    for record in detailed_records:
        expected = (record.get('expected_complexity') or "").strip().lower()
        llm_raw = record.get('model_raw_output')
        is_match_original = record.get('is_match', False)
        
        total_fusion += 1
        
        # 使用fusion脚本的方法计算匹配
        y_llm = normalize_label(llm_raw)
        is_match_fusion = compare_complexity(y_llm, expected)
        
        if is_match_fusion:
            correct_fusion += 1
        
        # 记录差异
        if is_match_original != is_match_fusion:
            differences.append({
                'complexity_id': record.get('complexity_id'),
                'expected': expected,
                'model_raw_output': llm_raw,
                'y_llm': y_llm,
                'is_match_original': is_match_original,
                'is_match_fusion': is_match_fusion
            })
    
    accuracy_fusion = (correct_fusion / total_fusion) * 100 if total_fusion > 0 else 0
    
    print("=== 准确率比较 ===")
    print(f"原始is_match字段准确率: {correct_original}/{total_original} ({accuracy_original:.2f}%)")
    print(f"Fusion脚本方法准确率: {correct_fusion}/{total_fusion} ({accuracy_fusion:.2f}%)")
    print(f"差异记录数: {len(differences)}")
    print()
    
    # 输出部分差异记录进行分析
    print("=== 差异记录示例 (前20个) ===")
    for i, diff in enumerate(differences[:20]):
        print(f"{i+1}. ID: {diff['complexity_id']}")
        print(f"   期望: {diff['expected']}")
        print(f"   LLM原始输出: {diff['model_raw_output']}")
        print(f"   归一化后: {diff['y_llm']}")
        print(f"   原始匹配: {diff['is_match_original']}")
        print(f"   Fusion匹配: {diff['is_match_fusion']}")
        print()
    
    # 分析差异原因
    print("=== 差异原因分析 ===")
    # 统计差异类型
    diff_types = {}
    for diff in differences:
        key = f"原始{'对' if diff['is_match_original'] else '错'}_Fusion{'对' if diff['is_match_fusion'] else '错'}"
        diff_types[key] = diff_types.get(key, 0) + 1
    
    for key, count in diff_types.items():
        print(f"{key}: {count}个记录")
