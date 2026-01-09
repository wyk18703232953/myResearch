def main(n):
    # Generate deterministic binary strings a and b based on n
    # Let length of a be n, length of b be 2*n (ensuring m >= n for meaningful computation)
    a = ''.join(str((i // 2) % 2) for i in range(n))
    m = 2 * n if n > 0 else 1
    b = ''.join(str((i * 3) % 2) for i in range(m))

    m = len(b)
    dp = [[0 for _ in range(2)] for _ in range(m + 1)]
    dp[1][0] = int(b[0]) ^ 1
    dp[1][1] = int(b[0])
    for i in range(2, m + 1):
        dp[i][0] = dp[i - 1][0] + (int(b[i - 1]) ^ 1)
        dp[i][1] = dp[i - 1][1] + int(b[i - 1])

    ans = 0
    # If m < n, the original logic would index out of range; to keep logic meaningful,
    # limit iterations accordingly
    limit = min(n, m)
    for i in range(limit):
        count0 = dp[m - limit + i + 1][0] - dp[i][0]
        count1 = dp[m - limit + i + 1][1] - dp[i][1]
        ans += count0 * int(a[i]) + count1 * (int(a[i]) ^ 1)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)