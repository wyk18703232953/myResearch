def main(n):
    MAXN = 202

    # Map n to sizes of R, G, B such that they are all <= 200 and scale with n
    # Use a simple deterministic partition of n into three parts
    R = min(MAXN - 2, max(1, n // 3))
    G = min(MAXN - 2, max(1, (n - R) // 2))
    B = min(MAXN - 2, max(1, n - R - G))
    # Ensure at least 1 in each, adjust if needed
    if B <= 0:
        B = 1
        if G > 1:
            G -= 1
        elif R > 1:
            R -= 1

    # Deterministic generation of r, g, b arrays
    r = [(i + 1) for i in range(R)]
    g = [(i + 2) for i in range(G)]
    b = [(i + 3) for i in range(B)]

    r.sort()
    g.sort()
    b.sort()

    dp = [[[0] * MAXN for _ in range(MAXN)] for _ in range(MAXN)]

    for i in range(1, R + 1):
        for j in range(1, G + 1):
            dp[i][j][0] = r[i - 1] * g[j - 1] + dp[i - 1][j - 1][0]

    for i in range(1, R + 1):
        for k in range(1, B + 1):
            dp[i][0][k] = r[i - 1] * b[k - 1] + dp[i - 1][0][k - 1]

    for j in range(1, G + 1):
        for k in range(1, B + 1):
            dp[0][j][k] = g[j - 1] * b[k - 1] + dp[0][j - 1][k - 1]

    for i in range(1, R + 1):
        for j in range(1, G + 1):
            for k in range(1, B + 1):
                dp[i][j][k] = max(
                    r[i - 1] * g[j - 1] + dp[i - 1][j - 1][k],
                    r[i - 1] * b[k - 1] + dp[i - 1][j][k - 1],
                    g[j - 1] * b[k - 1] + dp[i][j - 1][k - 1],
                )

    # print(dp[R][G][B])
    pass
if __name__ == "__main__":
    # Example call; change n to scale input size
    main(30)