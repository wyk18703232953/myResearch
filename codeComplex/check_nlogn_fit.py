import json
import os

# 遍历nlogn类型的结果文件夹
demo_dir = "/home/wuyankai/myResearch/codeComplex/demo/filteredData/python/nlogn"

nlogn_count = 0
other_count = 0

for folder_name in os.listdir(demo_dir):
    if folder_name.startswith("results_python_nlogn_"):
        report_path = os.path.join(demo_dir, folder_name, "analysis_report.json")
        if os.path.exists(report_path):
            try:
                with open(report_path, "r") as f:
                    report = json.load(f)
                
                # 找出最佳拟合模型
                best_model = None
                best_score = -1
                
                for model_name, model_data in report.get("models", {}).items():
                    score = model_data.get("confidence_score", model_data.get("r2", -1))
                    if score > best_score:
                        best_score = score
                        best_model = model_name
                
                # 检查最佳模型是否为N Log N
                if best_model == "N Log N":
                    nlogn_count += 1
                else:
                    other_count += 1
                
                # 打印前10个结果作为示例
                if (nlogn_count + other_count) <= 10:
                    print(f"{folder_name}: 最佳模型={best_model}, 分数={best_score:.4f}")
                    
            except Exception as e:
                print(f"处理 {folder_name} 时出错: {e}")

print(f"\n统计结果:")
print(f"nlogn类型的文件总数: {nlogn_count + other_count}")
print(f"最佳模型为N Log N的数量: {nlogn_count}")
print(f"最佳模型为其他类型的数量: {other_count}")
print(f"N Log N模型的比例: {nlogn_count / (nlogn_count + other_count) * 100:.2f}%")