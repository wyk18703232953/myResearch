def main(n):
    import random

    # 根据规模 n 生成 R,G,B 的大小，这里简单设为都等于 n
    R = G = B = n

    # 生成测试数据：随机正整数
    # 也可以根据需要改成其他分布或范围
    r = sorted(random.randint(1, 1000) for _ in range(R))
    g = sorted(random.randint(1, 1000) for _ in range(G))
    b = sorted(random.randint(1, 1000) for _ in range(B))

    # DP 三维数组
    dp = [[[0] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]

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

    # 返回结果，若需要打印可改为 print(dp[R][G][B])
    return dp[R][G][B]


if __name__ == "__main__":
    # 示例运行，可自行修改 n
    result = main(3)
    print(result)