def main(n):
    if n <= 0:
        return
    # Generate a deterministic array a of length n
    # Example pattern: a[i] = (i * 3 + 1) % 1000000007
    a = [(i * 3 + 1) % 1000000007 for i in range(n)]

    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = a[i]

    count = 1
    for i in range(n - 1):
        for j in range(n - i - 1):
            dp[j][j + count] = dp[j][j + count - 1] ^ dp[j + 1][j + count]
        count += 1

    count = 1
    for i in range(n - 1):
        for j in range(n - i - 1):
            dp[j][j + count] = max(dp[j][j + count], dp[j][j + count - 1], dp[j + 1][j + count])
        count += 1

    # Generate a deterministic set of queries.
    # Map n to number of queries; here choose q = n (at least 1).
    q = max(1, n)
    results = []
    for i in range(q):
        # Deterministically generate (l, r) with 0 <= l <= r < n
        l = i % n
        r = (i * 2 + 1) % n
        if l > r:
            l, r = r, l
        results.append(dp[l][r])

    for res in results:
        print(res)


if __name__ == "__main__":
    main(5)