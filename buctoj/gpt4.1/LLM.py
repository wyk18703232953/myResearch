from openai import OpenAI
import os

def get_api(problem,i):
    client = OpenAI(api_key="sk-glL4mhF8GCov9dZiCJLIQ64OvlUpPa2qjLCpnV6zKz4byxXE", base_url="https://yunwu.ai/v1")

    response = client.chat.completions.create(
        # model="gpt-4.1-mini-2025-04-14",#0.4 1.6
        # model="gpt-4o-mini", #0.15 0.6
        # model="o1-pro-all", 
        model="o3-mini-all",
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
    lines = raw_response.splitlines()
    code_lines = []

    inside_code = False
    for line in lines:
        if line.strip().startswith("```"):
            inside_code = not inside_code
            continue
        if inside_code:
            code_lines.append(line)

    clean_code = "\n".join(code_lines).strip()
    # print(clean_code)
    answer_dir = "answer"
    os.makedirs(answer_dir, exist_ok=True)
    # raw_path = os.path.join(answer_dir, f"answer_raw{i+1}.text")
    # with open(raw_path, "w", encoding="utf-8") as f:
    #     f.write(raw_response)
    clean_path = os.path.join(answer_dir, f"answer{i+1}.text")
    with open(clean_path, "w", encoding="utf-8") as f:
        f.write(clean_code)
    return clean_code
