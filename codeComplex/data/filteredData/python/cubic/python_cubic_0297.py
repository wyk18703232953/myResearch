import random

def main(n):
    # 生成规模：R, G, B 总和约为 n
    # 简单策略：尽量平均分配
    if n <= 0:
        print(0)
        return

    R = n // 3
    G = (n - R) // 2
    B = n - R - G

    # 保证非零长度（如果 n 很小）
    if R == 0 and n > 0:
        R = 1
    if R + G + B > n:
        # 调整到不超过 n（理论上上面分配不会超过，这里只是保险）
        while R + G + B > n and B > 0:
            B -= 1
        while R + G + B > n and G > 0:
            G -= 1
        while R + G + B > n and R > 0:
            R -= 1

    # 生成测试数据（正整数）
    r = sorted([random.randint(1, 1000) for _ in range(R)], reverse=True)
    g = sorted([random.randint(1, 1000) for _ in range(G)], reverse=True)
    b = sorted([random.randint(1, 1000) for _ in range(B)], reverse=True)

    # 原始算法
    dp = [[[0 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]
    ans = 0
    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if i < R and j < G:
                    dp[i + 1][j + 1][k] = max(
                        dp[i + 1][j + 1][k],
                        dp[i][j][k] + r[i] * g[j]
                    )
                if j < G and k < B:
                    dp[i][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1],
                        dp[i][j][k] + g[j] * b[k]
                    )
                if i < R and k < B:
                    dp[i + 1][j][k + 1] = max(
                        dp[i + 1][j][k + 1],
                        dp[i][j][k] + r[i] * b[k]
                    )
                ans = max(ans, dp[i][j][k])

    print(ans)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)