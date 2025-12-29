def main(n):
    import random

    # 生成测试数据：n 行 m 列网格，K 为偶数以便有意义的答案
    m = n
    K = 2 * (n // 2 + 1)  # 保证 K 为偶数且随 n 增大

    # 生成水平边权重：n 行，每行 m-1 个
    horiz = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    # 生成竖直边权重：n-1 行，每行 m 个
    vert = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    # 构建 edges 结构，与原代码等价
    edges = []
    for i in range(n):
        edges.append([[]])
        lis = horiz[i]
        for j in range(m - 1):
            edges[i][j].append((1, 0, lis[j]))
            edges[i].append([])
            edges[i][j + 1].append((-1, 0, lis[j]))
    for i in range(n - 1):
        lis = vert[i]
        for j in range(m):
            edges[i][j].append((0, 1, lis[j]))
            edges[i + 1][j].append((0, -1, lis[j]))

    # 原始逻辑
    if K % 2 == 1:
        lis = [[-1] * m for _ in range(n)]
    else:
        lis = [[0] * m for _ in range(n)]

        for _ in range(1, (K // 2) + 1):
            new_lis = [[0] * m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    dist = []
                    for e in edges[i][j]:
                        dist.append(e[2] + lis[i + e[1]][j + e[0]])
                    new_lis[i][j] = min(dist)
            lis = new_lis
        for i in range(n):
            for j in range(m):
                lis[i][j] *= 2

    for row in lis:
        print(*row)


if __name__ == "__main__":
    # 示例：规模 n = 4
    main(4)