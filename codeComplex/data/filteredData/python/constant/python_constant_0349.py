import random

def main(n):
    # 所有可能的颜色及对应宝石
    ans = {
        'purple': 'Power',
        'green': 'Time',
        'blue': 'Space',
        'orange': 'Soul',
        'red': 'Reality',
        'yellow': 'Mind'
    }

    # n 为给定规模，这里理解为：随机选择 n 个不同颜色作为“已拥有”的颜色
    # n 不能超过颜色总数
    n = max(0, min(n, len(ans)))  # 保证 0 <= n <= 6

    all_colors = list(ans.keys())
    # 随机生成测试数据：从所有颜色中选出 n 个作为 lst
    lst = random.sample(all_colors, n)

    # 逻辑与原程序保持一致
    missing_stones = []
    for color in ans:
        if color not in lst:
            missing_stones.append(ans[color])

    print(len(missing_stones))
    for stone in missing_stones:
        print(stone)


# 示例：直接运行 main(3) 做一次测试
if __name__ == "__main__":
    main(3)