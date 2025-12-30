import random

def main(n: int):
    # n 用来控制规模，这里将 R, G, B 都设为 n，且 n 不超过 200
    R = G = B = min(n, 200)

    # 生成测试数据，取值范围可按需调整
    r = sorted(random.randint(1, 1000) for _ in range(R))
    g = sorted(random.randint(1, 1000) for _ in range(G))
    b = sorted(random.randint(1, 1000) for _ in range(B))

    # dp[i][j][k]：使用 r 前 i 个、g 前 j 个、b 前 k 个时的最大得分
    # 题目原程序中第三维大小为固定 202，这里也保持一致
    dp = [[[0] * 202 for _ in range(202)] for __ in range(202)]

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
    # 示例：调用 main(5)
    main(5)