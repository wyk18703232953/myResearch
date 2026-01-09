import math


def main(n):
    # Interpret n as grid size parameter
    # Use n for both dimensions and for k scaling
    if n <= 0:
        return
    rows = n
    cols = n
    k = 2 * n  # even, scales with n

    # Generate deterministic right and down weight matrices
    # right: rows x (cols-1)
    right = []
    for i in range(rows):
        row = []
        for j in range(cols - 1):
            # simple deterministic weight depending on i, j
            row.append((i + 1) * (j + 2))
        right.append(row)

    # down: (rows-1) x cols
    down = []
    for i in range(rows - 1):
        row = []
        for j in range(cols):
            row.append((i + 2) * (j + 1))
        down.append(row)

    # Original algorithm begins here, with n -> rows, m -> cols
    if k % 2 == 1:
        for _ in range(rows):
            # print(" ".join(["-1" for _ in range(cols)]))
            pass
        return

    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for _ in range(1, (k // 2) + 1):
        tmp = [[math.inf for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i:
                    tmp[i][j] = min(tmp[i][j], dp[i - 1][j] + 2 * down[i - 1][j])
                if i < rows - 1:
                    tmp[i][j] = min(tmp[i][j], dp[i + 1][j] + 2 * down[i][j])
                if j:
                    tmp[i][j] = min(tmp[i][j], dp[i][j - 1] + 2 * right[i][j - 1])
                if j < cols - 1:
                    tmp[i][j] = min(tmp[i][j], dp[i][j + 1] + 2 * right[i][j])
        dp = tmp

    for i in range(rows):
        # print(" ".join(str(x) for x in dp[i]))
        pass
if __name__ == "__main__":
    # example deterministic call for complexity experiments
    main(5)