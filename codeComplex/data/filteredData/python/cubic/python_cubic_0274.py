def main(n):
    import random

    # 根据规模 n 生成 r, g, b（总规模大致与 n 成正比）
    # 这里简单设定 r = g = b = n
    r = g = b = n

    # 生成测试数据：随机正整数
    # 可根据需要调整数值范围
    l1 = [random.randint(1, 10**4) for _ in range(r)]
    l2 = [random.randint(1, 10**4) for _ in range(g)]
    l3 = [random.randint(1, 10**4) for _ in range(b)]

    l1.sort(reverse=True)
    l2.sort(reverse=True)
    l3.sort(reverse=True)

    # 三维 DP，注意内存为 O(r*g*b)，n 不宜太大
    dp = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    ans = 0

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i > 0 and j > 0:
                    dp[i][j][k] = max(dp[i][j][k], l1[i - 1] * l2[j - 1] + dp[i - 1][j - 1][k])
                if i > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k], l1[i - 1] * l3[k - 1] + dp[i - 1][j][k - 1])
                if j > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k], l2[j - 1] * l3[k - 1] + dp[i][j - 1][k - 1])
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]

    print(ans)


if __name__ == "__main__":
    # 示例：n=5
    main(5)