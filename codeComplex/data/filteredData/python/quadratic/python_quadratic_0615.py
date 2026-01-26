def main(n):
    # Interpret n as the length of array a
    # Deterministically construct m and k based on n
    m = max(1, n // 3 + 2)
    k = n // 2 + 1

    # Deterministically construct array a of length n
    a = [(i * 2 + 1) % 100 for i in range(n)] if n > 0 else []

    if n == 0:
        # print(0)
        pass
        return

    # Core logic from original program
    dp = [[float('-inf')] * m for _ in range(n)]
    dp[0][0] = a[0]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i - 1][j - 1] + a[i]
        dp[i][0] = max(dp[i - 1][m - 1] - k, 0) + a[i]

    result = max(max(row) for row in dp)
    result = max(result - k, 0)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)