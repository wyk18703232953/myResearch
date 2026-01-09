def main(n):
    # Generate deterministic input data based on n
    # a: array of length n
    a = [(i * 37 + 11) % 1000000007 for i in range(n)]

    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n):
        dp[0][i] = a[i]
    for i in range(1, n):
        for j in range(n - i + 1):
            dp[i][j] = dp[i - 1][j] ^ dp[i - 1][j + 1]
    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j + 1])

    # Generate deterministic queries
    # Let number of queries be q = n (for scalability)
    q = n
    outputs = []
    if n == 0:
        # No valid queries when n == 0
        # print()
        pass
        return

    for i in range(q):
        # Deterministic construction of l, r with 1 <= l <= r <= n
        l = (i % n) + 1
        r = ((i * 7) % n) + 1
        if l > r:
            l, r = r, l
        outputs.append(str(dp[r - l][l - 1]))

    # print("\n".join(outputs))
    pass
if __name__ == "__main__":
    main(5)