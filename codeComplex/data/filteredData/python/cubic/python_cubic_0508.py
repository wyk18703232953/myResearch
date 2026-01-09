def main(n):
    # Interpret n as grid size parameter:
    # n >= 2 -> grid n x n, k = 2 * n (even)
    # n == 1 -> minimal case, use 1x1 grid and k = 2
    if n <= 1:
        rows = 1
        cols = 1
        k = 2

    else:
        rows = n
        cols = n
        k = 2 * n

    # Deterministic generation of ea (rows x (cols-1)) and eb ((rows-1) x cols)
    # Ensure shapes match original constraints: ea: rows x cols, eb: (rows-1) x cols
    # In original code ea has shape [n][m-1?] actually ea is used with j and j-1, j < m-1 indexing.
    # Here we keep ea as rows x (cols-1) logically but allocate as rows x cols and only use valid indices.
    ea = [[(i * cols + j + 1) for j in range(cols)] for i in range(rows)]
    eb = [[(i * cols + j + 1) * 2 for j in range(cols)] for i in range(rows - 1)]

    m = cols
    n_rows = rows

    dp = [[[10**20] * m for _ in range(n_rows)] for _ in range(k // 2 + 1)]
    dp[0] = [[0] * m for _ in range(n_rows)]

    def show_ans():
        for line in dp[-1]:
            # print(' '.join(map(str, [d * 2 for d in line])))
            pass
    if k % 2:
        for _ in range(n_rows):
            # print(' '.join(['-1'] * m))
            pass
        return

    for t in range(1, k // 2 + 1):
        for i in range(n_rows):
            for j in range(m):
                if i:
                    dp[t][i][j] = min(dp[t][i][j], dp[t - 1][i - 1][j] + eb[i - 1][j])
                if i < n_rows - 1:
                    dp[t][i][j] = min(dp[t][i][j], dp[t - 1][i + 1][j] + eb[i][j])
                if j:
                    dp[t][i][j] = min(dp[t][i][j], dp[t - 1][i][j - 1] + ea[i][j - 1])
                if j < m - 1:
                    dp[t][i][j] = min(dp[t][i][j], dp[t - 1][i][j + 1] + ea[i][j])
    show_ans()


if __name__ == "__main__":
    main(5)