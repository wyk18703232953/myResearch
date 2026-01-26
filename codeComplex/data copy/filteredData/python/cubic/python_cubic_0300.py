def main(n):
    # Map n to sizes of R, G, B so total complexity scales as O(n^3)
    # Choose R = G = B = max(1, n // 3)
    m = max(1, n // 3)
    R = G = B = m

    # Deterministic generation of arrays r, g, b
    # Values increase in different simple patterns
    r = sorted([(i * 2 + 1) % (n + 7) + 1 for i in range(R)])
    g = sorted([(i * 3 + 2) % (n + 11) + 1 for i in range(G)])
    b = sorted([(i * 5 + 3) % (n + 13) + 1 for i in range(B)])

    dp = [[[0 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                best = dp[i][j][k]
                if i > 0 and j > 0:
                    val = dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1]
                    if val > best:
                        best = val
                if i > 0 and k > 0:
                    val = dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1]
                    if val > best:
                        best = val
                if j > 0 and k > 0:
                    val = dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1]
                    if val > best:
                        best = val
                dp[i][j][k] = best

    # print(dp[R][G][B])
    pass
if __name__ == "__main__":
    main(9)