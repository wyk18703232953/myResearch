def main(n):
    # Generate deterministic data based on n
    # Interpret n as the length of array a; number of queries q also derived from n
    a = [(i * 17 + 23) % 256 for i in range(n)]
    dp = [[0] * n for _ in range(n)]
    f = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        f[i][i] = dp[i][i] = a[i]
        for j in range(i + 1, n):
            f[i][j] = f[i][j - 1] ^ f[i + 1][j]
            dp[i][j] = max(f[i][j], dp[i][j - 1], dp[i + 1][j])

    # Deterministically generate q and queries (l, r)
    q = n  # number of queries equals n
    results = []
    for k in range(q):
        # Generate l, r in [1, n], ensure l <= r
        l = (k % n) + 1
        r = ((k * 3) % n) + 1
        if l > r:
            l, r = r, l
        results.append(dp[l - 1][r - 1])

    # Output results to keep observable behavior
    for val in results:
        # print(val)
        pass
if __name__ == "__main__":
    main(5)