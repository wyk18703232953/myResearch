import json
import numpy as np

# 定义复杂度类型映射和层级顺序
# 按照时间复杂度从低到高的层级顺序
complexity_hierarchy = ['constant', 'logn', 'linear', 'nlogn', 'quadratic', 'cubic', 'np']

# 创建层级索引映射
hierarchy_index = {label: idx for idx, label in enumerate(complexity_hierarchy)}
number_of_classes = len(complexity_hierarchy)

def parse_fit_results(file_path):
    """
    解析fit结果文件
    
    Args:
        file_path: fit结果文件路径
    
    Returns:
        tuple: (真实标签列表, 预测标签列表)
    """
    true_labels = []
    pred_labels = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    data = json.loads(line)
                    true_label = data.get('answer', '')  # answer是真实标签
                    pred_label = data.get('complexity', '')  # complexity是预测标签
                    
                    # 验证标签有效性
                    if true_label in hierarchy_index and pred_label in hierarchy_index:
                        true_labels.append(true_label)
                        pred_labels.append(pred_label)
                    else:
                        print(f"跳过无效标签: true={true_label}, pred={pred_label}")
                        
                except json.JSONDecodeError as e:
                    print(f"JSON解析错误: {e}, 行内容: {line}")
    
    return true_labels, pred_labels

def calculate_hc_score(true_labels, pred_labels, w=None):
    """
    计算层级复杂度分数（HC-Score）
    
    Args:
        true_labels: 真实标签列表
        pred_labels: 预测标签列表
        w: 评分窗口大小，None表示使用原始HC公式
    
    Returns:
        float: HC分数
    """
    N = len(true_labels)
    total_score = 0
    
    for i in range(N):
        true_idx = hierarchy_index[true_labels[i]]
        pred_idx = hierarchy_index[pred_labels[i]]
        
        # 计算层级距离
        distance = abs(pred_idx - true_idx)
        
        if w is None:
            # 原始HC公式：HC(P,R) = (1/N) * Σ(1 - |pi - ri| / Number_of_class)
            score = 1 - (distance / number_of_classes)
        else:
            # 窗口化HC公式：HCw(P,R) = (1/N) * Σ max(0, 1 - |pi - ri| / w)
            if distance >= w:
                score = 0
            else:
                score = 1 - (distance / w)
        
        total_score += score
    
    hc_score = total_score / N if N > 0 else 0
    return hc_score

def calculate_detailed_hc_analysis(true_labels, pred_labels):
    """
    计算详细的HC分数分析
    
    Args:
        true_labels: 真实标签列表
        pred_labels: 预测标签列表
    
    Returns:
        dict: 包含各种HC分数和详细分析的字典
    """
    N = len(true_labels)
    
    # 计算不同窗口大小的HC分数
    hc_original = calculate_hc_score(true_labels, pred_labels, w=None)  # 原始HC
    hc_w1 = calculate_hc_score(true_labels, pred_labels, w=1)  # 窗口=1（仅完全正确得分）
    hc_w2 = calculate_hc_score(true_labels, pred_labels, w=2)  # 窗口=2
    hc_w3 = calculate_hc_score(true_labels, pred_labels, w=3)  # 窗口=3
    
    # 计算准确率（用于对比）
    accuracy = np.mean(np.array(true_labels) == np.array(pred_labels))
    
    # 分析距离分布
    distances = []
    for i in range(N):
        true_idx = hierarchy_index[true_labels[i]]
        pred_idx = hierarchy_index[pred_labels[i]]
        distances.append(abs(pred_idx - true_idx))
    
    distance_counts = {d: distances.count(d) for d in range(number_of_classes)}
    distance_percentages = {d: (count / N) * 100 for d, count in distance_counts.items()}
    
    # 分析每个类别的HC表现
    class_hc_scores = {}
    for label in complexity_hierarchy:
        # 筛选该类别为真实标签的样本
        mask = [tl == label for tl in true_labels]
        if sum(mask) > 0:
            class_true = [true_labels[i] for i in range(N) if mask[i]]
            class_pred = [pred_labels[i] for i in range(N) if mask[i]]
            class_hc_scores[label] = calculate_hc_score(class_true, class_pred, w=None)
    
    return {
        'total_samples': N,
        'accuracy': accuracy,
        'hc_original': hc_original,
        'hc_w1': hc_w1,
        'hc_w2': hc_w2,
        'hc_w3': hc_w3,
        'distance_distribution': distance_counts,
        'distance_percentages': distance_percentages,
        'class_hc_scores': class_hc_scores,
        'hierarchy_order': complexity_hierarchy
    }

