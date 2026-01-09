import json
from collections import Counter

# 读取输入的LLM结果文件
input_path = "/home/wuyankai/myResearch/codeComplex/results/LLM/ast_llm_results1_demo_filtered.json"

with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 统计不同复杂度类型的数量
expected_types = Counter()
for record in data["detailed_records"]:
    expected = record.get("expected_complexity", "").strip().lower()
    expected_types[expected] += 1

print("复杂度类型统计 (输入文件):")
for expected_type, count in expected_types.most_common():
    print(f"- {expected_type}: {count} 条记录")

# 检查complexity_id中是否包含constant
print("\n检查complexity_id中是否包含constant:")
constant_in_id = 0
for record in data["detailed_records"]:
    complexity_id = record.get("complexity_id", "")
    if "constant" in complexity_id:
        constant_in_id += 1
        print(f"- {complexity_id}")

print(f"\ncomplexity_id中包含constant的记录数: {constant_in_id}")