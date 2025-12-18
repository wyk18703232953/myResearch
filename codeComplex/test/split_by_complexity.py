import json
import os

def split_jsonl_by_complexity(input_file, output_dir):
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 从输入文件名提取语言类型
    filename = os.path.basename(input_file)
    if 'python' in filename.lower():
        language_prefix = 'python'
    elif 'java' in filename.lower():
        language_prefix = 'java'
    else:
        language_prefix = 'unknown'
    
    # 用于存储不同complexity的JSON对象
    complexity_groups = {}
    
    # 读取输入文件
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            # 解析JSON对象
            try:
                data = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"解析错误: {e}, 行内容: {line}")
                continue
            
            # 获取complexity字段
            complexity = data.get('complexity', 'unknown')
            
            # 将数据添加到对应的分组
            if complexity not in complexity_groups:
                complexity_groups[complexity] = []
            complexity_groups[complexity].append(data)
    
    # 将每个分组写入对应的文件
    for complexity, items in complexity_groups.items():
        output_file = os.path.join(output_dir, f'{language_prefix}_complexity_{complexity}.jsonl')
        with open(output_file, 'w', encoding='utf-8') as f:
            for item in items:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
        print(f"已保存 {len(items)} 条记录到 {output_file}")

if __name__ == "__main__":
    output_dir = 'd:/MyResearch/codeComplex/data/'
    
    # 处理Python文件
    print("开始处理Python文件...")
    python_file = 'd:/MyResearch/codeComplex/data/python_data.jsonl'
    split_jsonl_by_complexity(python_file, output_dir)
    
    # 处理Java文件
    print("\n开始处理Java文件...")
    java_file = 'd:/MyResearch/codeComplex/data/java_data.jsonl'
    split_jsonl_by_complexity(java_file, output_dir)