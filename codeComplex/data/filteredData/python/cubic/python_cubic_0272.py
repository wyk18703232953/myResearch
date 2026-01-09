def main(n):
    # Map n to sizes of R, G, B such that each is at most 201 (since dp dimension is 202)
    # Use a simple deterministic mapping:
    # Let total = min(n, 600), and split roughly into three parts.
    total = min(max(0, n), 600)
    R = total // 3
    G = (total - R) // 2
    B = total - R - G
    R = min(R, 201)
    G = min(G, 201)
    B = min(B, 201)

    # Deterministically generate sequences r, g, b based on R, G, B
    r = [(i * 2 + 1) % 1000 for i in range(R)]
    g = [(i * 3 + 2) % 1000 for i in range(G)]
    b = [(i * 5 + 3) % 1000 for i in range(B)]

    r.sort()
    g.sort()
    b.sort()

    # dp dimension is fixed as in original code: 202 x 202 x 202
    dp = [[[0] * 202 for _ in range(202)] for _ in range(202)]

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                cur = dp[i][j][k]
                if i and j:
                    val = dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1]
                    if val > cur:
                        cur = val
                if i and k:
                    val = dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1]
                    if val > cur:
                        cur = val
                if j and k:
                    val = dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1]
                    if val > cur:
                        cur = val
                dp[i][j][k] = cur

    # print(dp[R][G][B])
    pass
if __name__ == "__main__":
    main(100)