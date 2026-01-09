def main(n):
    # Map n to grid size and k (path length parameter)
    # Choose a square grid with side length s and k proportional to s
    if n <= 0:
        return
    s = max(1, int(n ** 0.5))
    m = s
    n_rows = s
    k = 2 * s  # even k to avoid trivial -1 case

    # Deterministic generation of lr (n_rows x m-1) and ud (n_rows-1 x m)
    # Use simple arithmetic based on indices
    lr = [[(i + j + 1) for j in range(m - 1)] for i in range(n_rows)]
    ud = [[(i + j + 2) for j in range(m)] for i in range(n_rows - 1)]

    if k % 2:
        arr = [-1] * m
        for _ in range(n_rows):
            # print(*arr)
            pass
        return

    kk = k // 2
    INF = 10 ** 10
    dp = [[[INF] * (kk + 1) for _ in range(m)] for _ in range(n_rows)]
    for i in range(n_rows):
        for j in range(m):
            dp[i][j][0] = 0

    for z in range(1, kk + 1):
        for i in range(n_rows):
            for j in range(m):
                if i > 0:
                    val = dp[i - 1][j][z - 1] + ud[i - 1][j]
                    if val < dp[i][j][z]:
                        dp[i][j][z] = val
                if i < n_rows - 1:
                    val = dp[i + 1][j][z - 1] + ud[i][j]
                    if val < dp[i][j][z]:
                        dp[i][j][z] = val
                if j > 0:
                    val = dp[i][j - 1][z - 1] + lr[i][j - 1]
                    if val < dp[i][j][z]:
                        dp[i][j][z] = val
                if j < m - 1:
                    val = dp[i][j + 1][z - 1] + lr[i][j]
                    if val < dp[i][j][z]:
                        dp[i][j][z] = val

    ans = [[dp[i][j][kk] * 2 for j in range(m)] for i in range(n_rows)]
    for i in range(n_rows):
        # print(*ans[i])
        pass
if __name__ == "__main__":
    main(1000)