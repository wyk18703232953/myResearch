from openai import OpenAI
import os
import re
import json

# 大模型调用函数，参考LLM.py的调用规则
def clean_code_with_llm(src, api_key=None, base_url=None):
    """
    使用大模型清洗代码，去除注释和死代码
    
    参数:
    src (str): 源代码
    api_key (str, optional): OpenAI API密钥，如果不提供则使用默认密钥
    base_url (str, optional): API基础URL，如果不提供则使用默认URL
    
    返回:
    str: 清洗后的代码
    """
    # 设置默认API参数
    if api_key is None:
        api_key = "sk-3sNQAO5ydpVp29WWoCqvM7Ajqzd1I5WKOpe29cpoT3DoMrZe"
    if base_url is None:
        base_url = "https://yunwu.ai/v1"
    
    # 创建OpenAI客户端
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    # 定义提示词，要求模型清洗代码
    system_prompt = """你是一位专业的Python代码清洗专家。
    你的任务是：
    1. 去除代码中的所有注释，包括单行注释(#)和多行注释(三引号)
    2. 去除死代码，包括永远不会执行的分支、未使用的变量和函数
    3. 保留代码的原始功能和逻辑
    4. 保持代码的可读性和格式
    5. 只返回清洗后的代码，不要输出任何解释或额外信息"""
    
    user_prompt = f"""请清洗以下Python代码，去除所有注释和死代码，只返回清洗后的代码：
    ```
    {src}
    ```
    
    请严格按照要求，只返回清洗后的代码，不要添加任何其他内容！"""
    
    try:
        # 调用大模型API
        response = client.chat.completions.create(
            model="gpt-5.1",
            temperature=0.0,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            stream=False
        )
        
        # 提取模型原始回复
        cleaned_code = response.choices[0].message.content.strip()
        
        # 移除可能的代码块标记
        cleaned_code = re.sub(r'^```python\s*', '', cleaned_code, flags=re.MULTILINE)
        cleaned_code = re.sub(r'^```\s*', '', cleaned_code, flags=re.MULTILINE)
        cleaned_code = re.sub(r'\s*```$', '', cleaned_code, flags=re.MULTILINE)
        
        return cleaned_code
        
    except Exception as e:
        error_msg = str(e)
        print(f"清洗代码时出错: {error_msg}")
        return src  # 出错时返回原始代码

# 数据清洗主函数
def clean_dataset(input_file, output_file, max_items=None):
    """
    清洗JSONL数据集，去除注释和死代码
    
    参数:
    input_file (str): 输入JSONL文件路径
    output_file (str): 输出JSONL文件路径
    max_items (int, optional): 最大处理项目数，如果为None则处理所有项目
    """
    # 读取输入文件
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    # 限制处理数量
    if max_items is not None:
        lines = lines[:max_items]
    
    # 处理每个样本
    cleaned_samples = []
    total = len(lines)
    
    print(f"开始清洗数据集，共 {total} 个样本")
    
    for i, line in enumerate(lines):
        try:
            # 解析JSON
            sample = json.loads(line)
            src = sample.get('src', '')
            
            if not src:
                continue
            
            # 清洗代码
            print(f"处理样本 {i+1}/{total}")
            cleaned_src = clean_code_with_llm(src)
            
            # 更新样本
            sample['src'] = cleaned_src
            cleaned_samples.append(sample)
            
            # 每处理10个样本保存一次
            if (i+1) % 10 == 0:
                print(f"已处理 {i+1} 个样本")
                
        except json.JSONDecodeError:
            print(f"第 {i+1} 行格式错误，跳过")
            continue
        except Exception as e:
            print(f"处理第 {i+1} 个样本时出错: {e}")
            continue
    
    # 保存清洗后的数据集
    with open(output_file, 'w', encoding='utf-8') as f:
        for sample in cleaned_samples:
            f.write(json.dumps(sample, ensure_ascii=False) + '\n')
    
    print(f"清洗完成！共处理 {len(cleaned_samples)} 个样本")
    print(f"清洗后的数据集已保存到 {output_file}")

# 示例用法
if __name__ == "__main__":
    input_file = r"d:\MyResearch\codeComplex\data\python_data.jsonl"
    output_file = r"d:\MyResearch\codeComplex\data\python_data_cleaned.jsonl"
    
    # 先测试10个样本
    clean_dataset(input_file, output_file, max_items=10000)