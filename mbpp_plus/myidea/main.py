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

#读取mbppplus数据集
def read_dataset():
    """读取mbppplus数据集"""
    dataset_path = "d:/MyResearch/mbpp_plus/data/mbpp_plus_data.parquet"
    df = pd.read_parquet(dataset_path)
    return df

#提取函数名，只能生成这个名字的函数。
def extract_function_name(code):
    """从代码中提取函数名"""
    lines = code.split('\n')
    for line in lines:
        if line.strip().startswith('def '):
            # 提取函数名
            func_name = line.split('def ')[1].split('(')[0]
            return func_name
    return None

#生成代码
def generate_code(prompt, expected_func_name):
    """使用LLM生成代码"""
    # 构建提示词，确保生成的函数名与预期一致
    enhanced_prompt = f"""
    根据以下需求，编写一个Python函数，函数名必须为{expected_func_name}：
    
    {prompt}
    
    请返回完整的函数代码，包括必要的import语句，不要包含其他解释或测试代码，不要使用Markdown格式。
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
        
        # 保留import语句和函数定义
        lines = generated_code.split('\n')
        cleaned_lines = []
        in_code = False
        
        for line in lines:
            stripped_line = line.strip()
            
            # 保留import语句
            if stripped_line.startswith('import ') or stripped_line.startswith('from '):
                cleaned_lines.append(line)
                in_code = True
            # 保留函数定义和函数体
            elif stripped_line.startswith('def '):
                cleaned_lines.append(line)
                in_code = True
            # 保留函数体内的代码
            elif in_code and (line.startswith(' ') or line.startswith('\t') or stripped_line == ''):
                cleaned_lines.append(line)
            # 遇到非缩进的非import语句且不在函数体内，停止保留
            elif in_code and stripped_line and not (line.startswith(' ') or line.startswith('\t')):
                # 函数结束，停止处理
                break
        
        cleaned_code = '\n'.join(cleaned_lines)
        return cleaned_code
    except Exception as e:
        print(f"代码生成失败: {e}")
        return None

#利用数据集中的测试代码生成测试文件
def create_test_file(task_id, generated_code, test_content):
    """创建测试文件"""
    # 创建子文件夹
    folder_path = f"d:/MyResearch/mbpp_plus/myidea/resource/{task_id}"
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
            return False  # 失败
    except Exception as e:
        print(f"测试执行失败: {e}")
        return False

"""生成测试报告"""
def generate_report(results):
    """生成测试报告"""
    total = len(results)
    success = sum(1 for r in results.values() if r)
    fail = total - success
    accuracy = success / total if total > 0 else 0
    
    report = {
        "total": total,
        "success": success,
        "fail": fail,
        "accuracy": round(accuracy, 4)
    }
    
    # 保存报告
    report_path = "d:/MyResearch/mbpp_plus/myidea/test_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    return report


def main():
    """主函数"""
    print("开始执行MBPPPlus数据处理流程...")
    
    # 1. 读取数据集
    print("1. 读取数据集...")
    df = read_dataset()
    print(f"共读取到 {len(df)} 个数据条目")
    
    # 2. 处理每个数据条目
    print("2. 处理数据条目...")
    results = {}
    
    # 处理所有数据条目
    for index, row in df.iterrows():
        task_id = row['task_id']
        prompt = row['prompt']
        original_code = row['code']
        test_content = row['test']
        
        print(f"\n处理任务 {task_id}...")
        
        # 提取预期函数名
        expected_func_name = extract_function_name(original_code)
        if not expected_func_name:
            print(f"警告：无法从原代码中提取函数名，跳过任务 {task_id}")
            results[task_id] = False
            continue
        
        # 生成代码
        print(f"   生成代码，预期函数名：{expected_func_name}...")
        generated_code = generate_code(prompt, expected_func_name)
        if not generated_code:
            print(f"   代码生成失败，跳过任务 {task_id}")
            results[task_id] = False
            continue
        
        # 创建测试文件
        print(f"   创建测试文件...")
        test_file_path = create_test_file(task_id, generated_code, test_content)
        
        # 运行测试
        print(f"   运行测试...")
        test_result = run_test(test_file_path)
        results[task_id] = test_result
        
        print(f"   测试结果：{'成功' if test_result else '失败'}")
        break
    
    # 3. 生成报告
    print("\n3. 生成测试报告...")
    report = generate_report(results)
    
    # 4. 输出报告
    print("\n测试报告：")
    print(f"总数据条目数量：{report['total']}")
    print(f"成功数量：{report['success']}")
    print(f"失败数量：{report['fail']}")
    print(f"正确率：{report['accuracy']:.2%}")
    
    print("\nMBPPPlus数据处理流程执行完成！")


if __name__ == "__main__":
    main()