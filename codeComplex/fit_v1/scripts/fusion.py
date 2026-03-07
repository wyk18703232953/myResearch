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

# 反向映射，用于从模型名称到文件夹类型
reverse_complexity_map = {
    'Constant': 'constant',
    'Linear': 'linear',
    'Quadratic': 'quadratic',
    'Cubic': 'cubic',
    'Logarithmic': 'logn',
    'N Log N': 'nlogn',
    'np': 'np'
}

# 定义标签顺序（按照用户要求）
true_labels_order = ['constant', 'logn', 'linear', 'nlogn', 'quadratic', 'cubic', 'np']
pred_labels_order = ['constant', 'logn', 'linear', 'nlogn', 'quadratic', 'cubic', 'np']

def get_best_model(analysis_report):
    """
    从分析报告中确定最佳拟合模型
    
    Args:
        analysis_report: 分析报告字典
    
    Returns:
        str: 最佳拟合模型名称
    """
    models = analysis_report.get('models', {})
    best_model = None
    best_r2 = -float('inf')
    
    for model_name, model_data in models.items():
        r2 = model_data.get('r2', -float('inf'))
        if r2 > best_r2:
            best_r2 = r2
            best_model = model_name
    
    return best_model

def calculate_accuracy(base_dir):
    """
    计算准确率
    
    Args:
        base_dir: 基础目录路径
    
    Returns:
        tuple: (总文件数, 正确预测数, 准确率, 详细统计, 混淆矩阵)
    """
    total_files = 0
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
    
    # 遍历所有子目录
    for root, dirs, files in os.walk(base_dir):
        for dir_name in dirs:
            if dir_name.startswith('results_'):
                # 提取正确标签
                parts = dir_name.split('_')
                if len(parts) >= 3:
                    correct_label = None
                    for part in parts:
                        if part in complexity_map:
                            correct_label = part
                            break
                    
                    if correct_label:
                        # 检查分析报告
                        report_path = os.path.join(root, dir_name, 'analysis_report.json')
                        if os.path.exists(report_path):
                            total_files += 1
                            detailed_stats[correct_label]['total'] += 1
                            
                            try:
                                with open(report_path, 'r') as f:
                                    report = json.load(f)
                                
                                best_model = get_best_model(report)
                                if best_model:
                                    predicted_label = reverse_complexity_map.get(best_model, None)
                                    if predicted_label == correct_label:
                                        correct_predictions += 1
                                        detailed_stats[correct_label]['correct'] += 1
                                    else:
                                        detailed_stats[correct_label]['incorrect'].append({
                                            'file': dir_name,
                                            'predicted': predicted_label
                                        })
                                    
                                    # 更新混淆矩阵
                                    if predicted_label:
                                        confusion_matrix[correct_label][predicted_label] += 1
                            except Exception as e:
                                print(f"处理 {report_path} 时出错: {e}")
    
    accuracy = correct_predictions / total_files if total_files > 0 else 0
    return total_files, correct_predictions, accuracy, detailed_stats, confusion_matrix

def generate_results(base_dir):
    """
    生成统计结果
    
    Args:
        base_dir: 基础目录路径
    """
    total_files, correct_predictions, accuracy, detailed_stats, confusion_matrix = calculate_accuracy(base_dir)
    
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
    ax.set_title('复杂度预测统计')
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
    output_dir = os.path.join(os.path.dirname(base_dir), 'results')
    os.makedirs(output_dir, exist_ok=True)
    
    plt.tight_layout()
    # plt.savefig(os.path.join(output_dir, 'accuracy_results.png'))
    print(f"\n统计图表已保存至: {os.path.join(output_dir, 'accuracy_results.png')}")
    
    # 生成混淆矩阵热力图
    generate_confusion_matrix(confusion_matrix, total_files, output_dir)
    
    # 保存详细统计数据
    with open(os.path.join(output_dir, 'detailed_stats.json'), 'w') as f:
        json.dump({
            'total_files': total_files,
            'correct_predictions': correct_predictions,
            'accuracy': accuracy,
            'detailed_stats': detailed_stats,
            'confusion_matrix': confusion_matrix
        }, f, indent=2)
    print(f"详细统计数据已保存至: {os.path.join(output_dir, 'detailed_stats.json')}")

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
    
    ax.set_title('混淆矩阵（百分比）')
    ax.set_xlabel('预测标签')
    ax.set_ylabel('真实标签')
    
    # 添加颜色条
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel('百分比', rotation=-90, va="bottom")
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'confusion_matrix.png'))
    print(f"混淆矩阵图表已保存至: {os.path.join(output_dir, 'confusion_matrix.png')}")
    
    # 保存混淆矩阵数据
    with open(os.path.join(output_dir, 'confusion_matrix.json'), 'w') as f:
        json.dump({
            'matrix': conf_matrix_percent.tolist(),
            'true_labels': true_labels_display,
            'pred_labels': pred_labels_display
        }, f, indent=2)
    print(f"混淆矩阵数据已保存至: {os.path.join(output_dir, 'confusion_matrix.json')}")

if __name__ == "__main__":
    base_dir = '/home/wuyankai/myResearch/codeComplex/fit_v1/filteredData'
    generate_results(base_dir)
