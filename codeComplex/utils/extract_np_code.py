import json
import os

# 输入JSON文件路径
json_file_path = '/home/wuyankai/myResearch/codeComplex/data/onlyCode/python/python_complexity_np.json'
# 输出文件夹路径
output_dir = '/home/wuyankai/myResearch/codeComplex/data/onlyCode/python/np'

# 确保输出文件夹存在
os.makedirs(output_dir, exist_ok=True)

# 读取JSON文件
with open(json_file_path, 'r', encoding='utf-8') as f:
    code_list = json.load(f)

# 遍历每个代码片段并生成.py文件
for i, code in enumerate(code_list):
    # 生成文件名
    file_name = f'python_np_{i+1:04d}.py'
    file_path = os.path.join(output_dir, file_name)
    
    # 保存代码到文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(code)

print(f'已成功生成 {len(code_list)} 个Python文件到 {output_dir}')