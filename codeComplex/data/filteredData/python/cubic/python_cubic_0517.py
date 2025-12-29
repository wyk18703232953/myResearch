import random

def main(n):
    # 可按需修改：列数 m、步数 K、权值范围
    m = n
    K = 4  # 必须为偶数，否则结果恒为 -1
    max_w = 10

    # 生成测试数据：随机边权，正整数
    edgesh = [[random.randint(1, max_w) for _ in range(m - 1)] for _ in range(n)]
    edgesv = [[random.randint(1, max_w) for _ in range(m)] for _ in range(n - 1)]

    INF = 10 ** 10
    # dp[i][j][k]：从 (i,j) 出发走恰好 k 步回到 (i,j) 的最小代价
    dp = [[[INF for _ in range(K + 1)] for _ in range(m)] for _ in range(n)]

    for k in range(0, K + 1, 2):
        for i in range(n):
            for j in range(m):
                if k == 0:
                    dp[i][j][k] = 0
                else:
                    best = INF
                    # 向右再回来：经过边 (i, j)-(i, j+1)
                    if j + 1 < m:
                        best = min(best, 2 * edgesh[i][j] + dp[i][j + 1][k - 2])
                    # 向左再回来：经过边 (i, j-1)-(i, j)
                    if j - 1 >= 0:
                        best = min(best, 2 * edgesh[i][j - 1] + dp[i][j - 1][k - 2])
                    # 向下再回来：经过边 (i, j)-(i+1, j)
                    if i + 1 < n:
                        best = min(best, 2 * edgesv[i][j] + dp[i + 1][j][k - 2])
                    # 向上再回来：经过边 (i-1, j)-(i, j)
                    if i - 1 >= 0:
                        best = min(best, 2 * edgesv[i - 1][j] + dp[i - 1][j][k - 2])

                    dp[i][j][k] = best

    # 输出结果
    for i in range(n):
        row = []
        for j in range(m):
            val = dp[i][j][K]
            row.append(str(-1 if val >= INF else val))
        print(" ".join(row))


if __name__ == "__main__":
    # 示例调用：n = 4
    main(4)