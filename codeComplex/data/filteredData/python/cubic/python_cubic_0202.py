import random

def main(n: int):
    # 生成规模：将 n 分成 R, G, B 三个非负整数
    # 保证总规模在 O(n)，同时每个颜色都有一定概率非零
    if n < 3:
        R = G = B = max(1, n)
    else:
        R = random.randint(1, n)
        G = random.randint(1, n)
        B = random.randint(1, n)

    # 生成测试数据：随机正整数（可根据需要调整范围）
    r = [random.randint(1, 10**4) for _ in range(R)]
    g = [random.randint(1, 10**4) for _ in range(G)]
    b = [random.randint(1, 10**4) for _ in range(B)]

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    dp = [[[0] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                c = False
                if i < R and j < G:
                    dp[i + 1][j + 1][k] = max(
                        dp[i + 1][j + 1][k],
                        dp[i][j][k] + r[i] * g[j]
                    )
                    c = True
                if j < G and k < B:
                    dp[i][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1],
                        dp[i][j][k] + g[j] * b[k]
                    )
                    c = True
                if k < B and i < R:
                    dp[i + 1][j][k + 1] = max(
                        dp[i + 1][j][k + 1],
                        dp[i][j][k] + b[k] * r[i]
                    )
                    c = True

                if not c:
                    if i < R:
                        dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
                    if j < G:
                        dp[i][j + 1][k] = max(dp[i][j + 1][k], dp[i][j][k])
                    if k < B:
                        dp[i][j][k + 1] = max(dp[i][j][k + 1], dp[i][j][k])

    ans = 0
    for i in dp:
        for j in i:
            ans = max(ans, max(j))

    print(ans)


if __name__ == "__main__":
    # 示例：n 可根据需要调整
    main(5)