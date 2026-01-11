import json
import os

# 定义输入文件路径
input_file = '/home/wuyankai/myResearch/codeComplex/results/LLM/ast_llm_results.json'

# 读取JSON文件
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 创建复杂度计数器
summary = data.get('summary', {})
detailed_records = data.get('detailed_records', [])

# 初始化复杂度计数器
complexity_counters = {}

# 遍历所有记录，为每个复杂度类型创建计数器
for record in detailed_records:
    complexity = record.get('expected_complexity', '')
    if complexity not in complexity_counters:
        complexity_counters[complexity] = 0

# 再次遍历记录，添加complexity_id字段
for record in detailed_records:
    complexity = record.get('expected_complexity', '')
    if complexity in complexity_counters:
        complexity_counters[complexity] += 1
        # 格式化complexity_id，如python_linear_0843
        complexity_id = f'python_{complexity}_{complexity_counters[complexity]:04d}'
        record['complexity_id'] = complexity_id

# 写入修改后的JSON文件
with open(input_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("已成功添加complexity_id字段")
print(f"处理的记录总数: {len(detailed_records)}")
print("复杂度统计:")
for complexity, count in complexity_counters.items():
    print(f"  {complexity}: {count} 条记录")
