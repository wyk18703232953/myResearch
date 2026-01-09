def main(n):
    # Interpret n as total size, split into three colors as evenly as possible
    c1 = n // 3
    c2 = (n - c1) // 2
    c3 = n - c1 - c2

    # Deterministic data generation
    r = sorted([(i * 2 + 1) for i in range(c1)])
    g = sorted([(i * 3 + 2) for i in range(c2)])
    b = sorted([(i * 5 + 3) for i in range(c3)])

    dp = [[[0 for _ in range(c3 + 1)] for _ in range(c2 + 1)] for _ in range(c1 + 1)]
    for i in range(c1 + 1):
        for j in range(c2 + 1):
            for k in range(c3 + 1):
                if i > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k])
                if j > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k])
                if k > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j][k - 1])
                if i > 0 and j > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1])
                if i > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1])
                if j > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1])
    return dp[c1][c2][c3]


if __name__ == "__main__":
    # example: run with a chosen scale n
    result = main(10)
    # print(result)
    pass