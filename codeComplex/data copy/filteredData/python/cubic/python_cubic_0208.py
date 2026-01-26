def main(n):
    # Map n to sizes of the three arrays
    # Simple deterministic mapping: split n into three parts
    R = n // 3
    G = (n + 1) // 3
    B = n - R - G
    if R <= 0:
        R = 1
    if G <= 0:
        G = 1
    if B <= 0:
        B = 1

    # Deterministically generate r, g, b based on their sizes
    r = [(i * 2 + 1) % 1000 + 1 for i in range(R)]
    g = [(i * 3 + 2) % 1000 + 1 for i in range(G)]
    b = [(i * 5 + 3) % 1000 + 1 for i in range(B)]

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    dp = [[[0 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]
    mx = 0

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if i < R and j < G:
                    val = dp[i][j][k] + r[i] * g[j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                if i < R and k < B:
                    val = dp[i][j][k] + r[i] * b[k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                if j < G and k < B:
                    val = dp[i][j][k] + g[j] * b[k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val
                if dp[i][j][k] > mx:
                    mx = dp[i][j][k]

    # print(mx)
    pass
if __name__ == "__main__":
    main(6)