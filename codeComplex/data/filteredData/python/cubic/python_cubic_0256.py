import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 将 n 按 3 近似均分为 nr, ng, nb，且不超过 200（原 dp 数组上限）
    max_len = 200
    n = min(n, 3 * max_len)

    nr = min(max_len, n // 3)
    ng = min(max_len, (n - nr) // 2)
    nb = min(max_len, n - nr - ng)

    # 生成随机数组，数值范围可自行调整
    r = [random.randint(1, 1000) for _ in range(nr)]
    g = [random.randint(1, 1000) for _ in range(ng)]
    b = [random.randint(1, 1000) for _ in range(nb)]

    r.sort()
    g.sort()
    b.sort()

    # dp 维度基于实际 nr, ng, nb
    dp = [[[0 for _ in range(nb + 1)] for _ in range(ng + 1)] for _ in range(nr + 1)]

    for i in range(nr + 1):
        for j in range(ng + 1):
            for k in range(nb + 1):
                if i and j:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1])
                if i and k:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1])
                if j and k:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1])

    print(dp[nr][ng][nb])


if __name__ == "__main__":
    # 示例：调用 main，规模自定
    main(60)