import random

def main(n):
    # 规模参数：我们用 n 同时作为行数、列数和步数上限的一部分来源
    # 为了保持原程序含义，这里构造：
    #   n_rows = n
    #   m_cols = n
    #   k_steps = n（可按需要调整生成规则）
    n_rows = n
    m_cols = n
    k_steps = n

    # 生成测试数据：边权 wh (横向) 和 wv (纵向)
    # wh: n_rows 行，每行 m_cols-1 个权值，范围 1..10
    # wv: n_rows-1 行，每行 m_cols 个权值，范围 1..10
    wh = []
    for _ in range(n_rows):
        if m_cols > 1:
            row = [random.randint(1, 10) for _ in range(m_cols - 1)]
        else:
            row = []
        wh.append(row)

    wv = []
    for _ in range(n_rows - 1):
        row = [random.randint(1, 10) for _ in range(m_cols)]
        wv.append(row)

    n = n_rows
    m = m_cols
    k = k_steps

    if k % 2 != 0:
        ans = [[-1 for _ in range(m)] for _ in range(n)]
        for res in ans:
            print(*res)
        return

    # dp 尺寸按原程序：dp[505][505][25]
    # 但只会用到 i<=n, j<=m, x<=k
    MAX_N = 505
    MAX_M = 505
    MAX_K = 25  # 原代码第三维大小为 25

    if k >= MAX_K:
        # 若 k 过大会越界，简单截断到 MAX_K-1
        k = MAX_K - 1

    INF = 1234567890
    dp = [[[0 for _ in range(MAX_K)] for _ in range(MAX_M)] for _ in range(MAX_N)]

    for x in range(1, k + 1):
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
        for j in range(1, m + 1):
            ans = INF
            for x in range(1, k + 1):
                if k % x == 0 and (k // x) % 2 == 0:
                    ans = min(ans, dp[i][j][x] * (k // x))
            print(ans, end=" ")
        print()


if __name__ == "__main__":
    # 示例调用：可以修改这里的 n 观察不同规模
    main(5)