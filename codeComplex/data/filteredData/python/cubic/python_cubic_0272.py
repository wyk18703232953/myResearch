import random

def main(n):
    # 这里用 n 控制总规模：R + G + B = n，尽量平均分配
    R = n // 3
    G = (n - R) // 2
    B = n - R - G

    # 生成测试数据：1..1000 的随机整数
    r = [random.randint(1, 1000) for _ in range(R)]
    g = [random.randint(1, 1000) for _ in range(G)]
    b = [random.randint(1, 1000) for _ in range(B)]

    r.sort()
    g.sort()
    b.sort()

    # 由于原程序的 dp 维度固定为 202，这里保持一致
    max_dim = 202
    dp = [[[0] * max_dim for _ in range(max_dim)] for __ in range(max_dim)]

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


# 示例：调用 main(30)
if __name__ == "__main__":
    main(30)