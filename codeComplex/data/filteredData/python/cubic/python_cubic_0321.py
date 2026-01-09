def main(n):
    # Map n to sizes of the three arrays
    # Make total size O(n): divide n roughly into three parts
    c1 = n // 3
    c2 = (n + 1) // 3
    c3 = n - c1 - c2
    if c1 < 0:
        c1 = 0
    if c2 < 0:
        c2 = 0
    if c3 < 0:
        c3 = 0

    # Deterministic generation of arrays r, g, b
    # Use simple arithmetic progressions so that values are sorted
    r = [i + 1 for i in range(c1)]
    g = [2 * (i + 1) for i in range(c2)]
    b = [3 * (i + 1) for i in range(c3)]

    # The original code sorted inputs; here they are already sorted
    # but to preserve structure we can still call sorted (deterministic)
    r = sorted(r)
    g = sorted(g)
    b = sorted(b)

    # 3D DP array
    dp = [[[0 for _ in range(c3 + 1)] for _ in range(c2 + 1)] for _ in range(c1 + 1)]
    for i in range(c1 + 1):
        for j in range(c2 + 1):
            for k in range(c3 + 1):
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

    # print(dp[c1][c2][c3])
    pass
if __name__ == "__main__":
    # Example call for time complexity experiments
    main(30)