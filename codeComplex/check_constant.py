import json

# 读取生成的JSON报告
report_path = "/home/wuyankai/myResearch/codeComplex/results/fusion_llm_report_universal_v14.json"

with open(report_path, "r", encoding="utf-8") as f:
    report = json.load(f)

# 检查summary中的types字段
print("Types in summary:")
for type_name, stats in report["summary"]["types"].items():
    print(f"- {type_name}: {stats}")

# 检查detailed_records中是否有constant类型
print("\nChecking detailed records for constant type:")
constant_count = 0
for record in report["detailed_records"]:
    if record.get("expected_complexity") == "constant":
        constant_count += 1
        if constant_count <= 5:  # 只显示前5条
            print(f"  {record.get('complexity_id')}: expected={record.get('expected_complexity')}, y_llm={record.get('y_llm')}, y_fit={record.get('y_fit')}, y_final={record.get('y_final')}")

print(f"\nTotal constant records: {constant_count}")