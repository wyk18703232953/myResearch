from data import write_jsonl, read_problems
from openai import OpenAI
import os

problems = read_problems()
def generate_one_completion(problem):
    client = OpenAI(api_key="sk-glL4mhF8GCov9dZiCJLIQ64OvlUpPa2qjLCpnV6zKz4byxXE", base_url="https://yunwu.ai/v1")

    response = client.chat.completions.create(
        # model="gpt-4.1-mini-2025-04-14",#0.4 1.6
        # model="gpt-4o-mini", #0.15 0.6
        # model="o1-pro-all", 
        model="gpt-5-nano-2025-08-07",
        temperature=0.0,
        messages = [
    {
        "role": "system",
        "content": """You are an expert C++ developer specializing in competitive programming and algorithm optimization. Your code must meet these strict requirements:

        1. Strict compliance with C++20 standard
        2. Optimal time/space complexity for the given problem
        3. Robust error handling and edge case coverage
        4. Clean, professional coding style with:
        - Proper header includes
        - Meaningful identifier names
        - Consistent indentation (4 spaces)
        - Doxygen-style function comments
        - Appropriate const correctness
        5. Include necessary standard library headers
        6. Use modern C++ features (smart pointers, std::optional, etc.) where applicable
        7. Avoid using namespace std; (use std:: prefix instead)
        8. Provide complete compilable implementation"""
            },
            {
                "role": "user",
                "content": f"""Problem Statement:
        {problem}

        Required Deliverables:
        1. Complete C++20 solution in a single compilable file
        2. Must include:
        - All necessary standard library headers
        - Precise function documentation
        - Input validation
        - Edge case handling
        3. Solution must demonstrate:
        - Algorithmic efficiency
        - Memory safety
        - Exception safety where applicable
        4. Format requirements:
        - 80 character line width limit
        - Clear separation of logical sections
        - No using namespace std;

        Output ONLY the C++ code with no additional explanations or commentary."""
            }
        ],
        stream=False
    )

    raw_response = response.choices[0].message.content
    return raw_response
num_samples_per_task = 2
# samples = [
#     dict(task_id=task_id, completion=generate_one_completion(problems[task_id]["prompt"]))
#     for task_id in problems
#     for _ in range(num_samples_per_task)
# ]
# write_jsonl("samples.jsonl", samples)
# 只生成一个样例用于测试
samples = []
i=0;
for task_id in problems:
    # 生成当前问题的代码完成内容
    completion = generate_one_completion(problems[task_id]["prompt"])
    # 添加到样本列表
    samples.append(dict(task_id=task_id, completion=completion))
    # 只生成一个样例就退出循环
    print(f"已生成一个测试样例，任务ID: {task_id}")
    print("样例代码预览:")
    print(completion[:200] + "..." if len(completion) > 200 else completion)
    write_jsonl(f"sample_test.jsonl", samples)
    i=i+1;
    if i==2:
        break



# 保存到文件

print("样例已保存到 sample_test.jsonl 文件")