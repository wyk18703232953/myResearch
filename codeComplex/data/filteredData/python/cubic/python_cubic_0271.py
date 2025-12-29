import random

def main(n: int):
    # 根据 n 生成三个序列的长度，保证不超过 200（原 dp 维度上限）
    # 这里简单按 n 均分到 a, b, c，并截断到 200
    a = min(200, max(1, n // 3))
    b = min(200, max(1, n // 3))
    c = min(200, max(1, n - a - b))
    
    # 生成测试数据：随机正整数
    R = [random.randint(1, 1000) for _ in range(a)]
    G = [random.randint(1, 1000) for _ in range(b)]
    B = [random.randint(1, 1000) for _ in range(c)]

    # dp 大小最多为 201^3，和原程序一致
    dp = [[[0 for _ in range(201)] for _ in range(201)] for _ in range(201)]

    R.sort()
    G.sort()
    B.sort()

    for i in range(len(R) + 1):
        for j in range(len(G) + 1):
            for k in range(len(B) + 1):
                if i and j:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j - 1][k] + R[i - 1] * G[j - 1]
                    )
                if j and k:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i][j - 1][k - 1] + G[j - 1] * B[k - 1]
                    )
                if i and k:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j][k - 1] + R[i - 1] * B[k - 1]
                    )

    print(dp[len(R)][len(G)][len(B)])


if __name__ == "__main__":
    # 示例：运行规模 n = 60
    main(60)