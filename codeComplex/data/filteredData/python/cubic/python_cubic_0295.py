def main(n):
    # Map n to sizes of the three arrays
    if n <= 0:
        # print(0)
        pass
        return
    R = max(1, n // 3)
    G = max(1, (n - R) // 2)
    B = max(1, n - R - G)

    # Deterministic data generation
    r = [i * 2 + 1 for i in range(R)]
    g = [i * 3 + 2 for i in range(G)]
    b = [i * 5 + 3 for i in range(B)]

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    dp = [[[0 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]
    ans = 0

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
if __name__ == "__main__":
    main(30)