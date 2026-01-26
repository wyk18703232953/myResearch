def main(n):
    # Map n to sizes of R, G, B with upper cap 200 (original dp dimension limit 202)
    if n < 1:
        n = 1
    max_size = 200
    R = min(n, max_size)
    G = min(n, max_size)
    B = min(n, max_size)

    # Deterministic generation of arrays r, g, b
    r = [(i * 2 + 1) for i in range(R)]
    g = [(i * 3 + 2) for i in range(G)]
    b = [(i * 5 + 3) for i in range(B)]

    r.sort()
    g.sort()
    b.sort()

    # dp dimension is fixed as in original code (up to 201 indices inclusive)
    dp = [[[0] * 202 for _ in range(202)] for _ in range(202)]

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                val = dp[i][j][k]
                if i and j:
                    v = dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1]
                    if v > val:
                        val = v
                if i and k:
                    v = dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1]
                    if v > val:
                        val = v
                if j and k:
                    v = dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1]
                    if v > val:
                        val = v
                dp[i][j][k] = val

    # print(dp[R][G][B])
    pass
if __name__ == "__main__":
    main(50)