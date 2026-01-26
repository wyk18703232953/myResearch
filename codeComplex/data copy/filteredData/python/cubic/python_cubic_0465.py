import math

def main(n):
    # Map n to grid dimensions and k (even)
    if n < 4:
        rows = 2
        cols = 2
        k = 2

    else:
        rows = n // 2
        cols = n - rows
        if cols <= 0:
            cols = 1
            rows = n
        k = (n // 2) * 2
        if k == 0:
            k = 2

    # Deterministic generation of horizontal and vertical edge weights
    # horizontal: rows x cols, cost from (i,j) to (i,j+1) stored at [i][j]
    horizontal = [[(i + j + 1) % 7 + 1 for j in range(cols)] for i in range(rows)]
    # vertical: (rows-1) x cols, cost from (i,j) to (i+1,j) stored at [i][j]
    vertical = [[(i * cols + j + 3) % 11 + 1 for j in range(cols)] for i in range(rows - 1)]

    n_rows = rows
    n_cols = cols

    if k % 2 or max(n_rows, n_cols) == 1:
        result = [[-1] * n_cols for _ in range(n_rows)]
        for row in result:
            # print(*row)
            pass
        return

    half_k = k // 2
    dp = [[[0] * (half_k + 1) for _ in range(n_cols)] for _ in range(n_rows)]

    for length in range(1, half_k + 1):
        for i in range(n_rows):
            for j in range(n_cols):
                left_path = math.inf if j == 0 else horizontal[i][j - 1] + dp[i][j - 1][length - 1]
                right_path = math.inf if j == n_cols - 1 else horizontal[i][j] + dp[i][j + 1][length - 1]
                top_path = math.inf if i == 0 else vertical[i - 1][j] + dp[i - 1][j][length - 1]
                bottom_path = math.inf if i == n_rows - 1 else vertical[i][j] + dp[i + 1][j][length - 1]
                dp[i][j][length] = min(left_path, right_path, top_path, bottom_path)

    for i in range(n_rows):
        # print(*[dp[i][j][half_k] * 2 for j in range(n_cols)])
        pass
if __name__ == "__main__":
    main(10)