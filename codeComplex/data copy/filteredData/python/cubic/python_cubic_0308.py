def main(n):
    # Interpret n as total size, split into three non-negative parts R, G, B
    R = n // 3
    G = (n + 1) // 3
    B = n - R - G
    r = list(range(R, 0, -1))
    g = list(range(G, 0, -1))
    b = list(range(B, 0, -1))

    dp = [[[0] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]
    ans = 0
    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if j * k > 0:
                    dp[i][j][k] = max(dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1], dp[i][j][k])
                if i * k > 0:
                    dp[i][j][k] = max(dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1], dp[i][j][k])
                if i * j > 0:
                    dp[i][j][k] = max(dp[i - 1][j - 1][k] + g[j - 1] * r[i - 1], dp[i][j][k])
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    main(6)