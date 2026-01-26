def main(n):
    # Map n to sizes of R, G, B
    # Choose them roughly balanced and O(n) total length
    R = n
    G = n // 2 + 1
    B = n // 3 + 1

    # Deterministic generation of arrays r, g, b
    # Ensure they are sorted in decreasing order as in original code
    r = sorted([(i * 2 + 1) for i in range(R)], reverse=True)
    g = sorted([(i * 3 + 2) for i in range(G)], reverse=True)
    b = sorted([(i * 5 + 3) for i in range(B)], reverse=True)

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
if __name__ == "__main__":
    main(10)