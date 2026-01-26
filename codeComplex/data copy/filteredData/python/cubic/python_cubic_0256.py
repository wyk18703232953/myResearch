def main(n):
    # Map n to nr, ng, nb with an upper cap of 200 (since dp is 201^3)
    # Ensure they are all at least 1 when n > 0
    limit = 200
    nr = min(max(n, 1), limit)
    ng = min(max(n * 2 // 3 + 1, 1), limit)
    nb = min(max(n // 2 + 1, 1), limit)

    # Deterministic generation of r, g, b
    r = [(i * 2 + 1) % 1000 + 1 for i in range(nr)]
    g = [(i * 3 + 2) % 1000 + 1 for i in range(ng)]
    b = [(i * 5 + 3) % 1000 + 1 for i in range(nb)]

    r.sort()
    g.sort()
    b.sort()

    # DP array sized according to 201 as in original code
    dp = [[[0 for _ in range(201)] for _ in range(201)] for _ in range(201)]

    for i in range(nr + 1):
        for j in range(ng + 1):
            for k in range(nb + 1):
                val = dp[i][j][k]
                if i and j:
                    cand = dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1]
                    if cand > val:
                        val = cand
                if i and k:
                    cand = dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1]
                    if cand > val:
                        val = cand
                if j and k:
                    cand = dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1]
                    if cand > val:
                        val = cand
                dp[i][j][k] = val

    # print(dp[nr][ng][nb])
    pass
if __name__ == "__main__":
    main(50)