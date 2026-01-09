def main(n):
    # Interpret n as the length of array a
    # Generate deterministic parameters m, k based on n
    m = max(1, n // 3 + 2)
    k = n // 2 + 1

    # Generate deterministic array a of length n
    a = [(i * 2 - (i % 3)) for i in range(n)]

    dp = [[float('-inf')] * m for _ in range(n)]
    if n > 0:
        dp[0][0] = a[0]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i - 1][j - 1] + a[i]
        dp[i][0] = max(dp[i - 1][m - 1] - k, 0) + a[i]
    if n == 0:
        # print(0)
        pass
        return
    ans = max(max(row) for row in dp)
    ans = max(ans - k, 0)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)