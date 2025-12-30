import random

def main(n):
    # 根据规模 n 生成 R,G,B，并生成对应长度的数组
    # 这里示例为：R = G = B = n
    R = G = B = n

    # 生成测试数据：1..100 之间的随机整数
    r = [random.randint(1, 100) for _ in range(R)]
    g = [random.randint(1, 100) for _ in range(G)]
    b = [random.randint(1, 100) for _ in range(B)]

    r.sort()
    g.sort()
    b.sort()

    dp = [[[0 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]

    for i in range(1, R + 1):
        for j in range(1, G + 1):
            dp[i][j][0] = dp[i - 1][j - 1][0] + r[i - 1] * g[j - 1]

    for j in range(1, G + 1):
        for k in range(1, B + 1):
            dp[0][j][k] = dp[0][j - 1][k - 1] + b[k - 1] * g[j - 1]

    for i in range(1, R + 1):
        for k in range(1, B + 1):
            dp[i][0][k] = dp[i - 1][0][k - 1] + r[i - 1] * b[k - 1]

    for i in range(1, R + 1):
        for j in range(1, G + 1):
            for k in range(1, B + 1):
                ri, gj, bk = r[i - 1], g[j - 1], b[k - 1]
                mx = max(ri, gj, bk)
                if mx == ri:
                    dp[i][j][k] = max(
                        dp[i - 1][j - 1][k] + ri * gj,
                        dp[i - 1][j][k - 1] + ri * bk
                    )
                elif mx == gj:
                    dp[i][j][k] = max(
                        dp[i - 1][j - 1][k] + ri * gj,
                        dp[i][j - 1][k - 1] + gj * bk
                    )
                else:
                    dp[i][j][k] = max(
                        dp[i][j - 1][k - 1] + bk * gj,
                        dp[i - 1][j][k - 1] + ri * bk
                    )

    print(dp[R][G][B])


if __name__ == "__main__":
    # 示例：调用 main(3) 进行测试
    main(3)