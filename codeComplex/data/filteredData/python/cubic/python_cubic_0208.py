import random

def main(n: int):
    # 这里将规模 n 均分成 R, G, B 三组（相差不超过 1）
    R = n // 3
    G = (n - R) // 2
    B = n - R - G

    # 生成测试数据：随机整数（可按需调整范围）
    # 为保证可重复测试，可设置随机种子，如 random.seed(0)
    r = [random.randint(1, 1000) for _ in range(R)]
    g = [random.randint(1, 1000) for _ in range(G)]
    b = [random.randint(1, 1000) for _ in range(B)]

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    dp = [[[0 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]
    mx = 0

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if i < R and j < G:
                    dp[i + 1][j + 1][k] = max(
                        dp[i + 1][j + 1][k],
                        dp[i][j][k] + r[i] * g[j]
                    )
                if i < R and k < B:
                    dp[i + 1][j][k + 1] = max(
                        dp[i + 1][j][k + 1],
                        dp[i][j][k] + r[i] * b[k]
                    )
                if j < G and k < B:
                    dp[i][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1],
                        dp[i][j][k] + g[j] * b[k]
                    )
                mx = max(mx, dp[i][j][k])

    print(mx)


if __name__ == "__main__":
    # 示例：运行规模为 9 的测试
    main(9)