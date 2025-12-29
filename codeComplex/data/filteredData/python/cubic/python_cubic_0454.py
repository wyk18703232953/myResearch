import random

def main(n):
    # 生成规模参数
    # 为了保持与原逻辑一致，需要 n 行、m 列、路径长度 k
    # 这里简单设：m = n，k = 2 * n（保证为偶数，且有一定规模）
    m = n
    k = 2 * n

    # 生成测试数据：边权为 1~10 的随机整数
    horizontal_edges = []
    for _ in range(n):
        horizontal_edges.append([random.randint(1, 10) for _ in range(m - 1)])

    vertical_edges = []
    for _ in range(n - 1):
        vertical_edges.append([random.randint(1, 10) for _ in range(m)])

    # 若 k 为奇数，直接输出 -1（这里构造 k 为偶数，一般不会触发）
    if k % 2 == 1:
        for _ in range(n):
            print(' '.join(['-1'] * m))
        return

    INF = 10 ** 9
    dp = [[[INF for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            dp[i][j][0] = 0

    for z in range(2, k + 1, 2):
        for i in range(n):
            for j in range(m):
                # 垂直移动
                if i > 0:
                    if i < n - 1:
                        dp[i][j][z] = min(
                            dp[i - 1][j][z - 2] + 2 * vertical_edges[i - 1][j],
                            dp[i + 1][j][z - 2] + 2 * vertical_edges[i][j],
                        )
                    else:
                        dp[i][j][z] = dp[i - 1][j][z - 2] + 2 * vertical_edges[i - 1][j]
                else:
                    dp[i][j][z] = dp[i + 1][j][z - 2] + 2 * vertical_edges[i][j]

                # 水平移动
                if j > 0:
                    if j < m - 1:
                        dp[i][j][z] = min(
                            dp[i][j][z],
                            dp[i][j - 1][z - 2] + 2 * horizontal_edges[i][j - 1],
                            dp[i][j + 1][z - 2] + 2 * horizontal_edges[i][j],
                        )
                    else:
                        dp[i][j][z] = min(
                            dp[i][j][z],
                            dp[i][j - 1][z - 2] + 2 * horizontal_edges[i][j - 1],
                        )
                else:
                    dp[i][j][z] = min(
                        dp[i][j][z],
                        dp[i][j + 1][z - 2] + 2 * horizontal_edges[i][j],
                    )

    for i in range(n):
        print(' '.join(str(dp[i][j][k]) for j in range(m)))


if __name__ == "__main__":
    # 示例：调用 main(3) 运行规模为 3 的测试
    main(3)