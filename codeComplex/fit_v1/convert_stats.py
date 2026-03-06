#!/usr/bin/env python3
import json
import os

def convert_json_to_txt(json_file_path, output_file_path):
    """
    将详细统计JSON文件转换为指定格式的TXT文件
    格式：{"complexity":"实际复杂度","file":"文件名","answer":"预测复杂度"}
    """
    
    # 读取JSON文件
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 提取详细统计信息
    detailed_stats = data.get('detailed_stats', {})
    total_files = data.get('total_files', 0)
    correct_predictions = data.get('correct_predictions', 0)
    
    print(f"总文件数: {total_files}")
    print(f"正确预测数: {correct_predictions}")
    print(f"错误预测数: {total_files - correct_predictions}")
    
    # 准备输出内容
    output_lines = []
    
    # 遍历每个复杂度类别
    for actual_complexity, stats in detailed_stats.items():
        total = stats.get('total', 0)
        correct = stats.get('correct', 0)
        incorrect_predictions = stats.get('incorrect', [])
        
        print(f"{actual_complexity}: 总数={total}, 正确={correct}, 错误={len(incorrect_predictions)}")
        
        # 处理正确预测的样本
        for i in range(correct):
            # 正确预测时，file字段为空
            file_name = ""
            # 正确预测时，预测复杂度等于实际复杂度
            predicted_complexity = actual_complexity
            
            # 生成指定格式的行
            line = f'{{"complexity":"{actual_complexity}","file":"{file_name}","answer":"{predicted_complexity}"}}'
            output_lines.append(line)
        
        # 处理错误预测的样本
        for prediction in incorrect_predictions:
            file_name = prediction.get('file', '')
            predicted_complexity = prediction.get('predicted', '')
            
            # 生成指定格式的行
            line = f'{{"complexity":"{actual_complexity}","file":"{file_name}","answer":"{predicted_complexity}"}}'
            output_lines.append(line)
    
    # 写入TXT文件
    with open(output_file_path, 'w', encoding='utf-8') as f:
        for line in output_lines:
            f.write(line + '\n')
    
    print(f"转换完成！共生成 {len(output_lines)} 行数据")
    print(f"输出文件：{output_file_path}")
    
    return len(output_lines)

if __name__ == "__main__":
    # 文件路径
    json_file = "/home/wuyankai/myResearch/codeComplex/fit_v1/statistics/detailed_stats.json"
    output_dir = "/home/wuyankai/myResearch/codeComplex/fit_v1/results"
    output_file = os.path.join(output_dir, "converted_stats.txt")
    
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 执行转换
    try:
        count = convert_json_to_txt(json_file, output_file)
        print(f"成功转换 {count} 条记录")
    except Exception as e:
        print(f"转换过程中出现错误：{e}")