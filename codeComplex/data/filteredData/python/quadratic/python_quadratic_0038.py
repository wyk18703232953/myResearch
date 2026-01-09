def main(n):
    M = 10**9 + 7

    # Deterministic generation of s: alternate 'f' and 's'
    s = [('f' if i % 2 == 0 else 's') for i in range(n)]

    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n):
        for j in range(n):
            if i >= 1 and s[i - 1] == 'f':
                if j >= 1:
                    dp[i][j] = dp[i - 1][j - 1] - dp[i - 1][j]
            elif i >= 1:
                dp[i][j] = dp[i - 1][j]
            dp[i][j] %= M
        for k in range(n - 1, -1, -1):
            dp[i][k] = (dp[i][k] + dp[i][k + 1]) % M

    # print(dp[n - 1][0] % M)
    pass
if __name__ == "__main__":
    main(10)