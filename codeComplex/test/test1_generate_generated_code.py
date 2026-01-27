import os
import time
from openai import OpenAI

SOURCE_DIR = r"/home/wuyankai/myResearch/codeComplex/data/onlyCode/python/"
OUTPUT_DIR = r"/home/wuyankai/myResearch/codeComplex/data/filteredData/python/"

def call_large_model(original_code, api_key=None, base_url=None):
    if api_key is None:
        api_key = "sk-3sNQAO5ydpVp29WWoCqvM7Ajqzd1I5WKOpe29cpoT3DoMrZe"
    if base_url is None:
        base_url = "https://yunwu.ai/v1"
    
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    system_prompt = "你是一位算法专家。将Python程序转换为【确定性】【可规模化】【可重复实验】的程序，用于时间复杂度分析。"
    user_prompt = f"""请将以下 Python 程序重构为一个【确定性】【可规模化】【可重复实验】的程序。
### 重构目标
将原始“依赖 input() 的交互式程序”
转换为一个不依赖任何外部输入的程序，用于时间复杂度实验。

### 必须完成的任务
1. **完全移除** input()、sys.stdin、readline 等所有输入方式
2. 定义 `main(n)` 函数，其中：
   - `n` 表示程序的“输入规模”
   - 所有测试数据必须由 `n` **确定性生成**
3. 自动识别原程序的输入结构，例如：
   - 单个整数
   - 多个整数
   - 整数列表 / 字符串
   - 二维矩阵
   - 多测试用例（如 T 组数据）
4. 根据输入结构，将 `n` 映射为合理的规模含义，例如：
   - 列表长度
   - 矩阵行列规模
   - 测试用例数量
5. 保持原程序的核心算法逻辑不变

### 严格禁止
- ❌ 使用 `random`、`numpy.random`、`secrets`
- ❌ 使用当前时间、系统状态、网络请求
- ❌ 使用任何非确定性行为
- ❌ 引入新的第三方库

### 数据生成要求
- 测试数据必须是**完全确定性的**
- 相同的 n，多次运行结果必须一致
- 优先使用：
  - `range`
  - 列表推导
  - 简单算术构造（如 i, i+1, i%k, i//2）

### 输出要求
- 仅输出完整、可直接运行的 Python 代码
- 必须包含：
  - `def main(n):`
  - `if __name__ == "__main__":` 示例调用
- 不输出任何解释、注释说明、Markdown 或自然语言文本

### 原始代码
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
    # 检查源目录是否包含.py文件，如果有则直接处理
    python_files = sorted([f for f in os.listdir(source_dir) if f.endswith('.py') and not os.path.isdir(os.path.join(source_dir, f))])
    
    if python_files:
        print(f"\n处理目录: {os.path.basename(source_dir)}")
        total_files = len(python_files)
        success_count = 0
        
        for i, filename in enumerate(python_files, 1):
            source_path = os.path.join(source_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            print(f"[{i}/{total_files}]", end=" ")
            if process_file(source_path, output_path, force_regenerate):
                success_count += 1
            
            time.sleep(0.1)
        
        print(f"\n目录 {os.path.basename(source_dir)} 完成: {success_count}/{total_files} 文件成功")
    
    # 处理子目录（保留原功能）
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
