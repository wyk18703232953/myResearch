def main(n):
    # Interpret n as total length of three arrays; split deterministically
    R = n // 3
    G = (n - R) // 2
    B = n - R - G

    # Ensure at least size 1 for non-zero n to keep behavior meaningful
    if n == 0:
        R = G = B = 0

    # Deterministic data generation
    r = [(i * 2 + 1) for i in range(R)]
    g = [(i * 3 + 2) for i in range(G)]
    b = [(i * 5 + 3) for i in range(B)]

    r.sort()
    g.sort()
    b.sort()

    # Initialize 3D DP array
    dp = []
    for i in range(R + 1):
        d = []
        for j in range(G + 1):
            d.append([0] * (B + 1))
        dp.append(d)

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if i + j + k < 2:
                    continue
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

    result = dp[R][G][B]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example: run with a specific n to exercise the algorithm
    main(9)