def main(n: int):
    import random

    # 1. 生成规模：R, G, B 根据 n 来设置，这里简单设为 n
    R = n
    G = n
    B = n

    # 2. 生成测试数据：1~100 的随机整数，并按题意降序排序
    r = sorted([random.randint(1, 100) for _ in range(R)], reverse=True)
    g = sorted([random.randint(1, 100) for _ in range(G)], reverse=True)
    b = sorted([random.randint(1, 100) for _ in range(B)], reverse=True)

    # 3. 原逻辑
    ans = 0
    dp = [[[0 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if i < R and j < G:
                    dp[i + 1][j + 1][k] = max(
                        dp[i + 1][j + 1][k],
                        dp[i][j][k] + r[i] * g[j]
                    )
                if j < G and k < B:
                    dp[i][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1],
                        dp[i][j][k] + g[j] * b[k]
                    )
                if i < R and k < B:
                    dp[i + 1][j][k + 1] = max(
                        dp[i + 1][j][k + 1],
                        dp[i][j][k] + b[k] * r[i]
                    )
                ans = max(ans, dp[i][j][k])

    print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)