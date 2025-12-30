from random import randint


def main(n):
    """
    n: 规模参数，用来控制网格大小和点的数量
    逻辑与原程序一致：在 n×m 网格上，寻找离给定点集的最远位置（曼哈顿距离），
    并输出该位置的坐标 (row, col)。
    """

    # 根据 n 生成测试数据
    # 设网格大小为 n 行 m 列，m 可与 n 相关（例如 m = n 或 m = 2n 等）
    # 这里选择 m = n，形成 n×n 的网格
    m = n

    # 生成 k 个点，k 不宜过大，取与 n 线性相关
    # 至少 1 个点
    k = max(1, n // 3)

    # 随机生成 k 个点坐标 (x, y)，1 ≤ x ≤ n, 1 ≤ y ≤ m
    pairs = []
    for _ in range(k):
        x = randint(1, n)
        y = randint(1, m)
        pairs.append((x, y))

    # 以下逻辑与原始程序保持一致
    last_tree = (1, 1)
    maxd = 0
    mult = m * n

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            md = mult
            for x, y in pairs:
                d = abs(i - x) + abs(j - y)
                md = min(md, d)
            if md > maxd:
                last_tree = (i, j)
                maxd = md

    # 输出结果（原程序写入 output.txt，这里直接打印）
    print(f"{last_tree[0]} {last_tree[1]}")


if __name__ == "__main__":
    # 示例：可在此处调整 n 的默认测试规模
    main(10)