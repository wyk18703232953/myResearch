from random import randint

def main(n):
    # 根据规模 n 生成 R, G, B
    # 这里简单设为不超过 n 的正整数
    R = max(1, n // 3)
    G = max(1, n // 3)
    B = max(1, n - R - G)

    # 生成测试数据：r, g, b 为正整数数组，取值范围 1..n
    r = sorted(randint(1, n) for _ in range(R))
    g = sorted(randint(1, n) for _ in range(G))
    b = sorted(randint(1, n) for _ in range(B))

    # DP 三维数组
    dp = [[[0 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if i > 0 and j > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1]
                    )
                if i > 0 and k > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1]
                    )
                if j > 0 and k > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1]
                    )
    print(dp[-1][-1][-1])


if __name__ == "__main__":
    # 示例：调用 main(30)
    main(30)