def main(n):
    # Map n to sizes of R, G, B such that total size scales with n
    # Here we choose R = n, G = n, B = n for cubic DP size O(n^3)
    R = n
    G = n
    B = n

    # Deterministic data generation
    # Use decreasing sequences to mimic original "sorted(..., reverse=True)"
    r = [R - i for i in range(R)]
    g = [G - i for i in range(G)]
    b = [B - i for i in range(B)]

    ans = 0
    dp = [[[0 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]
    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if i < R and j < G:
                    val = dp[i][j][k] + r[i] * g[j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                if j < G and k < B:
                    val = dp[i][j][k] + g[j] * b[k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val
                if i < R and k < B:
                    val = dp[i][j][k] + r[i] * b[k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    main(10)