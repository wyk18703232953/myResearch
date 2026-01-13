import os
import shutil

data_dir = "/home/wuyankai/myResearch/codeComplex/data/filteredData/python"
demo_dir = "/home/wuyankai/myResearch/codeComplex/demo/filteredData/python"

# 获取所有数据类型
data_types = os.listdir(data_dir)

for data_type in data_types:
    # 跳过非目录
    if not os.path.isdir(os.path.join(data_dir, data_type)):
        continue
    
    # 如果demo目录中没有对应的类型文件夹，跳过
    demo_type_dir = os.path.join(demo_dir, data_type)
    if not os.path.exists(demo_type_dir):
        continue
    
    print(f"处理类型: {data_type}")
    
    # 获取数据目录中的所有文件名（不包含扩展名）
    data_files = set()
    data_type_dir = os.path.join(data_dir, data_type)
    for filename in os.listdir(data_type_dir):
        if filename.endswith(".py"):
            data_files.add(os.path.splitext(filename)[0])
    
    # 获取demo目录中的所有结果文件夹名
    demo_files = set()
    for folder_name in os.listdir(demo_type_dir):
        if os.path.isdir(os.path.join(demo_type_dir, folder_name)):
            # 结果文件夹名格式通常为：results_python_xxx_xxxx
            # 或直接是文件名（没有.py扩展名）
            # 尝试提取对应的源代码文件名
            if folder_name.startswith("results_"):
                # 从results_python_xxx_xxxx中提取python_xxx_xxxx部分
                parts = folder_name.split("_")
                if len(parts) >= 4:
                    # 重构文件名：python_xxx_xxxx
                    source_filename = "_".join(parts[1:4])
                    demo_files.add(source_filename)
            else:
                # 直接是文件名
                demo_files.add(folder_name)
    
    # 找出demo中存在但data中不存在的文件
    files_to_delete = demo_files - data_files
    
    if files_to_delete:
        print(f"  找到 {len(files_to_delete)} 个需要删除的结果文件夹")
        
        # 删除这些结果文件夹
        for filename in files_to_delete:
            # 查找对应的结果文件夹
            for folder_name in os.listdir(demo_type_dir):
                if filename in folder_name:
                    folder_path = os.path.join(demo_type_dir, folder_name)
                    if os.path.isdir(folder_path):
                        print(f"    删除: {folder_path}")
                        shutil.rmtree(folder_path)
                        break
    else:
        print(f"  没有需要删除的结果文件夹")

print("\n清理完成！")