def main(n):
    # 生成测试数据，这里简单设置 k 与 n 相关
    # 确保 1 <= k <= 2*n
    k = max(1, min(2 * n, n))  # 示例：k = n，且做边界裁剪

    mod = 998244353
    dp = [[[0, 0] for _ in range(2 * n + 1)] for _ in range(n)]
    dp[0][0][0] = 1
    dp[0][1][1] = 1

    for i in range(1, n):
        for j in range(2 * n - 1):
            a0 = dp[i - 1][j][0]
            a1 = dp[i - 1][j][1]

            dp[i][j][0] = (dp[i][j][0] + a0 + 2 * a1) % mod
            dp[i][j + 1][0] = (dp[i][j + 1][0] + a0) % mod
            dp[i][j + 1][1] = (dp[i][j + 1][1] + 2 * a0) % mod
            dp[i][j][1] = (dp[i][j][1] + a1) % mod
            dp[i][j + 2][1] = (dp[i][j + 2][1] + a1) % mod

    ans = sum(dp[n - 1][k - 1]) * 2 % mod
    print(ans)


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的默认值
    main(5)