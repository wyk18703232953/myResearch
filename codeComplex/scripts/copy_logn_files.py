import os
import shutil
import re

# 源目录和目标目录
SOURCE_DIR = "/home/wuyankai/myResearch/codeComplex/data/onlyCode/python/constant"
DEST_DIR = "/home/wuyankai/myResearch/codeComplex/demo/filteredData/python/constant"

# 复制文件到对应的子目录
def copy_files_to_subdirectories():
    """将源目录中的每个Python文件复制到目标目录中对应的子目录"""
    file_count = 0
    
    # 遍历源目录中的所有Python文件
    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith('.py'):
            # 提取文件名中的编号部分
            match = re.match(r'python_constant_(\d+)\.py', filename)
            if match:
                number = match.group(1)
                # 构建对应的子目录名
                subdir_name = f"results_python_constant_{number}"
                dest_subdir = os.path.join(DEST_DIR, subdir_name)
                
                # 确保子目录存在
                os.makedirs(dest_subdir, exist_ok=True)
                
                # 复制文件到子目录，并重命名为原名+1（在扩展名前添加1）
                src_path = os.path.join(SOURCE_DIR, filename)
                # 分离文件名和扩展名
                name_without_ext, ext = os.path.splitext(filename)
                # 在文件名后添加1，然后添加扩展名
                dest_filename = f"{name_without_ext}_onlycode{ext}"
                dest_path = os.path.join(dest_subdir, dest_filename)
                
                shutil.copy2(src_path, dest_path)
                file_count += 1
                print(f"复制: {filename} -> {subdir_name}/{dest_filename}")
            else:
                print(f"跳过: {filename} (不符合命名模式)")
    
    return file_count

# 开始复制
print(f"开始复制文件从 {SOURCE_DIR} 到 {DEST_DIR} 的对应子目录")

file_count = copy_files_to_subdirectories()

print(f"\n复制完成！共复制了 {file_count} 个Python文件。")
