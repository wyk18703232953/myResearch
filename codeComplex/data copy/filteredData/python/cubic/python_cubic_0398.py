def main(n):
    import math

    # Map n to grid size and path length deterministically
    # Ensure at least 1x1 grid
    n = max(1, int(n))
    # Define n, m as functions of n so total cells ~ n^2
    rows = max(1, n // 2)
    cols = max(1, n - rows)

    # Ensure k is even and at least 2 (when possible)
    # Let k grow with n but cap so it doesn't explode
    k = 2 * max(1, min(rows + cols, 10))

    # Deterministic weight generation
    # horizontal[i][j] is weight between (i,j) and (i,j+1)
    horizontal = [[(i + j + 1) for j in range(cols - 1)] for i in range(rows)]
    # vertical[i][j] is weight between (i,j) and (i+1,j)
    vertical = [[(i + j + 2) for j in range(cols)] for i in range(rows - 1)]

    n_rows, n_cols = rows, cols
    n, m = n_rows, n_cols

    # Behavior equivalent to original solve()
    if k % 2 or max(n, m) == 1:
        for _ in range(n):
            print(*([-1] * m))
        return

    half = k // 2
    dp = [[[0] * (half + 1) for _ in range(m)] for _ in range(n)]

    for length in range(1, half + 1):
        for i in range(n):
            for j in range(m):
                left_path = math.inf if j == 0 else horizontal[i][j - 1] + dp[i][j - 1][length - 1]
                right_path = math.inf if j == m - 1 else horizontal[i][j] + dp[i][j + 1][length - 1]
                top_path = math.inf if i == 0 else vertical[i - 1][j] + dp[i - 1][j][length - 1]
                bottom_path = math.inf if i == n - 1 else vertical[i][j] + dp[i + 1][j][length - 1]
                dp[i][j][length] = min(left_path, right_path, top_path, bottom_path)

    for i in range(n):
        row_out = []
        for j in range(m):
            row_out.append(dp[i][j][half] * 2)
        print(*row_out)


if __name__ == "__main__":
    # Example deterministic call; change the argument to scale input size
    main(10)