def main(n, m=10**9+7):
    N = 405  # 最大规模上界，可按需调整或设为 n+5 等
    dp = [[0] * N for _ in range(N)]
    c = [[1] * N for _ in range(N)]
    p = [0] * N

    # 预处理 2 的幂
    p[0] = 1
    for i in range(1, N):
        p[i] = (p[i - 1] * 2) % m

    # 预处理组合数 C(i, j) mod m
    for i in range(1, N):
        for j in range(1, i):
            c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % m

    # 原始 DP 逻辑
    dp[0][0] = 1
    for i in range(2, n + 2):
        for x in range(1, (n - 1) // 2 + 2):
            for k in range(1, i):
                dp[i][x] = (dp[i][x]
                            + ((dp[i - k - 1][x - 1] * p[k - 1]) % m)
                            * c[i - x][k]) % m

    ans = 0
    for i in range(1, (n - 1) // 2 + 2):
        ans = (ans + dp[n + 1][i]) % m

    print(ans)


if __name__ == "__main__":
    # 示例：n 可在此处自定义，用于自动生成规模为 n 的测试
    main(10)