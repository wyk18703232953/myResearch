def main(n):
    # Map n to grid size and k
    # Choose square grid with side = max(1, n) and fixed even k related to n
    rows = max(1, n)
    cols = max(1, n)
    # Ensure k is even and at least 2 for some movement; tie it to n for scaling
    k = 2 * max(1, n // 2)

    # Deterministic generation of right and down cost grids
    # right: rows x (cols - 1), but original code assumes rows x cols with unused entries;
    # here we match original structure: right is rows x cols, but only [i][0..cols-2] used
    right = [[(i + j + 1) for j in range(cols)] for i in range(rows)]
    # down: (rows - 1) x cols, but original code uses rows-1 x cols
    down = [[(i * 2 + j + 1) for j in range(cols)] for i in range(max(0, rows - 1))]

    # Handle odd k case exactly as original
    if k % 2 == 1:
        for _ in range(rows):
            for _ in range(cols):
                # print(-1, end=" ")
                pass
            # print()
            pass
        return

    half_k = k // 2

    dp = [[[0 for _ in range(half_k + 1)] for _ in range(cols)] for _ in range(rows)]

    for l in range(half_k):
        for i in range(rows):
            for j in range(cols):
                dp[i][j][l + 1] = float("inf")
                if i > 0:
                    dp[i][j][l + 1] = min(dp[i][j][l + 1], dp[i - 1][j][l] + down[i - 1][j])
                if j > 0:
                    dp[i][j][l + 1] = min(dp[i][j][l + 1], dp[i][j - 1][l] + right[i][j - 1])
                if i < rows - 1:
                    dp[i][j][l + 1] = min(dp[i][j][l + 1], dp[i + 1][j][l] + down[i][j])
                if j < cols - 1:
                    dp[i][j][l + 1] = min(dp[i][j][l + 1], dp[i][j + 1][l] + right[i][j])

    for i in range(rows):
        for j in range(cols):
            # print(2 * dp[i][j][half_k], end=" ")
            pass
        # print()
        pass
if __name__ == "__main__":
    main(5)