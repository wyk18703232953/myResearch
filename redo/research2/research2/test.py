# Please install OpenAI SDK first: `pip3 install openai`
# import os
from openai import OpenAI

client = OpenAI(
    api_key='sk-glL4mhF8GCov9dZiCJLIQ64OvlUpPa2qjLCpnV6zKz4byxXE',
    base_url="https://yunwu.ai/v1")

response = client.chat.completions.create(
    model="gpt-5-nano-2025-08-07",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)\


# from openai import OpenAI

# client = OpenAI(api_key="sk-glL4mhF8GCov9dZiCJLIQ64OvlUpPa2qjLCpnV6zKz4byxXE", base_url="https://yunwu.ai/v1")

# response = client.chat.completions.create(
#     model="gpt-5-nano-2025-08-07",
#     messages=[
#         {"role": "system","content": "You are  human"},
#         {"role": "user", "content": "你好啊"},
#     ],
#     stream=False
# )
# print(response.choices[0].message.content)
