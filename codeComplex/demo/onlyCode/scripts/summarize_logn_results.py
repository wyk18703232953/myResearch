import os
import json
import glob

# 定义logn结果目录路径
results_dir = "d:/MyResearch/codeComplex/demo/onlyCode/results/logn"

def get_best_model(fit_results_json):
    """从fit_results.json文件中获取最佳拟合模型"""
    with open(fit_results_json, 'r', encoding='utf-8') as f:
        fit_results = json.load(f)
    
    # 找出R²值最高的模型
    best_model = None
    best_r_squared = -1
    
    for model_name, result in fit_results.items():
        if result['success'] and result['r_squared'] > best_r_squared:
            best_r_squared = result['r_squared']
            best_model = model_name
    
    return best_model, best_r_squared

def get_best_model_from_report(report_file):
    """从报告文件中获取最佳拟合模型"""
    with open(report_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        if "最佳拟合模型:" in line:
            best_model = line.split(":")[1].strip()
            best_r_squared_line = lines[i+1]
            if "最佳R²值:" in best_r_squared_line:
                best_r_squared = float(best_r_squared_line.split(":")[1].strip())
            return best_model, best_r_squared
    
    return None, 0

def main():
    # 创建结果统计字典
    results_summary = {
        'total_files': 0,
        'logarithmic_count': 0,
        'non_logarithmic_count': 0,
        'failed_files': [],
        'results': []
    }
    
    # 遍历所有results_python_logn_*目录
    result_dirs = glob.glob(os.path.join(results_dir, "results_python_logn_*"))
    result_dirs.sort()  # 按顺序处理
    
    print(f"找到 {len(result_dirs)} 个结果目录")
    
    for dir_path in result_dirs:
        # 提取题目编号
        dir_name = os.path.basename(dir_path)
        if "python_logn_" in dir_name:
            problem_id = dir_name.split("python_logn_")[1]
        else:
            problem_id = dir_name
        
        results_summary['total_files'] += 1
        
        # 尝试从fit_results.json获取结果
        fit_results_json = os.path.join(dir_path, "fit_results.json")
        report_file = os.path.join(dir_path, f"time_complexity_report_{dir_name}.txt")
        
        best_model = None
        best_r_squared = 0
        
        if os.path.exists(fit_results_json):
            best_model, best_r_squared = get_best_model(fit_results_json)
        elif os.path.exists(report_file):
            best_model, best_r_squared = get_best_model_from_report(report_file)
        else:
            # 查找任何报告文件
            report_files = glob.glob(os.path.join(dir_path, "time_complexity_report*.txt"))
            if report_files:
                best_model, best_r_squared = get_best_model_from_report(report_files[0])
        
        if best_model:
            # 记录结果
            results_summary['results'].append({
                'problem_id': problem_id,
                'best_model': best_model,
                'r_squared': best_r_squared
            })
            
            # 统计logarithmic模型数量
            if best_model == 'Logarithmic':
                results_summary['logarithmic_count'] += 1
            else:
                results_summary['non_logarithmic_count'] += 1
                print(f"问题 {problem_id} 未识别为Logarithmic，最佳模型是: {best_model} (R²={best_r_squared:.6f})")
        else:
            # 记录失败的文件
            results_summary['failed_files'].append(problem_id)
            print(f"问题 {problem_id} 分析失败，无法获取最佳模型")
    
    # 计算正确率
    if results_summary['total_files'] > 0:
        accuracy = results_summary['logarithmic_count'] / results_summary['total_files']
    else:
        accuracy = 0
    
    # 生成汇总报告
    summary_report = """时间复杂度分析汇总报告
====================

总体统计:
- 总分析文件数: {total_files}
- 识别为Logarithmic的文件数: {logarithmic_count}
- 未识别为Logarithmic的文件数: {non_logarithmic_count}
- 分析失败的文件数: {failed_count}
- 正确率: {accuracy:.2%}

未识别为Logarithmic的问题:
{non_logarithmic_list}

分析失败的问题:
{failed_list}

所有分析结果详情:
{detailed_list}
"""
    
    # 构建未识别为Logarithmic的列表
    non_logarithmic_list = ""
    for result in results_summary['results']:
        if result['best_model'] != 'Logarithmic':
            non_logarithmic_list += f"- 问题 {result['problem_id']}: 最佳模型={result['best_model']}, R²={result['r_squared']:.6f}\n"
    
    if not non_logarithmic_list:
        non_logarithmic_list = "无"
    
    # 构建分析失败的列表
    failed_list = "\n".join([f"- 问题 {problem_id}" for problem_id in results_summary['failed_files']])
    if not failed_list:
        failed_list = "无"
    
    # 构建详细结果列表
    detailed_list = ""
    for result in results_summary['results']:
        detailed_list += f"- 问题 {result['problem_id']}: 最佳模型={result['best_model']}, R²={result['r_squared']:.6f}\n"
    
    # 生成报告内容
    report_content = summary_report.format(
        total_files=results_summary['total_files'],
        logarithmic_count=results_summary['logarithmic_count'],
        non_logarithmic_count=results_summary['non_logarithmic_count'],
        failed_count=len(results_summary['failed_files']),
        accuracy=accuracy,
        non_logarithmic_list=non_logarithmic_list,
        failed_list=failed_list,
        detailed_list=detailed_list
    )
    
    # 保存报告
    report_path = os.path.join(results_dir, "results_summary_report.txt")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"\n汇总报告已生成: {report_path}")
    print(f"\n总体结果:")
    print(f"- 总分析文件数: {results_summary['total_files']}")
    print(f"- 识别为Logarithmic的文件数: {results_summary['logarithmic_count']}")
    print(f"- 正确率: {accuracy:.2%}")
    print(f"- 分析失败的文件数: {len(results_summary['failed_files'])}")
    
    if results_summary['failed_files']:
        print(f"分析失败的问题: {', '.join(results_summary['failed_files'])}")

if __name__ == "__main__":
    main()
