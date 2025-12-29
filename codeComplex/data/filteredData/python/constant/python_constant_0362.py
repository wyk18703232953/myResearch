import random

def main(n):
    # 所有可能的颜色
    all_colors = ["purple", "green", "red", "blue", "orange", "yellow"]
    
    # 生成测试数据：从 all_colors 中随机选择 n 个不同的颜色
    # 若 n 大于 6，则只取前 6 个
    n = min(n, len(all_colors))
    l = random.sample(all_colors, n)
    
    # 下面是原逻辑
    print(6 - n)
    if "purple" not in l:
        print("Power")
    if "green" not in l:
        print("Time")
    if "red" not in l:
        print("Reality")
    if "blue" not in l:
        print("Space")
    if "orange" not in l:
        print("Soul")
    if "yellow" not in l:
        print("Mind")

# 示例调用（提交到评测系统时可删除或注释）
if __name__ == "__main__":
    main(3)