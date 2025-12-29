import json
from collections import defaultdict
import os

INPUT_FILE = r"d:\MyResearch\codeComplex\results\LLM\ast_llm_results.json"
OUTPUT_DIR = r"d:\MyResearch\codeComplex\results\LLM"

def analyze_accuracy():
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    total = data.get('summary', {}).get('total', 0)
    correct = data.get('summary', {}).get('correct', 0)
    failed = data.get('summary', {}).get('failed', 0)
    overall_accuracy = data.get('summary', {}).get('accuracy', 0)
    
    records = data.get('detailed_records', [])
    
    complexity_stats = defaultdict(lambda: {
        'total': 0,
        'correct': 0,
        'failed': 0,
        'accuracy': 0.0,
        'predictions': defaultdict(int)
    })
    
    for record in records:
        expected = record.get('expected_complexity', 'unknown')
        is_match = record.get('is_match', False)
        model_output = record.get('model_raw_output', 'unknown')
        
        complexity_stats[expected]['total'] += 1
        complexity_stats[expected]['predictions'][model_output] += 1
        
        if is_match:
            complexity_stats[expected]['correct'] += 1
        else:
            complexity_stats[expected]['failed'] += 1
    
    for complexity in complexity_stats:
        stats = complexity_stats[complexity]
        if stats['total'] > 0:
            stats['accuracy'] = (stats['correct'] / stats['total']) * 100
    
    report = {
        'overall': {
            'total': total,
            'correct': correct,
            'failed': failed,
            'accuracy': overall_accuracy
        },
        'by_complexity': {}
    }
    
    for complexity in sorted(complexity_stats.keys()):
        stats = complexity_stats[complexity]
        report['by_complexity'][complexity] = {
            'total': stats['total'],
            'correct': stats['correct'],
            'failed': stats['failed'],
            'accuracy': round(stats['accuracy'], 2),
            'predictions': dict(stats['predictions'])
        }
    
    return report

def format_report(report):
    lines = []
    lines.append("=" * 80)
    lines.append("AST LLM 复杂度识别准确率分析报告")
    lines.append("=" * 80)
    lines.append("")
    
    lines.append("总体统计:")
    lines.append("-" * 40)
    lines.append(f"总样本数: {report['overall']['total']}")
    lines.append(f"正确数: {report['overall']['correct']}")
    lines.append(f"错误数: {report['overall']['failed']}")
    lines.append(f"准确率: {report['overall']['accuracy']:.2f}%")
    lines.append("")
    
    lines.append("按复杂度分类统计:")
    lines.append("-" * 40)
    lines.append("")
    
    for complexity in sorted(report['by_complexity'].keys()):
        stats = report['by_complexity'][complexity]
        lines.append(f"复杂度: {complexity}")
        lines.append(f"  总样本数: {stats['total']}")
        lines.append(f"  正确数: {stats['correct']}")
        lines.append(f"  错误数: {stats['failed']}")
        lines.append(f"  准确率: {stats['accuracy']:.2f}%")
        lines.append(f"  预测分布:")
        
        for pred_type in sorted(stats['predictions'].keys()):
            count = stats['predictions'][pred_type]
            percentage = (count / stats['total']) * 100 if stats['total'] > 0 else 0
            lines.append(f"    {pred_type}: {count} ({percentage:.2f}%)")
        lines.append("")
    
    lines.append("=" * 80)
    
    return "\n".join(lines)

def main():
    print("开始分析 ast_llm_results.json...")
    
    report = analyze_accuracy()
    
    report_text = format_report(report)
    
    print(report_text)
    
    output_file = os.path.join(OUTPUT_DIR, "ast_accuracy_summary.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report_text)
    
    print(f"\n报告已保存到: {output_file}")
    
    json_output_file = os.path.join(OUTPUT_DIR, "ast_accuracy_summary.json")
    with open(json_output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"JSON报告已保存到: {json_output_file}")

if __name__ == "__main__":
    main()
