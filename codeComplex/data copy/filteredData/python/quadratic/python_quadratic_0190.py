def main(n):
    # n: length of the array s
    if n <= 0:
        return
    # deterministic construction of s based on n
    s = [(i * 17 + 23) % 1000 for i in range(n)]

    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n):
        dp[0][i] = s[i]
    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = dp[i - 1][j] ^ dp[i - 1][j + 1]
    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j + 1], dp[i][j])

    # deterministically generate q and queries (l, r)
    q = n
    queries = []
    for i in range(q):
        l = i % n + 1
        r = n
        if l > r:
            l, r = r, l
        queries.append((l, r))

    for l, r in queries:
        # original logic: dp[r-l][l-1]
        # print(dp[r - l][l - 1])
        pass
if __name__ == "__main__":
    # example deterministic call; adjust n as needed for experiments
    main(10)