import random

def main(n: int):
    # 宝石字典
    d = {
        'purple': 'Power',
        'green': 'Time',
        'blue': 'Space',
        'orange': 'Soul',
        'red': 'Reality',
        'yellow': 'Mind'
    }

    # 根据 n 生成测试数据：随机选择要“移除”的颜色键
    # 实际可移除的最大数量不超过字典大小
    n = max(0, min(n, len(d)))
    colors = list(d.keys())
    remove_keys = random.sample(colors, n)  # 随机选 n 个不同的 key

    # 模拟原逻辑：依次 pop 掉这些 key
    for key in remove_keys:
        d.pop(key, None)

    # 输出结果：剩余数量和对应的 value，每个占一行
    print(len(d), *d.values(), sep='\n')


if __name__ == "__main__":
    # 示例：可自行修改 n 测试
    main(3)