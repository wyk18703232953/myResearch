def main(n):
    # Interpret n as the array length; choose a fixed k dependent on n but deterministic
    if n <= 0:
        return
    k = max(1, n // 3)

    # Deterministic construction of arrays a and b
    a = [(i * 2 + 1) % 100 for i in range(n)]
    b = [(i * 3 + 7) % 50 for i in range(n)]

    from itertools import accumulate

    ps = list(accumulate(a))
    dp = [[0 for _ in range(2)] for _ in range(1 + n)]

    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] + a[i - 1] * b[i - 1]
        base = dp[i - 1][1] + a[i - 1] * b[i - 1]
        segment_sum = ps[i - 1] - (ps[i - k - 1] if i - k - 1 >= 0 else 0)
        alt = segment_sum + dp[max(i - k, 0)][0]
        dp[i][1] = max(base, alt)

    # print(max(dp[n]))
    pass
if __name__ == "__main__":
    main(10)