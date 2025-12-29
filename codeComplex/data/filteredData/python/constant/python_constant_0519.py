def main(n):
    """
    n 为规模参数，这里用于生成测试数据的范围上限：
    x, y, z 在 [0, n]
    t1, t2, t3 在 [1, n]（避免为 0）
    """
    import random

    # 生成测试数据
    x = random.randint(0, n)
    y = random.randint(0, n)
    z = random.randint(0, n)
    t1 = random.randint(1, n)
    t2 = random.randint(1, n)
    t3 = random.randint(1, n)

    # 原逻辑
    lift = abs(z - x) * t2 + t3 + t3 + abs(x - y) * t2 + t3
    stairs = t1 * abs(x - y)

    if lift <= stairs:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：n=10 的一次运行
    main(10)