def main(n):
    if n <= 0:
        return
    a = [i % 1000 for i in range(1, n + 1)]
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n):
        dp[0][i] = a[i]
    for i in range(1, n):
        for j in range(n - i + 1):
            dp[i][j] = dp[i - 1][j] ^ dp[i - 1][j + 1]
    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j + 1])
    t = n
    for k in range(t):
        l = (k % n) + 1
        r = n
        if l > r:
            l, r = r, l
        print(dp[r - l][l - 1])


if __name__ == "__main__":
    main(10)