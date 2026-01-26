def main(n):
    # n: length of array a
    # We also define number of queries q as n for scalability.
    if n <= 0:
        return

    # Deterministic construction of array a of length n
    # Example pattern: a[i] = (i * 31 + 7) ^ (i // 2)
    a = [(i * 31 + 7) ^ (i // 2) for i in range(n)]

    # Build dp table exactly as in original program
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n):
        dp[0][i] = a[i]
    for i in range(1, n):
        for j in range(n - i + 1):
            dp[i][j] = dp[i - 1][j] ^ dp[i - 1][j + 1]
    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j + 1])

    # Deterministic construction of queries
    # We create q = n queries with 1 <= l <= r <= n.
    # Pattern: l increases, r wraps in a simple way.
    q = n
    results = []
    for i in range(q):
        l = (i % n) + 1
        r = n - (i % n)
        if l > r:
            l, r = r, l
        # Ensure within bounds
        l = max(1, min(l, n))
        r = max(1, min(r, n))
        if l > r:
            l, r = r, l
        results.append(dp[r - l][l - 1])

    # Output results to observe behavior / for timing
    for ans in results:
        # print(ans)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)