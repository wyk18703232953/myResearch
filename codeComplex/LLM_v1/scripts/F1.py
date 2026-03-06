import json
import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score, classification_report

# 定义复杂度类型映射和标签顺序
complexity_map = {
    'constant': 'Constant',
    'linear': 'Linear',
    'quadratic': 'Quadratic',
    'cubic': 'Cubic',
    'logn': 'Logarithmic',
    'nlogn': 'N Log N',
    'np': 'np'
}

# 标签顺序
labels_order = ['constant', 'logn', 'linear', 'nlogn', 'quadratic', 'cubic', 'np']
label_to_index = {label: idx for idx, label in enumerate(labels_order)}

def parse_gpt4_results(file_path):
    """
    解析GPT-4结果文件
    
    Args:
        file_path: GPT-4结果文件路径
    
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
                    if true_label in complexity_map and pred_label in complexity_map:
                        true_labels.append(true_label)
                        pred_labels.append(pred_label)
                    else:
                        print(f"跳过无效标签: true={true_label}, pred={pred_label}")
                        
                except json.JSONDecodeError as e:
                    print(f"JSON解析错误: {e}, 行内容: {line}")
    
    return true_labels, pred_labels

def calculate_f1_scores(true_labels, pred_labels):
    """
    计算F1分数和其他评估指标
    
    Args:
        true_labels: 真实标签列表
        pred_labels: 预测标签列表
    
    Returns:
        dict: 包含各种评估指标的字典
    """
    # 转换为数值索引
    y_true = [label_to_index[label] for label in true_labels]
    y_pred = [label_to_index[label] for label in pred_labels]
    
    # 计算宏平均F1分数
    macro_f1 = f1_score(y_true, y_pred, average='macro')
    
    # 计算微平均F1分数
    micro_f1 = f1_score(y_true, y_pred, average='micro')
    
    # 计算加权平均F1分数
    weighted_f1 = f1_score(y_true, y_pred, average='weighted')
    
    # 计算每个类别的F1分数
    per_class_f1 = f1_score(y_true, y_pred, average=None, labels=range(len(labels_order)))
    
    # 计算精确率和召回率
    precision = precision_score(y_true, y_pred, average=None, labels=range(len(labels_order)))
    recall = recall_score(y_true, y_pred, average=None, labels=range(len(labels_order)))
    
    # 计算宏平均精确率和召回率
    macro_precision = precision_score(y_true, y_pred, average='macro')
    macro_recall = recall_score(y_true, y_pred, average='macro')
    
    # 计算微平均精确率和召回率
    micro_precision = precision_score(y_true, y_pred, average='micro')
    micro_recall = recall_score(y_true, y_pred, average='micro')
    
    # 计算加权平均精确率和召回率
    weighted_precision = precision_score(y_true, y_pred, average='weighted')
    weighted_recall = recall_score(y_true, y_pred, average='weighted')
    
    # 计算准确率
    accuracy = np.mean(np.array(y_true) == np.array(y_pred))
    
    # 生成详细的分类报告
    class_report = classification_report(y_true, y_pred, 
                                        target_names=labels_order, 
                                        labels=range(len(labels_order)),
                                        output_dict=True)
    
    return {
        'accuracy': accuracy,
        'macro_f1': macro_f1,
        'micro_f1': micro_f1,
        'weighted_f1': weighted_f1,
        'macro_precision': macro_precision,
        'macro_recall': macro_recall,
        'micro_precision': micro_precision,
        'micro_recall': micro_recall,
        'weighted_precision': weighted_precision,
        'weighted_recall': weighted_recall,
        'per_class_f1': dict(zip(labels_order, per_class_f1)),
        'per_class_precision': dict(zip(labels_order, precision)),
        'per_class_recall': dict(zip(labels_order, recall)),
        'classification_report': class_report
    }

def save_results_to_txt(results, output_file):
    """
    将结果保存到txt文件
    
    Args:
        results: 评估结果字典
        output_file: 输出文件路径
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("GPT-4 代码复杂度预测 F1 分数评估结果\n")
        f.write("=" * 50 + "\n\n")
        
        # 总体指标
        f.write("总体评估指标:\n")
        f.write("-" * 30 + "\n")
        f.write(f"准确率 (Accuracy): {results['accuracy']:.4f}\n")
        f.write(f"宏平均F1分数 (Macro F1): {results['macro_f1']:.4f}\n")
        f.write(f"微平均F1分数 (Micro F1): {results['micro_f1']:.4f}\n")
        f.write(f"加权平均F1分数 (Weighted F1): {results['weighted_f1']:.4f}\n\n")
        
        f.write(f"宏平均精确率 (Macro Precision): {results['macro_precision']:.4f}\n")
        f.write(f"宏平均召回率 (Macro Recall): {results['macro_recall']:.4f}\n")
        f.write(f"微平均精确率 (Micro Precision): {results['micro_precision']:.4f}\n")
        f.write(f"微平均召回率 (Micro Recall): {results['micro_recall']:.4f}\n")
        f.write(f"加权平均精确率 (Weighted Precision): {results['weighted_precision']:.4f}\n")
        f.write(f"加权平均召回率 (Weighted Recall): {results['weighted_recall']:.4f}\n\n")
        
        # 每个类别的F1分数
        f.write("每个类别的F1分数:\n")
        f.write("-" * 30 + "\n")
        for label in labels_order:
            f1 = results['per_class_f1'][label]
            precision = results['per_class_precision'][label]
            recall = results['per_class_recall'][label]
            f.write(f"{label:>10}: F1={f1:.4f}, Precision={precision:.4f}, Recall={recall:.4f}\n")
        f.write("\n")
        
        # 详细的分类报告
        f.write("详细分类报告:\n")
        f.write("-" * 30 + "\n")
        report = results['classification_report']
        
        # 表头
        f.write(f"{'类别':<10} {'精确率':<10} {'召回率':<10} {'F1分数':<10} {'支持数':<10}\n")
        f.write("-" * 50 + "\n")
        
        # 每个类别的指标
        for label in labels_order:
            if label in report:
                metrics = report[label]
                f.write(f"{label:<10} {metrics['precision']:.4f}     {metrics['recall']:.4f}     {metrics['f1-score']:.4f}     {metrics['support']:<10}\n")
        
        # 平均值
        f.write("-" * 50 + "\n")
        f.write(f"{'macro avg':<10} {report['macro avg']['precision']:.4f}     {report['macro avg']['recall']:.4f}     {report['macro avg']['f1-score']:.4f}     {report['macro avg']['support']:<10}\n")
        f.write(f"{'weighted avg':<10} {report['weighted avg']['precision']:.4f}     {report['weighted avg']['recall']:.4f}     {report['weighted avg']['f1-score']:.4f}     {report['weighted avg']['support']:<10}\n")
        
        f.write("\n" + "=" * 50 + "\n")
        f.write("评估完成！")

def main():
    """主函数"""
    # 文件路径
    input_file = '/home/wuyankai/myResearch/codeComplex/LLM_v1/results/gpt4-python-codecomplex-simple.txt'
    output_file = '/home/wuyankai/myResearch/codeComplex/LLM_v1/results/gpt4_f1_scores.txt'
    
    print("正在解析GPT-4结果文件...")
    true_labels, pred_labels = parse_gpt4_results(input_file)
    print(f"成功解析 {len(true_labels)} 个结果")
    
    print("正在计算F1分数和其他评估指标...")
    results = calculate_f1_scores(true_labels, pred_labels)
    
    print("正在保存结果到文件...")
    save_results_to_txt(results, output_file)
    
    print(f"F1分数评估结果已保存至: {output_file}")
    
    # 在控制台输出主要结果
    print("\n主要评估指标:")
    print(f"准确率: {results['accuracy']:.4f}")
    print(f"宏平均F1分数: {results['macro_f1']:.4f}")
    print(f"微平均F1分数: {results['micro_f1']:.4f}")
    print(f"加权平均F1分数: {results['weighted_f1']:.4f}")

if __name__ == "__main__":
    main()