import random


def main(n):
    # 生成测试数据：n 行 m 列网格，以及水平/垂直边权
    # 此处令 m = n（也可根据需要调整为其他与 n 相关的规模）
    m = n

    # 边权范围可调
    MIN_COST = 1
    MAX_COST = 10

    # 生成 k（必须为偶数才能有解，原程序若 k 为奇数则输出 -1）
    # 这里直接保证 k 为偶数：例如固定为 2*n，若为 0 则没有移动
    k = 2 * n
    if k % 2 != 0:
        k += 1

    # 当 k 为奇数，输出 -1 矩阵
    if k % 2 != 0:
        for _ in range(n):
            print(*([-1] * m))
        return

    # 生成水平边权：n 行，每行 m-1 个权值
    horiz = [[random.randint(MIN_COST, MAX_COST) for _ in range(m - 1)]
             for _ in range(n)]

    # 生成垂直边权：n-1 行，每行 m 个权值
    vert = [[random.randint(MIN_COST, MAX_COST) for _ in range(m)]
            for _ in range(n - 1)]

    # 下面是原逻辑，不再使用 input()，直接使用生成的数据

    half_k = k // 2  # 原代码中 k /= 2

    DP = [[[0] * m for _ in range(n)] for _ in range(half_k + 1)]
    G = [[[] for _ in range(m)] for _ in range(n)]

    # 构建水平边
    for i in range(n):
        for j in range(m - 1):
            cost = horiz[i][j]
            G[i][j].append((cost, i, j + 1))
            G[i][j + 1].append((cost, i, j))

    # 构建垂直边
    for i in range(n - 1):
        for j in range(m):
            cost = vert[i][j]
            G[i][j].append((cost, i + 1, j))
            G[i + 1][j].append((cost, i, j))

    # 动态规划
    for p in range(1, half_k + 1):
        for u in range(n):
            for v in range(m):
                DP[p][u][v] = min(
                    DP[p - 1][x][y] + cost for (cost, x, y) in G[u][v]
                )

    # 输出答案
    for i in range(n):
        ans = [DP[half_k][i][j] * 2 for j in range(m)]
        print(*ans)


if __name__ == "__main__":
    # 示例调用：规模 n = 4
    main(4)