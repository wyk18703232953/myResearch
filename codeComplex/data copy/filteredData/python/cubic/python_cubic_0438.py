def main(n):
    # Map n to grid size and k (path length)
    # For scalability, choose n as total cells ≈ rows * cols, here rows = cols
    if n <= 0:
        return
    m = max(1, int(n ** 0.5))
    n_rows = m
    n_cols = m
    # Let k scale with grid dimension, make it even to exercise main branch
    k = 2 * m

    # Deterministic generation of right and down cost matrices
    right = [[9999999 for _ in range(n_cols - 1)] for _ in range(n_rows)]
    down = [[9999999 for _ in range(n_cols)] for _ in range(n_rows - 1)]

    # Fill right[i][j] = i + j + 1
    for i in range(n_rows):
        for j in range(n_cols - 1):
            right[i][j] = i + j + 1

    # Fill down[i][j] = i + j + 2
    for i in range(n_rows - 1):
        for j in range(n_cols):
            down[i][j] = i + j + 2

    if k % 2 == 1:
        for i in range(n_rows):
            row_out = []
            for j in range(n_cols):
                row_out.append("-1")
            # print(" ".join(row_out))
            pass

    else:
        k_half = k // 2
        row = n_rows
        col = n_cols
        dp = [[[9999999 for _ in range(col)] for _ in range(row)] for _ in range(k_half + 1)]
        for steps in range(k_half + 1):
            for i in range(row):
                for j in range(col):
                    if steps == 0:
                        dp[steps][i][j] = 0
                        continue
                    ans = 99999999999
                    if i > 0:
                        ans = min(ans, dp[steps - 1][i - 1][j] + down[i - 1][j])
                    if i < row - 1:
                        ans = min(ans, dp[steps - 1][i + 1][j] + down[i][j])
                    if j < col - 1:
                        ans = min(ans, dp[steps - 1][i][j + 1] + right[i][j])
                    if j > 0:
                        ans = min(ans, dp[steps - 1][i][j - 1] + right[i][j - 1])
                    dp[steps][i][j] = ans

        for i in range(row):
            row_out = []
            for j in range(col):
                row_out.append(str(2 * dp[k_half][i][j]))
            # print(" ".join(row_out))
            pass
if __name__ == "__main__":
    main(1000)