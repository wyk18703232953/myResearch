def main(n):
    # Map n to sizes of R, G, B
    # For scalability and determinism, split n approximately into three parts
    R = n // 3
    G = (n + 1) // 3
    B = n - R - G

    # Ensure at least size 1 for non-trivial behavior
    if R == 0:
        R = 1
    if G == 0:
        G = 1
    if B == 0:
        B = 1

    # Deterministic generation of r, g, b arrays based on R, G, B
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
                    val = r[i] * g[j] + dp[i][j][k]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                if i < R and k < B:
                    val = r[i] * b[k] + dp[i][j][k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                if k < B and j < G:
                    val = b[k] * g[j] + dp[i][j][k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
    # print(ans)
    pass
if __name__ == "__main__":
    main(5)