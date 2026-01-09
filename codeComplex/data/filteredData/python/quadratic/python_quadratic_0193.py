def main(n):
    # n: length of array a
    if n <= 0:
        return
    # Deterministic construction of array a
    # Example: a[i] = (i * 3 + 5) % 1000000007
    a = [(i * 3 + 5) % 1000000007 for i in range(n)]

    # Build dp table as in original code
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n):
        dp[0][i] = a[i]
    for i in range(1, n):
        for j in range(n - i + 1):
            dp[i][j] = dp[i - 1][j] ^ dp[i - 1][j + 1]
    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j + 1])

    # Deterministic generation of queries
    # Let number of queries q scale with n (e.g., q = n)
    q = n
    results = []
    for k in range(q):
        # Generate l, r such that 1 <= l <= r <= n
        # Example pattern: sliding intervals with wrap control
        l = (k % n) + 1
        r = n - (k % (n // 2 + 1))
        if r < l:
            l, r = r, l
        # Ensure bounds
        if l < 1:
            l = 1
        if r > n:
            r = n
        if l > r:
            l, r = r, l
        results.append(dp[r - l][l - 1])

    # Output results to ensure work is not optimized away
    for val in results:
        # print(val)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)