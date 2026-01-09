def main(n):
    # Map n to sizes of R, G, B, each up to 200 (since dp is 202^3)
    max_size = 200
    if n <= 0:
        R = G = B = 0

    else:
        R = min(n, max_size)
        G = min(n // 2 + n % 2, max_size)  # ceil(n/2)
        B = min(n // 3 + (1 if n % 3 else 0), max_size)  # ceil(n/3)

    # Deterministic generation of r, g, b based on sizes
    r = [(i * 2 + 1) for i in range(R)]
    g = [(i * 3 + 2) for i in range(G)]
    b = [(i * 5 + 3) for i in range(B)]

    r.sort()
    g.sort()
    b.sort()

    # dp dimension fixed as in original code: 202 x 202 x 202
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
                if k and j:
                    val = dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1]
                    if val > cur:
                        cur = val
                dp[i][j][k] = cur

    ans = 0
    for plane in dp:
        for row in plane:
            local_max = max(row)
            if local_max > ans:
                ans = local_max

    # print(ans)
    pass
if __name__ == "__main__":
    main(50)