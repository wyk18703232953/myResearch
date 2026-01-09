def main(n):
    a = [(i * 3 + 1) % (n + 7) for i in range(n)]
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
    q = n
    for i in range(q):
        l = i % n
        r = n - 1
        if l > r:
            l, r = r, l
        # print(dp[l][r])
        pass
if __name__ == "__main__":
    main(10)