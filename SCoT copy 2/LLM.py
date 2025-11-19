from openai import OpenAI
import os

def get_api():
    client = OpenAI(api_key="sk-glL4mhF8GCov9dZiCJLIQ64OvlUpPa2qjLCpnV6zKz4byxXE", base_url="https://yunwu.ai/v1")
    response = client.chat.completions.create(
        model="gpt-5-nano-2025-08-07",
        temperature=0.0,
        messages = [
        {
            "role": "system",
            "content": "hello world"
            }
        ],
        stream=False
    )
    return response.choices[0].message.content  

print(get_api())


