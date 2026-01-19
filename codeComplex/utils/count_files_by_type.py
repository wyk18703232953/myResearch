import os

# 指定要统计的根目录
demo_root = '/home/wuyankai/myResearch/codeComplex/demo/filteredData/python'

print("正在统计 /home/wuyankai/myResearch/codeComplex/demo/filteredData/python 目录下各子文件夹的文件数量...")
print("=" * 60)

# 获取所有子目录
subdirectories = [d for d in os.listdir(demo_root) if os.path.isdir(os.path.join(demo_root, d))]

# 按字母顺序排序子目录
subdirectories.sort()
total=0
# 统计每个子目录中的文件数量
total_files = 0
for subdir in subdirectories:
    subdir_path = os.path.join(demo_root, subdir)
    
    # 统计该子目录下的文件数量（不包括子目录）
    file_count = sum(1 for f in os.listdir(subdir_path) if os.path.isfile(os.path.join(subdir_path, f)))
    
    # 统计该子目录下的子目录数量（用于了解结构）
    dir_count = sum(1 for d in os.listdir(subdir_path) if os.path.isdir(os.path.join(subdir_path, d)))
    
    print(f"{subdir:<10}:  {file_count:>5} 个文件,  {dir_count:>5} 个子目录")
    total_files += file_count
    total+=dir_count

print("=" * 60)
print(f"总计:            {total_files:>5} 个文件, {total:>5} 个子目录")
