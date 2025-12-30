import random

MAXN = 202

def main(n: int):
    """
    n 为规模参数，这里将 R, G, B 都设为 n，且需满足 n <= 201（因为 MAXN=202，需要有 0..n 索引）。
    同时生成长度为 R,G,B 的测试数据，值范围在 1..1000 内。
    """
    # 限制规模，避免越界和爆内存
    n = max(1, min(n, MAXN - 1))
    R = G = B = n

    # 生成测试数据
    r = [random.randint(1, 1000) for _ in range(R)]
    g = [random.randint(1, 1000) for _ in range(G)]
    b = [random.randint(1, 1000) for _ in range(B)]

    r.sort()
    g.sort()
    b.sort()

    dp = [[[0] * MAXN for _ in range(MAXN)] for _ in range(MAXN)]

    for i in range(1, R + 1):
        for j in range(1, G + 1):
            dp[i][j][0] = r[i - 1] * g[j - 1] + dp[i - 1][j - 1][0]
    for i in range(1, R + 1):
        for k in range(1, B + 1):
            dp[i][0][k] = r[i - 1] * b[k - 1] + dp[i - 1][0][k - 1]
    for j in range(1, G + 1):
        for k in range(1, B + 1):
            dp[0][j][k] = g[j - 1] * b[k - 1] + dp[0][j - 1][k - 1]

    for i in range(1, R + 1):
        for j in range(1, G + 1):
            for k in range(1, B + 1):
                dp[i][j][k] = max(
                    r[i - 1] * g[j - 1] + dp[i - 1][j - 1][k],
                    r[i - 1] * b[k - 1] + dp[i - 1][j][k - 1],
                    g[j - 1] * b[k - 1] + dp[i][j - 1][k - 1],
                )

    print(dp[R][G][B])


if __name__ == "__main__":
    # 示例：使用规模 n=10 运行
    main(10)