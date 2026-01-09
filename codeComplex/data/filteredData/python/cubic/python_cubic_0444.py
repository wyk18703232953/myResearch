def main(n):
    # Interpret n as grid size with square grid and fixed even k
    # n must be at least 2 for down edges to exist; handle n==1 separately
    if n <= 0:
        return
    m = n
    k = 2 * n  # even number of steps, scales with n

    # Deterministic generation of left and down costs
    # left: n x m-1
    left = [[(i + j + 1) % 7 + 1 for j in range(m - 1)] for i in range(n)]
    # down: n-1 x m
    down = [[(i * m + j + 3) % 9 + 1 for j in range(m)] for i in range(n - 1)]

    dp = [[(-1 if k & 1 else 0) for _ in range(m)] for _ in range(n)]
    if k & 1 == 0:
        for _ in range(k // 2):
            dp1 = [[10 ** 8 for _ in range(m)] for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    if j > 0:
                        dp1[i][j] = min(dp1[i][j], dp[i][j - 1] + 2 * left[i][j - 1])
                    if j < m - 1:
                        dp1[i][j] = min(dp1[i][j], dp[i][j + 1] + 2 * left[i][j])
                    if i > 0:
                        dp1[i][j] = min(dp1[i][j], dp[i - 1][j] + 2 * down[i - 1][j])
                    if i < n - 1:
                        dp1[i][j] = min(dp1[i][j], dp[i + 1][j] + 2 * down[i][j])
            dp = dp1

    for row in dp:
        # print(*row)
        pass
if __name__ == "__main__":
    main(5)