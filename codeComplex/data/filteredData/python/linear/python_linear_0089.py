def main(n):
    # Generate deterministic test data: list of (x, y) pairs
    # Example pattern: p[i] = (i, i % max(1, n//3 + 1))
    p = [((i + 1), ((i + 1) % (max(1, n // 3 + 1)))) for i in range(n)]
    p = [(-(10**6), 0)] + sorted(p)

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        l, r = 0, i
        while r - l > 1:
            mid = (l + r) >> 1
            if p[i][0] - p[i][1] <= p[mid][0]:
                r = mid

            else:
                l = mid
        dp[i] = i - r + dp[r - 1]
    ans = min(dp[i] + (n - i) for i in range(1, n + 1))
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)