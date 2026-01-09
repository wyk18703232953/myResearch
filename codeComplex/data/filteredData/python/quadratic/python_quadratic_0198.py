def main(n):
    # Generate deterministic data based on n
    # Interpret n as the size of array a; set number of queries q = n
    a = [(i * 37 + 13) % 1000 for i in range(n)]
    dp = [[0] * n for _ in range(n)]
    f = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        f[i][i] = a[i]
        for j in range(i + 1, n):
            f[i][j] = f[i][j - 1] ^ f[i + 1][j]
    for i in range(n - 1, -1, -1):
        dp[i][i] = f[i][i]
        for j in range(i + 1, n):
            dp[i][j] = max(f[i][j], dp[i][j - 1], dp[i + 1][j])

    # Deterministic queries: q = n, intervals covering various ranges
    q = n
    results = []
    for k in range(q):
        # Map k to a 1-based interval [l, r]
        l = (k % n) + 1
        r = ((k * 2) % n) + 1
        if l > r:
            l, r = r, l
        results.append(dp[l - 1][r - 1])

    # Output all results to keep I/O behavior
    for val in results:
        # print(val)
        pass
if __name__ == "__main__":
    main(5)