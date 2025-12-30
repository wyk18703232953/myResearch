def main(n):
    mod = 998244353

    # 依据规模 n 生成测试数据，这里令 k = n（可按需修改生成规则）
    k = n

    # 原逻辑中的数组大小为 [n][k+2][4]，保持不变
    dp = [[[0] * 4 for _ in range(k + 2)] for _ in range(n)]
    dp[0][1] = [0, 1, 1, 0]
    dp[0][0] = [1, 0, 0, 1]

    for i in range(1, n):
        for r in range(k):
            # 对应原代码的状态转移
            dp[i][r + 1][3] = (dp[i][r + 1][3] + dp[i - 1][r][0]) % mod
            dp[i][r + 1][2] = (dp[i][r + 1][2] + dp[i - 1][r][0]) % mod
            dp[i][r + 1][1] = (dp[i][r + 1][1] + dp[i - 1][r][0]) % mod
            dp[i][r][0] = (dp[i][r][0] + dp[i - 1][r][0]) % mod

            dp[i][r + 2][2] = (dp[i][r + 2][2] + dp[i - 1][r][1]) % mod
            dp[i][r][0] = (dp[i][r][0] + dp[i - 1][r][1]) % mod
            dp[i][r][3] = (dp[i][r][3] + dp[i - 1][r][1]) % mod
            dp[i][r][1] = (dp[i][r][1] + dp[i - 1][r][1]) % mod

            dp[i][r + 2][1] = (dp[i][r + 2][1] + dp[i - 1][r][2]) % mod
            dp[i][r][0] = (dp[i][r][0] + dp[i - 1][r][2]) % mod
            dp[i][r][3] = (dp[i][r][3] + dp[i - 1][r][2]) % mod
            dp[i][r][2] = (dp[i][r][2] + dp[i - 1][r][2]) % mod

            dp[i][r + 1][0] = (dp[i][r + 1][0] + dp[i - 1][r][3]) % mod
            dp[i][r + 1][2] = (dp[i][r + 1][2] + dp[i - 1][r][3]) % mod
            dp[i][r + 1][1] = (dp[i][r + 1][1] + dp[i - 1][r][3]) % mod
            dp[i][r][3] = (dp[i][r][3] + dp[i - 1][r][3]) % mod

    # 输出结果：等价于原程序的最终 print
    if k - 1 >= 0:
        ans = (
            dp[-1][k - 1][0]
            + dp[-1][k - 1][1]
            + dp[-1][k - 1][2]
            + dp[-1][k - 1][3]
        ) % mod
    else:
        ans = 0

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)