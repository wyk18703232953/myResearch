def main(n):
    m = max(1, n // 3)
    k = max(1, n // 5)
    a = [(i * 2 + 3) % (n + 7) for i in range(n)]

    best = 0
    dp = [0] * (n + 1)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]

    for i in range(n):
        b2 = 0
        left = max(-1, i - m)
        for j in range(left, i + 1):
            s = prefix[i + 1] - prefix[j + 1]
            b2 = max(b2, dp[j] - k + s)
        dp[i] = max(b2, a[i] - k)
        best = max(best, dp[i])

    print(best)


if __name__ == "__main__":
    main(10)