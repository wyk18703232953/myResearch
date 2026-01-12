import json

# 读取筛选后的LLM结果文件
filtered_path = '/home/wuyankai/myResearch/codeComplex/results/LLM/ast_llm_results1_demo_filtered.json'

print("正在统计 /home/wuyankai/myResearch/codeComplex/results/LLM/ast_llm_results1_demo_filtered.json 中各类型的数量...")
print("=" * 60)

with open(filtered_path, 'r', encoding='utf-8') as f:
    filtered_data = json.load(f)
    filtered_records = filtered_data.get('detailed_records', [])

# 统计各类型的数量
type_counts = {}
for record in filtered_records:
    expected = (record.get('expected_complexity') or '').strip().lower()
    type_counts[expected] = type_counts.get(expected, 0) + 1

# 按数量排序
sorted_counts = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)

# 输出结果
print("类型级数量统计：")
print("-" * 60)
total = 0
for t, count in sorted_counts:
    print(f"{t:<10}: {count:>5} 条")
    total += count

print("-" * 60)
print(f"总计: {total:>15} 条")
