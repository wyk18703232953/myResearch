from openai import OpenAI
import os

def get_api(problem,problem_name):
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
    answer_dir = "d:/myResearch/luogu/answer"
    clean_path = os.path.join(answer_dir, f"{problem_name}.txt")
   
    with open(clean_path, "w", encoding="utf-8") as f:
        f.write(raw_response)
    return raw_response
# 读取problems文件夹中的所有文件，将文件中的内容赋值为problem，并将文件名赋值为problem_name
folder_path = "d:/myResearch/luogu/problems"
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            problem = content
            problem_name = os.path.splitext(file_name)[0]
            get_api(problem,problem_name)
