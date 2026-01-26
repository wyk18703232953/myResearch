def main(n):
    # Map n to sizes of R, G, B in a deterministic way
    # Split n roughly into three parts
    R = n // 3
    G = (n + 1) // 3
    B = n - R - G

    # Ensure at least size 1 for non-trivial behavior
    if R == 0 and n > 0:
        R = 1
    if G == 0 and n > 1:
        G = 1
    if B == 0 and n > 2:
        B = 1

    # Regenerate n as sum of R, G, B (not strictly necessary but keeps consistency)
    # Generate deterministic data for r, g, b
    # Use decreasing values, similar to sorted(reverse=True)
    r = sorted([(i * 2 + 1) for i in range(R)], reverse=True)
    g = sorted([(i * 3 + 2) for i in range(G)], reverse=True)
    b = sorted([(i * 5 + 3) for i in range(B)], reverse=True)

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
                    val = dp[i][j][k] + b[k] * r[i]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)