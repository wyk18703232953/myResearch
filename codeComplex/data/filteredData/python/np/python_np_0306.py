def main(n: int):
    # 根据 n 生成测试数据，这里令 k = n（也可按需修改为其他函数关系）
    k = n

    mod = 998244353
    dp = [[0, 0, 0, 0] for _ in range(k + 1)]
    dp[1][0] = dp[1][3] = 1
    if k > 1:
        dp[2][2] = dp[2][1] = 1

    for _ in range(1, n):
        g = [[0, 0, 0, 0] for _ in range(k + 1)]
        # 0 - bb
        # 1 - bw
        # 2 - wb
        # 3 - ww
        g[1][0] = g[1][3] = 1
        for i in range(2, k + 1):
            g[i][0] = (dp[i][0] + dp[i][1] + dp[i][2] + dp[i - 1][3]) % mod
            g[i][1] = (dp[i - 1][0] + dp[i][1] + dp[i - 2][2] + dp[i - 1][3]) % mod
            g[i][2] = (dp[i - 1][0] + dp[i - 2][1] + dp[i][2] + dp[i - 1][3]) % mod
            g[i][3] = (dp[i - 1][0] + dp[i][1] + dp[i][2] + dp[i][3]) % mod
        dp = g

    ans = sum(dp[-1]) % mod
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)，可按需修改 n 的值
    main(5)