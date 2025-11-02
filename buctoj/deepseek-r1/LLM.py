from openai import OpenAI
import os

def get_api(problem,i):
    client = OpenAI(api_key="sk-glL4mhF8GCov9dZiCJLIQ64OvlUpPa2qjLCpnV6zKz4byxXE", base_url="https://yunwu.ai/v1")

    response = client.chat.completions.create(
        model="deepseek-r1",
        temperature=0.0,
        messages=[
            {
                "role": "system",
                "content": "You are an experienced C++ senior programmer specializing in data structures and algorithms. Please write high-quality C++ code based on a user problem, ensuring that the code:\n1. follows modern C++ standards (e.g., C++17/20)\n2. is well-structured, well-named, and appropriately commented\n3. has good error-handling and boundary-condition checking\n4. is optimal in terms of time and space complexity\n\nPlease provide the complete C++ code directly in a compileable form, with no additional explanations or explanations. The code should contain the necessary header files and namespace declarations."
            },
            {
                "role": "user",
                "content": f"Task: Write C++ code to solve the following problem\n\nProblem description: {problem}\n\nRequirements:\n- Provide complete C++ code that can be compiled and run directly\n- The code should contain the necessary comments, but does not need to explain the problem or the solution\n- Follow C++ best practices and code specifications."
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
    # os.makedirs(answer_dir, exist_ok=True)
    # raw_path = os.path.join(answer_dir, f"answer_raw{i+1}.text")
    # with open(raw_path, "w", encoding="utf-8") as f:
    #     f.write(raw_response)
    clean_path = os.path.join(answer_dir, f"answer{i+1}.text")
    with open(clean_path, "w", encoding="utf-8") as f:
        f.write(clean_code)
    return clean_code
