from openai import OpenAI


def get_api(problem):
    client = OpenAI(api_key="sk-4e924cf0526746398b2517c9a36b6705", base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-reasoner",
        temperature=0.0,
        messages=[
            {
                "role": "system",
                "content": "You are a senior C++ programmer with deep expertise in data structures and algorithms. You write clean, efficient, and easy-to-understand C++ code that follows good programming practices. Your code should include necessary comments and maintain a clear coding style."
            },
            {
                "role": "user",
                "content": "\n".join([
                    "Task: Please solve the following programming problem using C++.",
                    f"Problem: {problem}",
                    "Requirements:",
                    "1. Only output the complete and compilable C++ code.",
                    "2. Do not include any explanation, text, or formatting outside the code.",
                    "3. Use clear variable names and follow standard C++ conventions.",
                    "Response_format: Respond only with the complete C++ code that can be compiled directly, and nothing else."
                ])
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

    return clean_code