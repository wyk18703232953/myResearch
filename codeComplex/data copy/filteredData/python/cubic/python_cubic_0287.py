def main(n):
    # Interpret n as total size; split into three groups R, G, B as evenly as possible
    if n <= 0:
        # print(0)
        pass
        return

    R = n // 3
    G = (n - R) // 2
    B = n - R - G

    # Generate deterministic arrays based on R, G, B
    # Use simple arithmetic patterns to construct values
    r = [(i * 2 + 1) for i in range(R)]
    g = [(i * 3 + 2) for i in range(G)]
    b = [(i * 5 + 3) for i in range(B)]

    area = 0
    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    dp = [[[0] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if i > 0 and j > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1])
                if j > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1])
                if i > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1])
                if dp[i][j][k] > area:
                    area = dp[i][j][k]

    # print(area)
    pass
if __name__ == "__main__":
    # Example call for time-complexity experiments
    main(9)