import os
import json
import numpy as np
import matplotlib.pyplot as plt

# 定义复杂度类型映射
complexity_map = {
    'constant': 'Constant',
    'linear': 'Linear',
    'quadratic': 'Quadratic',
    'cubic': 'Cubic',
    'logn': 'Logarithmic',
    'nlogn': 'N Log N',
    'np': 'np'
}

# 定义标签顺序（按照用户要求）
true_labels_order = ['constant', 'logn', 'linear', 'nlogn', 'quadratic', 'cubic', 'np']
pred_labels_order = ['constant', 'logn', 'linear', 'nlogn', 'quadratic', 'cubic', 'np']

def parse_gpt4_results(file_path):
    """
    解析GPT-4结果文件
    
    Args:
        file_path: GPT-4结果文件路径
    
    Returns:
        list: 包含所有结果的列表，每个元素是(真实标签, 预测标签)
    """
    results = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    data = json.loads(line)
                    true_label = data.get('answer', '')  # answer是真实标签
                    pred_label = data.get('complexity', '')  # complexity是预测标签
                    
                    # 验证标签有效性
                    if true_label in complexity_map and pred_label in complexity_map:
                        results.append((true_label, pred_label))
                    else:
                        print(f"跳过无效标签: true={true_label}, pred={pred_label}")
                        
                except json.JSONDecodeError as e:
                    print(f"JSON解析错误: {e}, 行内容: {line}")
    
    return results

def calculate_statistics(results):
    """
    计算统计信息
    
    Args:
        results: 解析后的结果列表
    
    Returns:
        tuple: (总文件数, 正确预测数, 准确率, 详细统计, 混淆矩阵)
    """
    total_files = len(results)
    correct_predictions = 0
    detailed_stats = {}
    
    # 初始化详细统计
    for complexity in complexity_map:
        detailed_stats[complexity] = {'total': 0, 'correct': 0, 'incorrect': []}
    
    # 初始化混淆矩阵
    confusion_matrix = {}
    for true_label in true_labels_order:
        confusion_matrix[true_label] = {}
        for pred_label in pred_labels_order:
            confusion_matrix[true_label][pred_label] = 0
    
    # 处理每个结果
    for i, (true_label, pred_label) in enumerate(results):
        detailed_stats[true_label]['total'] += 1
        
        if true_label == pred_label:
            correct_predictions += 1
            detailed_stats[true_label]['correct'] += 1
        else:
            detailed_stats[true_label]['incorrect'].append({
                'index': i,
                'predicted': pred_label
            })
        
        # 更新混淆矩阵
        confusion_matrix[true_label][pred_label] += 1
    
    accuracy = correct_predictions / total_files if total_files > 0 else 0
    return total_files, correct_predictions, accuracy, detailed_stats, confusion_matrix

def generate_confusion_matrix(confusion_matrix, total_files, output_dir):
    """
    生成混淆矩阵热力图
    
    Args:
        confusion_matrix: 混淆矩阵数据
        total_files: 总文件数
        output_dir: 输出目录
    """
    # 计算百分比混淆矩阵
    conf_matrix_percent = np.zeros((7, 7))
    for i, true_label in enumerate(true_labels_order):
        for j, pred_label in enumerate(pred_labels_order):
            count = confusion_matrix[true_label][pred_label]
            percent = (count / total_files) * 100 if total_files > 0 else 0
            conf_matrix_percent[i, j] = percent
    
    # 生成热力图
    fig, ax = plt.subplots(figsize=(12, 10))
    im = ax.imshow(conf_matrix_percent, cmap='Blues')
    
    # 设置标签
    true_labels_display = ['constant', 'logn', 'linear', 'nlogn', 'quadratic', 'cubic', 'np']
    pred_labels_display = ['constant', 'logn', 'linear', 'nlogn', 'quadratic', 'cubic', 'np']
    
    ax.set_xticks(np.arange(len(pred_labels_display)))
    ax.set_yticks(np.arange(len(true_labels_display)))
    ax.set_xticklabels(pred_labels_display)
    ax.set_yticklabels(true_labels_display)
    
    # 在每个单元格中添加百分比值
    for i in range(len(true_labels_display)):
        for j in range(len(pred_labels_display)):
            text = ax.text(j, i, f'{conf_matrix_percent[i, j]:.2f}%',
                          ha="center", va="center", color="black" if conf_matrix_percent[i, j] < 50 else "white")
    
    ax.set_title('GPT-4 复杂度预测混淆矩阵（百分比）')
    ax.set_xlabel('预测标签')
    ax.set_ylabel('真实标签')
    
    # 添加颜色条
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel('百分比', rotation=-90, va="bottom")
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'gpt4_confusion_matrix_corrected.png'), dpi=300, bbox_inches='tight')
    print(f"混淆矩阵图表已保存至: {os.path.join(output_dir, 'gpt4_confusion_matrix_corrected.png')}")
    
    # 保存混淆矩阵数据
    with open(os.path.join(output_dir, 'gpt4_confusion_matrix_corrected.json'), 'w') as f:
        json.dump({
            'matrix': conf_matrix_percent.tolist(),
            'true_labels': true_labels_display,
            'pred_labels': pred_labels_display
        }, f, indent=2)
    print(f"混淆矩阵数据已保存至: {os.path.join(output_dir, 'gpt4_confusion_matrix_corrected.json')}")

