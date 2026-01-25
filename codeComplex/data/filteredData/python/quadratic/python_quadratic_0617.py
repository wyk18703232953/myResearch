def main(n):
    # Interpret n as the length of array a
    if n <= 0:
        return 0

    # Deterministic mapping from n to m and k
    m = max(1, n // 3)
    k = n // 2

    # Deterministic construction of array a of length n
    # Example pattern: a[i] = (i * 2 + 1) % (n + 3)
    a = [((i * 2 + 1) % (n + 3)) for i in range(n)]

    # Original logic
    a = [0] + a
    dp = [0] * 300005
    ans = 0
    for i in range(1, n + 1):
        a[i] += a[i - 1]
        for j in range(1, m + 1):
            if i - j >= 0:
                dp[i] = max(dp[i], a[i] - a[i - j] - k)
        if i - m >= 0:
            dp[i] = max(dp[i], a[i] - a[i - m] + dp[i - m] - k)
        ans = max(ans, dp[i])
    return ans


if __name__ == "__main__":
    # Example deterministic call
    result = main(10)
    print(result)