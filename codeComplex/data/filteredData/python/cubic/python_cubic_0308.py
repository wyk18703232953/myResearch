import random

def main(n: int):
    # 1. 根据规模 n 生成测试数据
    # 这里简单设定 R = G = B = n
    R = G = B = n

    # 随机生成三种颜色的值，范围可自行调整
    r = [random.randint(1, 10**6) for _ in range(R)]
    g = [random.randint(1, 10**6) for _ in range(G)]
    b = [random.randint(1, 10**6) for _ in range(B)]

    # 与原程序一致：按降序排序
    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    # 2. 原逻辑：三维 DP
    dp = [[[0] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]
    ans = 0

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if j * k > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1]
                    )
                if i * k > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1]
                    )
                if i * j > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1]
                    )
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]

    print(ans)


# 示例：调用 main(5)
if __name__ == "__main__":
    main(5)