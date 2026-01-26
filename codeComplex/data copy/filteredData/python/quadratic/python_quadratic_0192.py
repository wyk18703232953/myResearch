def main(n):
    # n controls the size of the array l
    if n <= 0:
        return
    # deterministic construction of l
    l = [(i * 3 + 1) ^ (i // 2) for i in range(n)]
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[0][i] = l[i]
    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = dp[i - 1][j] ^ dp[i - 1][j + 1]
    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j + 1])
    # deterministic query generation
    q = n
    for k in range(q):
        x = k % n
        y = n - 1 - (k % n)
        if x > y:
            x, y = y, x
        # print(dp[y - x][x])
        pass
if __name__ == "__main__":
    main(10)