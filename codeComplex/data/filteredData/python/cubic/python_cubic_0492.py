def main(n):
    # Interpret n as both the grid dimension and the step parameter
    # n must be at least 2 to make sense for n-1 in b
    if n < 2:
        n = 2
    # Define grid dimensions and k deterministically from n
    rows = n
    cols = n
    k = n  # path length parameter

    # Deterministically generate a (rows x cols) and b ((rows-1) x cols)
    # a[i][j] is "horizontal" cost between (i,j) and (i,j+1)
    # b[i][j] is "vertical" cost between (i,j) and (i+1,j)
    a = [[(i + j + 1) for j in range(cols)] for i in range(rows)]
    b = [[(i * 2 + j + 1) for j in range(cols)] for i in range(rows - 1)]

    if k % 2 == 1:
        for _ in range(rows):
            # print(*([-1] * cols))
            pass
        return
    k //= 2

    INF = 10 ** 18
    dp = [[[INF] * (k + 1) for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            dp[i][j][0] = 0

    for v in range(1, k + 1):
        for i in range(rows):
            for j in range(cols):
                if i > 0:
                    dp[i][j][v] = min(dp[i - 1][j][v - 1] + b[i - 1][j], dp[i][j][v])
                if i < rows - 1:
                    dp[i][j][v] = min(dp[i + 1][j][v - 1] + b[i][j], dp[i][j][v])
                if j > 0:
                    dp[i][j][v] = min(dp[i][j - 1][v - 1] + a[i][j - 1], dp[i][j][v])
                if j < cols - 1:
                    dp[i][j][v] = min(dp[i][j + 1][v - 1] + a[i][j], dp[i][j][v])

    for i in range(rows):
        row_out = []
        for j in range(cols):
            row_out.append(dp[i][j][k] * 2)
        # print(*row_out)
        pass
if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(5)