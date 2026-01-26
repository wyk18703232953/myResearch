def main(n):
    # Map n to sizes of the three arrays in a balanced way
    R = n
    G = max(1, n // 2)
    B = max(1, n // 3)

    # Deterministic generation of r, g, b
    r = [i + 1 for i in range(R)]
    g = [2 * (i + 1) for i in range(G)]
    b = [3 * (i + 1) for i in range(B)]

    r.sort()
    g.sort()
    b.sort()

    dp = [[[0] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]
    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if i > 0 and j > 0:
                    val = dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1]
                    if val > dp[i][j][k]:
                        dp[i][j][k] = val
                if i > 0 and k > 0:
                    val = dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1]
                    if val > dp[i][j][k]:
                        dp[i][j][k] = val
                if j > 0 and k > 0:
                    val = dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1]
                    if val > dp[i][j][k]:
                        dp[i][j][k] = val

    # print(dp[R][G][B])
    pass
if __name__ == "__main__":
    main(5)