def generate_statistics(results, output_dir):
    """
    生成统计结果
    
    Args:
        results: 解析后的结果列表
        output_dir: 输出目录
    """
    total_files, correct_predictions, accuracy, detailed_stats, confusion_matrix = calculate_statistics(results)
    
    print(f"总文件数: {total_files}")
    print(f"正确预测数: {correct_predictions}")
    print(f"准确率: {accuracy:.4f}")
    print("\n详细统计:")
    
    # 准备数据用于绘图
    labels = []
    total_counts = []
    correct_counts = []
    
    for complexity, stats in detailed_stats.items():
        if stats['total'] > 0:
            labels.append(complexity.capitalize())
            total_counts.append(stats['total'])
            correct_counts.append(stats['correct'])
            
            complexity_accuracy = stats['correct'] / stats['total'] if stats['total'] > 0 else 0
            print(f"{complexity}: 总数={stats['total']}, 正确={stats['correct']}, 准确率={complexity_accuracy:.4f}")
    
    # 生成条形图
    x = np.arange(len(labels))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(12, 6))
    bars1 = ax.bar(x - width/2, total_counts, width, label='总数')
    bars2 = ax.bar(x + width/2, correct_counts, width, label='正确')
    
    ax.set_xlabel('复杂度类型')
    ax.set_ylabel('数量')
    ax.set_title('GPT-4 复杂度预测统计（修正后）')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    
    # 在条形图上添加数值
    for bar in bars1:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    
    for bar in bars2:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    
    # 保存图片
    os.makedirs(output_dir, exist_ok=True)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'gpt4_accuracy_statistics_corrected.png'), dpi=300, bbox_inches='tight')
    print(f"\n统计图表已保存至: {os.path.join(output_dir, 'gpt4_accuracy_statistics_corrected.png')}")
    
    # 生成混淆矩阵热力图
    generate_confusion_matrix(confusion_matrix, total_files, output_dir)
    
    # 保存详细统计数据
    with open(os.path.join(output_dir, 'gpt4_detailed_stats_corrected.json'), 'w') as f:
        json.dump({
            'total_files': total_files,
            'correct_predictions': correct_predictions,
            'accuracy': accuracy,
            'detailed_stats': detailed_stats,
            'confusion_matrix': confusion_matrix
        }, f, indent=2)
    print(f"详细统计数据已保存至: {os.path.join(output_dir, 'gpt4_detailed_stats_corrected.json')}")

def main():
    """主函数"""
    # 文件路径
    input_file = '/home/wuyankai/myResearch/codeComplex/LLM_v1/results/gpt4-python-codecomplex-simple.txt'
    output_dir = '/home/wuyankai/myResearch/codeComplex/LLM_v1/results'
    
    # 解析结果
    print("正在解析GPT-4结果文件...")
    results = parse_gpt4_results(input_file)
    print(f"成功解析 {len(results)} 个结果")
    
    # 生成统计信息
    print("\n正在生成统计信息...")
    generate_statistics(results, output_dir)
    
    print("\n处理完成！")

if __name__ == "__main__":
    main()