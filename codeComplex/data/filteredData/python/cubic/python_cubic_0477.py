import random

def main(n):
    # 生成规模参数
    # 原程序中有 n, m, k，这里令 m = n，k = 2 * n（保证为偶数且随规模变化）
    m = n
    k = 2 * n

    # 生成测试数据：边权随机正整数（可以根据需要调整范围）
    wh = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]       # 左右边权
    wv = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]       # 上下边权

    if k % 2 != 0:
        ans = [[-1 for _ in range(m)] for _ in range(n)]
        for res in ans:
            print(*res)
        return

    # dp[i][j][x]: 在(i,j)走恰好x步的最小代价（1-based 索引）
    MAXN = 505
    MAXM = 505
    MAXK = 25
    INF = 1234567890

    # 为了保持原逻辑，仍然按最大尺寸开数组
    dp = [[[0 for _ in range(MAXK)] for _ in range(MAXM)] for _ in range(MAXN)]

    # 由于 k 的最大可用步数只会用到 1..min(20, k)
    limit_x = min(20, k)

    for x in range(1, limit_x + 1):
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j][x] = INF
                if i != n:
                    dp[i][j][x] = min(dp[i][j][x],
                                      dp[i + 1][j][x - 1] + wv[i - 1][j - 1])
                if i != 1:
                    dp[i][j][x] = min(dp[i][j][x],
                                      dp[i - 1][j][x - 1] + wv[i - 2][j - 1])
                if j != m:
                    dp[i][j][x] = min(dp[i][j][x],
                                      dp[i][j + 1][x - 1] + wh[i - 1][j - 1])
                if j != 1:
                    dp[i][j][x] = min(dp[i][j][x],
                                      dp[i][j - 1][x - 1] + wh[i - 1][j - 2])

    for i in range(1, n + 1):
        row = []
        for j in range(1, m + 1):
            ans = INF
            for x in range(1, min(k, limit_x) + 1):
                if k % x == 0 and (k // x) % 2 == 0:
                    ans = min(ans, dp[i][j][x] * (k // x))
            row.append(str(ans if ans != INF else -1))
        print(" ".join(row))


if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)