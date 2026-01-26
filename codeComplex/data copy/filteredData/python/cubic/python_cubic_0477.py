def main(n):
    # Map n to problem parameters:
    # Let n be the grid dimension (square grid), and derive k from n.
    # Ensure n is at least 2 to avoid degenerate wv dimensions.
    if n < 2:
        n = 2
    m = n
    # Let k be an even number related to n, but capped to 24 (since dp depth is 24 max usable)
    # Original dp has size [..][..][25], and x goes up to 24 effectively (k/x even).
    # We keep k even and reasonably bounded by 24 for correctness with the fixed dp size.
    k = 2 * min(12, n)

    # Deterministic generation of wh (n x (m-1)) and wv ((n-1) x m)
    # Use simple arithmetic patterns: increasing sequences based on indices.
    wh = []
    for i in range(n):
        row = [(i + 1) + (j + 1) for j in range(m - 1)]
        wh.append(row)

    wv = []
    for i in range(n - 1):
        row = [(i + 1) * (j + 2) for j in range(m)]
        wv.append(row)

    if k % 2 != 0:
        ans = [[-1 for _ in range(m)] for _ in range(n)]
        for res in ans:
            # print(*res)
            pass
        return

    # dp dimensions are fixed as in original code
    MAX_N = 505
    MAX_M = 505
    MAX_K = 25

    # Initialize dp with zeros
    dp = [[[0 for _ in range(MAX_K)] for _ in range(MAX_M)] for _ in range(MAX_N)]

    INF = 1234567890

    # The original loops for x up to 20; we keep that,
    # but only meaningful up to x <= k and x <= 24 due to divisibility and even checks.
    for x in range(1, 21):
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j][x] = INF
                if i != n:
                    dp[i][j][x] = min(dp[i][j][x], dp[i + 1][j][x - 1] + wv[i - 1][j - 1])
                if i != 1:
                    dp[i][j][x] = min(dp[i][j][x], dp[i - 1][j][x - 1] + wv[i - 2][j - 1])
                if j != m:
                    dp[i][j][x] = min(dp[i][j][x], dp[i][j + 1][x - 1] + wh[i - 1][j - 1])
                if j != 1:
                    dp[i][j][x] = min(dp[i][j][x], dp[i][j - 1][x - 1] + wh[i - 1][j - 2])

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            ans = INF
            for x in range(1, k + 1):
                if x < MAX_K and (k % x == 0) and ((k // x) % 2 == 0):
                    ans = min(ans, dp[i][j][x] * (k // x))
            # print(ans, end=" ")
            pass
        # print()
        pass
if __name__ == "__main__":
    # Example deterministic call; change  to scale input size
    main(10)