import os
import time
from openai import OpenAI

SOURCE_DIR = r"d:\MyResearch\codeComplex\data\onlyCode\python"
OUTPUT_DIR = r"d:\MyResearch\codeComplex\data\filteredData\python"

def call_large_model(original_code, api_key=None, base_url=None):
    if api_key is None:
        api_key = "sk-3sNQAO5ydpVp29WWoCqvM7Ajqzd1I5WKOpe29cpoT3DoMrZe"
    if base_url is None:
        base_url = "https://yunwu.ai/v1"
    
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    system_prompt = "你是一位算法专家。将Python程序转换为无input()、可参数化规模n的程序。"
    user_prompt = f"""请将以下Python程序转换为一个无input()、包含 main(n) 函数的程序。
    
    要求：
    1. 移除 input()。
    2. 函数 main(n) 封装逻辑，n为规模。
    3. 根据 n 生成测试数据。
    4. 仅输出代码。
    
    原始代码：
    ```python
    {original_code}
    ```
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-5.1", 
            temperature=0.0,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        output = response.choices[0].message.content.strip()
        if output.startswith('```python'): output = output[9:]
        if output.endswith('```'): output = output[:-3]
        return output.strip()
    except Exception as e:
        raise Exception(f"API调用失败: {e}")

def process_file(source_path, output_path, force_regenerate=False):
    if os.path.exists(output_path) and not force_regenerate:
        print(f"  跳过 (已存在): {os.path.basename(output_path)}")
        return True
    
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            original_code = f.read()
        
        print(f"  处理中: {os.path.basename(source_path)}")
        generated_code = call_large_model(original_code)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(generated_code)
        
        print(f"  完成: {os.path.basename(output_path)}")
        return True
    except Exception as e:
        print(f"  错误: {os.path.basename(source_path)} - {e}")
        return False

def process_directory(source_dir, output_dir, force_regenerate=False):
    subdirs = [d for d in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, d))]
    
    for subdir in subdirs:
        source_subdir = os.path.join(source_dir, subdir)
        output_subdir = os.path.join(output_dir, subdir)
        os.makedirs(output_subdir, exist_ok=True)
        
        print(f"\n处理目录: {subdir}")
        
        python_files = sorted([f for f in os.listdir(source_subdir) if f.endswith('.py')])
        total_files = len(python_files)
        success_count = 0
        
        for i, filename in enumerate(python_files, 1):
            source_path = os.path.join(source_subdir, filename)
            output_path = os.path.join(output_subdir, filename)
            
            print(f"[{i}/{total_files}]", end=" ")
            if process_file(source_path, output_path, force_regenerate):
                success_count += 1
            
            time.sleep(0.1)
        
        print(f"\n目录 {subdir} 完成: {success_count}/{total_files} 文件成功")

def main():
    force_regenerate = False
    
    print("=" * 60)
    print("代码生成工具")
    print(f"源目录: {SOURCE_DIR}")
    print(f"输出目录: {OUTPUT_DIR}")
    print(f"强制重新生成: {force_regenerate}")
    print("=" * 60)
    
    if not os.path.exists(SOURCE_DIR):
        print(f"错误: 源目录不存在: {SOURCE_DIR}")
        return
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    process_directory(SOURCE_DIR, OUTPUT_DIR, force_regenerate)
    
    print("\n" + "=" * 60)
    print("所有处理完成!")
    print("=" * 60)

if __name__ == "__main__":
    main()
