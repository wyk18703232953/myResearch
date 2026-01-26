def main(n):
    # Interpret n as the grid dimension: n x n grid, k proportional to n
    if n <= 0:
        return
    rows = n
    cols = n
    # Make k even, scale with n for complexity; e.g., k = 2 * n
    k = 2 * n

    U, D, L, R = 0, 1, 2, 3
    DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Deterministic generation of right and down cost matrices
    # right: rows x (cols-1)
    right = [[(i + j + 1) for j in range(cols - 1)] for i in range(rows)]
    # down: (rows-1) x cols
    down = [[(i + j + 2) for j in range(cols)] for i in range(rows - 1)]

    # Early exit for odd k (mimic original logic)
    if k % 2 == 1:
        for _ in range(rows):
            # print(" ".join("-1" for _ in range(cols)))
            pass
        return

    k //= 2

    dp = [[[0 for _ in range(k + 1)] for _ in range(cols)] for _ in range(rows)]

    for l in range(k):
        for i in range(rows):
            for j in range(cols):
                best = float("inf")
                if i > 0:
                    best = min(best, dp[i - 1][j][l] + down[i - 1][j])
                if j > 0:
                    best = min(best, dp[i][j - 1][l] + right[i][j - 1])
                if i < rows - 1:
                    best = min(best, dp[i + 1][j][l] + down[i][j])
                if j < cols - 1:
                    best = min(best, dp[i][j + 1][l] + right[i][j])
                dp[i][j][l + 1] = best

    for i in range(rows):
        row_out = []
        for j in range(cols):
            row_out.append(str(2 * dp[i][j][k]))
        # print(" ".join(row_out))
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to scale input size
    main(5)