def main(n):
    # Interpret n as the grid size: n x n grid, and set k proportional to n
    rows = n
    cols = n
    k = 2 * n  # even, and scales with n

    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    w = [[[0 for _ in range(4)] for _ in range(cols)] for _ in range(rows)]

    # Deterministic generation of horizontal edge weights
    # For each row, we generate (cols-1) weights
    for i in range(rows):
        row = [((i + j) % 7) + 1 for j in range(cols - 1)]
        for j in range(cols - 1):
            w[i][j + 1][2] = row[j]
            w[i][j][3] = row[j]

    # Deterministic generation of vertical edge weights
    # For each pair of consecutive rows, we generate cols weights
    for i in range(rows - 1):
        row = [((i * 2 + j * 3) % 9) + 1 for j in range(cols)]
        for j in range(cols):
            w[i][j][1] = row[j]
            w[i + 1][j][0] = row[j]

    if k % 2 == 1:
        for i in range(rows):
            for j in range(cols):
                # print(-1, end=" ")
                pass
            # print()
            pass
        return

    else:
        k //= 2

    INF = int(40 * 1e6)
    dp = [[[INF for _ in range(k + 1)] for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            dp[i][j][0] = 0

    for d in range(1, k + 1):
        for i in range(rows):
            for j in range(cols):
                for di, (dx, dy) in enumerate(dxy):
                    ii = i + dx
                    jj = j + dy
                    if 0 <= ii < rows and 0 <= jj < cols:
                        cost = dp[ii][jj][d - 1] + w[i][j][di]
                        if cost < dp[i][j][d]:
                            dp[i][j][d] = cost

    for i in range(rows):
        for j in range(cols):
            # print(dp[i][j][k] * 2, end=" ")
            pass
        # print()
        pass
if __name__ == "__main__":
    main(5)