def save_results_to_txt(results, output_file):
    """
    将结果保存到txt文件
    
    Args:
        results: 评估结果字典
        output_file: 输出文件路径
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("fit 代码复杂度预测 HC-Score 评估结果\n")
        f.write("=" * 70 + "\n\n")
        
        # 总体信息
        f.write("数据集信息:\n")
        f.write("-" * 40 + "\n")
        f.write(f"总样本数: {results['total_samples']}\n")
        f.write(f"复杂度层级顺序: {' -> '.join(results['hierarchy_order'])}\n")
        f.write(f"层级数量: {len(results['hierarchy_order'])}\n\n")
        
        # 传统指标
        f.write("传统评估指标:\n")
        f.write("-" * 40 + "\n")
        f.write(f"准确率 (Accuracy): {results['accuracy']:.4f}\n\n")
        
        # HC-Score指标
        f.write("层级复杂度分数 (HC-Score):\n")
        f.write("-" * 40 + "\n")
        f.write(f"HC (原始公式): {results['hc_original']:.4f}\n")
        f.write(f"HC1 (窗口=1): {results['hc_w1']:.4f}\n")
        f.write(f"HC2 (窗口=2): {results['hc_w2']:.4f}\n")
        f.write(f"HC3 (窗口=3): {results['hc_w3']:.4f}\n\n")
        
        # 距离分布分析
        f.write("预测距离分布:\n")
        f.write("-" * 40 + "\n")
        f.write("距离 | 样本数 | 百分比 | 含义\n")
        f.write("-" * 40 + "\n")
        for d in range(number_of_classes):
            count = results['distance_distribution'].get(d, 0)
            percentage = results['distance_percentages'].get(d, 0)
            meaning = "完全正确" if d == 0 else f"偏差{d}个层级"
            f.write(f"{d:>4} | {count:>6} | {percentage:>6.2f}% | {meaning}\n")
        f.write("\n")
        
        # 各类别HC表现
        f.write("各类别HC分数分析:\n")
        f.write("-" * 40 + "\n")
        for label in results['hierarchy_order']:
            if label in results['class_hc_scores']:
                hc_score = results['class_hc_scores'][label]
                f.write(f"{label:>10}: HC = {hc_score:.4f}\n")
        f.write("\n")
        
        # 指标解释
        f.write("HC-Score指标解释:\n")
        f.write("-" * 40 + "\n")
        f.write("1. HC (原始公式): 对所有预测偏差进行线性惩罚\n")
        f.write("   公式: HC(P,R) = (1/N) * Σ(1 - |pi - ri| / Number_of_class)\n")
        f.write("   特点: 对相邻层级偏差进行轻微惩罚\n\n")
        
        f.write("2. HC1 (窗口=1): 仅完全正确的预测得分\n")
        f.write("   公式: HCw(P,R) = (1/N) * Σ max(0, 1 - |pi - ri| / w)\n")
        f.write("   特点: 等同于准确率，但概念不同\n\n")
        
        f.write("3. HC2 (窗口=2): 允许偏差1个层级的预测得分\n")
        f.write("   特点: 对相邻层级偏差宽容，对更大偏差严格惩罚\n\n")
        
        f.write("4. HC3 (窗口=3): 允许偏差2个层级的预测得分\n")
        f.write("   特点: 对中等偏差宽容，对极端偏差严格惩罚\n\n")
        
        f.write("层级复杂度分数的优势:\n")
        f.write("- 考虑了复杂度预测任务的层级特性\n")
        f.write("- 对相邻层级的预测偏差进行合理惩罚\n")
        f.write("- 通过窗口机制实现灵活的评估策略\n")
        f.write("- 比传统准确率更能反映模型的真实推理能力\n")
        
        f.write("\n" + "=" * 70 + "\n")
        f.write("评估完成！")

def main():
    """主函数"""
    # 文件路径
    input_file = '/home/wuyankai/myResearch/codeComplex/fit_v2/results/converted_stats.txt'
    output_file = '/home/wuyankai/myResearch/codeComplex/fit_v2/results/fit_v2_hc_scores.txt'
    
    print("正在解析fit结果文件...")
    true_labels, pred_labels = parse_fit_results(input_file)
    print(f"成功解析 {len(true_labels)} 个结果")
    
    print("正在计算HC-Score评估指标...")
    results = calculate_detailed_hc_analysis(true_labels, pred_labels)
    
    print("正在保存结果到文件...")
    save_results_to_txt(results, output_file)
    
    print(f"HC-Score评估结果已保存至: {output_file}")
    
    # 在控制台输出主要结果
    print("\n主要评估指标:")
    print(f"准确率: {results['accuracy']:.4f}")
    print(f"HC (原始): {results['hc_original']:.4f}")
    print(f"HC1 (窗口=1): {results['hc_w1']:.4f}")
    print(f"HC2 (窗口=2): {results['hc_w2']:.4f}")
    print(f"HC3 (窗口=3): {results['hc_w3']:.4f}")

if __name__ == "__main__":
    main()