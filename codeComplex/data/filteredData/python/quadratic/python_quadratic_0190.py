def main(n):
    # Generate deterministic data based on n
    # Original: n, then array s of length n, then q queries and their ranges
    s = [(i * 2 + 1) for i in range(n)]  # deterministic sequence of length n

    # Build dp as in original code
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n):
        dp[0][i] = s[i]
    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = dp[i - 1][j] ^ dp[i - 1][j + 1]
    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j + 1], dp[i][j])

    # Deterministically generate q and queries (l, r)
    # Let q scale with n, e.g. q = n
    q = n
    queries = []
    for i in range(q):
        # Generate intervals within [1, n], ensure l <= r
        l = (i % n) + 1
        r = n - (i % n)
        if l > r:
            l, r = r, l
        queries.append((l, r))

    # Execute queries and collect outputs
    outputs = []
    for l, r in queries:
        outputs.append(dp[r - l][l - 1])

    return outputs


if __name__ == "__main__":
    # Example call for testing / timing
    result = main(10)
    for val in result:
        # print(val)
        pass