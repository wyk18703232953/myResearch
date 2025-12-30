import random

def main(n: int):
    # 生成规模：R, G, B 都与 n 相关（不超过 200，以匹配原始 dp 数组大小）
    R = min(n, 200)
    G = min(max(n // 2, 1), 200)
    B = min(max(n // 3, 1), 200)

    # 生成测试数据：随机正整数
    random.seed(0)  # 固定种子便于复现
    r = [random.randint(1, 1000) for _ in range(R)]
    g = [random.randint(1, 1000) for _ in range(G)]
    b = [random.randint(1, 1000) for _ in range(B)]

    r.sort()
    g.sort()
    b.sort()

    # dp[i][j][k] 表示从 r 选 i 个、g 选 j 个、b 选 k 个后的最大价值
    # 原代码中 dp 维度固定为 202，这里保持一致
    dp = [[[0] * 202 for _ in range(202)] for _ in range(202)]

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if i and j:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1])
                if i and k:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1])
                if j and k:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1])

    print(dp[R][G][B])


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)