import os
import json
import pandas as pd
import subprocess
from openai import OpenAI

# 初始化OpenAI客户端
client = OpenAI(
    api_key="GnZpLRUqXACfasNtdRzM:DOmdLvpitzquFcnIXimk", 
    base_url='https://spark-api-open.xf-yun.com/v1'  # 指向讯飞星火的请求地址
)


def read_dataset():
    """读取mbppplus数据集"""
    dataset_path = "d:/MyResearch/mbpp_plus/data/mbpp_plus_data.parquet"
    df = pd.read_parquet(dataset_path)
    return df


def extract_function_name(code):
    """从代码中提取函数名"""
    lines = code.split('\n')
    for line in lines:
        if line.strip().startswith('def '):
            # 提取函数名
            func_name = line.split('def ')[1].split('(')[0]
            return func_name
    return None


def generate_code(prompt, expected_func_name):
    """使用LLM生成代码"""
    # 构建提示词，确保生成的函数名与预期一致
    enhanced_prompt = f"""
    根据以下需求，编写一个Python函数，函数名必须为{expected_func_name}：
    
    {prompt}
    
    请只返回函数代码，不要包含其他解释或测试代码，不要使用Markdown格式。
    """
    
    try:
        completion = client.chat.completions.create(
            model='lite',  # 指定请求的版本
            messages=[
                {
                    "role": "user",
                    "content": enhanced_prompt
                }
            ]
        )
        
        generated_code = completion.choices[0].message.content
        
        # 清理生成的代码，去除Markdown格式和额外解释
        # 去除可能的Markdown代码块标记
        generated_code = generated_code.replace('```python', '').replace('```', '')
        
        # 只保留函数定义部分
        lines = generated_code.split('\n')
        func_lines = []
        in_func = False
        for line in lines:
            if line.strip().startswith('def '):
                in_func = True
            if in_func:
                func_lines.append(line)
                # 检查函数是否结束
                if line.strip() and not line.startswith(' ') and not line.startswith('\t') and len(func_lines) > 1:
                    # 如果不是缩进行且不是函数定义行，说明函数结束
                    break
        
        cleaned_code = '\n'.join(func_lines)
        return cleaned_code
    except Exception as e:
        print(f"代码生成失败: {e}")
        return None


def create_test_file(task_id, generated_code, test_content):
    """创建测试文件"""
    # 创建子文件夹
    folder_path = f"d:/MyResearch/mbpp_plus/myidea/{task_id}"
    os.makedirs(folder_path, exist_ok=True)
    
    # 创建test.py文件
    test_file_path = os.path.join(folder_path, "test.py")
    with open(test_file_path, 'w', encoding='utf-8') as f:
        f.write(generated_code)
        f.write('\n\n')
        f.write(test_content)
    
    return test_file_path


def run_test(test_file_path):
    """运行测试文件"""
    try:
        result = subprocess.run(
            ["python", test_file_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        # 判断测试结果
        if result.returncode == 0 and not result.stderr:
            return True  # 成功
        else:
            print(f"测试失败，错误信息：{result.stderr}")
            return False  # 失败
    except Exception as e:
        print(f"测试执行失败: {e}")
        return False


def main():
    """主函数"""
    print("开始执行MBPPPlus数据处理流程...")
    
    # 1. 读取数据集
    print("1. 读取数据集...")
    df = read_dataset()
    print(f"共读取到 {len(df)} 个数据条目")
    
    # 2. 只处理第一个任务，测试修改是否有效
    print("2. 处理单个任务测试...")
    
    row = df.iloc[0]
    task_id = row['task_id']
    prompt = row['prompt']
    original_code = row['code']
    test_content = row['test']
    
    print(f"\n处理任务 {task_id}...")
    
    # 提取预期函数名
    expected_func_name = extract_function_name(original_code)
    if not expected_func_name:
        print(f"警告：无法从原代码中提取函数名，跳过任务 {task_id}")
        return
    
    # 生成代码
    print(f"   生成代码，预期函数名：{expected_func_name}...")
    generated_code = generate_code(prompt, expected_func_name)
    if not generated_code:
        print(f"   代码生成失败，跳过任务 {task_id}")
        return
    
    print(f"   生成的代码：\n{generated_code}")
    
    # 创建测试文件
    print(f"   创建测试文件...")
    test_file_path = create_test_file(task_id, generated_code, test_content)
    
    # 运行测试
    print(f"   运行测试...")
    test_result = run_test(test_file_path)
    
    print(f"   测试结果：{'成功' if test_result else '失败'}")


if __name__ == "__main__":
    main()