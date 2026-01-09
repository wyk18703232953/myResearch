def main(n):
    # 根据规模 n 生成测试数据：
    # 这里简单设定 R, G, B 都与 n 相等，
    # 并生成一些确定性的递减序列作为颜色数组。
    R = G = B = n

    # 生成测试数据（可按需要调整生成策略）
    r = list(range(1, R + 1))
    g = list(range(1, G + 1))
    b = list(range(1, B + 1))

    # 原代码中会排序为降序，这里保持一致
    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    # 动态规划数组
    dp = [[[0] * (B + 1) for _ in range(G + 1)] for __ in range(R + 1)]
    ans = 0

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if i > 0 and j > 0 and k > 0:
                    dp[i][j][k] = max(
                        dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1],
                        dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1],
                        dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1],
                    )
                elif i > 0 and j > 0:
                    dp[i][j][k] = dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1]
                elif i > 0 and k > 0:
                    dp[i][j][k] = dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1]
                    ans = max(ans, dp[i][j][k])
                elif j > 0 and k > 0:
                    dp[i][j][k] = dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1]
                ans = max(ans, dp[i][j][k])

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(3)