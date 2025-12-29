def main(n: int):
    import random

    # 1. 根据规模 n 生成测试数据
    # 这里将 n 拆成三部分，分别作为 R, G, B 的数量
    # 你可以根据需要调整拆分和取值范围
    R = n // 3
    G = (n - R) // 2
    B = n - R - G

    # 生成随机正整数，取值范围 [1, 10^4]
    r = [random.randint(1, 10_000) for _ in range(R)]
    g = [random.randint(1, 10_000) for _ in range(G)]
    b = [random.randint(1, 10_000) for _ in range(B)]

    # 2. 原逻辑开始
    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)
    nr = len(r)
    ng = len(g)
    nb = len(b)

    dp = [[[0] * (nb + 1) for _ in range(ng + 1)] for _ in range(nr + 1)]
    ans = 0
    for i in range(nr + 1):
        for j in range(ng + 1):
            for k in range(nb + 1):
                if (i + j + k) % 2 == 1:
                    continue
                if i > 0 and j > 0:
                    # Make RG
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1])
                if j > 0 and k > 0:
                    # Make GB
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1])
                if i > 0 and k > 0:
                    # Make BR
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j][k - 1] + b[k - 1] * r[i - 1])
                ans = max(ans, dp[i][j][k])

    print(ans)


if __name__ == "__main__":
    # 示例：使用 n = 30 运行
    main(30)