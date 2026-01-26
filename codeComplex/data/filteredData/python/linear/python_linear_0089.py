def main(n):
    # Generate deterministic test data:
    # Original input: n lines, each with two integers.
    # We choose a simple deterministic pattern so that:
    #   p[i] = (i, i % 5)
    # This gives n pairs and is fully determined by n.
    p = [(-(10**6), 0)] + sorted((i, i % 5) for i in range(1, n + 1))

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
    # Example deterministic call; adjust n as needed for experiments
    main(10)