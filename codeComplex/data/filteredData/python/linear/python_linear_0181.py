def main(n):
    from itertools import accumulate

    # Interpret n as the array size; keep k as a fixed fraction of n (at least 1)
    if n <= 0:
        return

    k = max(1, n // 3)

    # Deterministic data generation
    # a[i] = i+1, b[i] = (i % 5) - 2  -> periodic small integers including negatives
    a = [i + 1 for i in range(n)]
    b = [(i % 5) - 2 for i in range(n)]

    ps = list(accumulate(a))
    dp = [[0 for _ in range(2)] for _ in range(1 + n)]
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] + a[i - 1] * b[i - 1]
        dp[i][1] = max(
            dp[i - 1][1] + a[i - 1] * b[i - 1],
            ps[i - 1] - (ps[i - k - 1] if i - k - 1 >= 0 else 0) + dp[max(i - k, 0)][0],
        )
    # print(max(max(v) for v in dp))
    pass
if __name__ == "__main__":
    main(10)