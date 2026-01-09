def main(n):
    # n is the array length
    if n <= 0:
        return
    # Deterministically generate array l of length n
    l = [(i * 3 + 7) % 1000000007 for i in range(n)]

    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = l[i]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = max(dp[i][j], dp[i][j - 1] ^ dp[i + 1][j])
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = max(dp[i][j], dp[i][j - 1], dp[i + 1][j])

    # Deterministically generate Q queries; here Q = n
    Q = n
    res = []
    for qi in range(Q):
        # generate l, r such that 1 <= l <= r <= n
        lq = qi % n
        rq = n - 1
        if lq > rq:
            lq, rq = rq, lq
        res.append(dp[lq][rq])

    # Output results to keep behavior similar to original program
    for x in res:
        # print(x)
        pass
if __name__ == "__main__":
    main(300)