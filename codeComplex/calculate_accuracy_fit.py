import json
import glob
import os

# 获取所有stats_*.json文件，但排除stats_global.json
stats_files = glob.glob('/home/wuyankai/myResearch/codeComplex/demo/filteredData/python/**/stats_*.json', recursive=True)
stats_files = [f for f in stats_files if 'stats_global' not in f]

print("复杂度类型统计结果：")
print("=" * 50)

# 定义类型名称映射
type_name_map = {
    'constant': 'constant',
    'logn': 'logn',
    'linear': 'linear',
    'nlogn': 'nlogn',
    'quadratic': 'quadratic',
    'cubic': 'cubic'
}

# 按类型排序
stats_files.sort(key=lambda x: list(type_name_map.keys()).index(os.path.basename(x).split('_')[1].split('.')[0]))

# 初始化总统计变量
total_global = 0
success_global = 0

for file_path in stats_files:
    # 从文件名中提取类型
    file_name = os.path.basename(file_path)
    type_name = file_name.split('_')[1].split('.')[0]
    
    # 读取统计数据
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    total = data.get('total', 0)
    success = data.get('success', 0)
    
    # 累加全局统计
    total_global += total
    success_global += success
    
    # 计算准确率
    accuracy = (success / total * 100) if total > 0 else 0
    
    # 格式化输出
    print(f"{type_name.ljust(15)} 总: {total:4d} 正确: {success:4d} 准确率: {accuracy:6.2f}%")

# 计算并输出总准确率
print("=" * 50)
if total_global > 0:
    global_accuracy = (success_global / total_global * 100)
    print(f"{'总准确率'.ljust(15)} 总: {total_global:4d} 正确: {success_global:4d} 准确率: {global_accuracy:6.2f}%")
else:
    print(f"{'总准确率'.ljust(15)} 总: {total_global:4d} 正确: {success_global:4d} 准确率:  0.00%")
print("=" * 50)