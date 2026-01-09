def main(n):
    m = max(1, n // 3)
    k = n // 2
    a = [i % 7 for i in range(1, n + 1)]
    a = [0] + a
    dp = [0] * (n + m + 5)
    ans = 0
    for i in range(1, n + 1):
        a[i] += a[i - 1]
        for j in range(1, m + 1):
            if i - j >= 0:
                dp[i] = max(dp[i], a[i] - a[i - j] - k)
        if i - m >= 0:
            dp[i] = max(dp[i], a[i] - a[i - m] + dp[i - m] - k)
        ans = max(ans, dp[i])
    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)