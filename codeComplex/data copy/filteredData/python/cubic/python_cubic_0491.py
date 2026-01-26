def roll(i, j, n, m, hor, ver, grid):
    ways = []
    if j:
        ways.append(2 * hor[i][j - 1] + grid[i][j - 1])
    if m - 1 - j:
        ways.append(2 * hor[i][j] + grid[i][j + 1])
    if i:
        ways.append(2 * ver[i - 1][j] + grid[i - 1][j])
    if n - 1 - i:
        ways.append(2 * ver[i][j] + grid[i + 1][j])
    return min(ways)


def main(n):
    # Interpret n as the grid size parameter.
    # We map:
    #   rows = n
    #   cols = n
    #   k   = n  (number of steps in original problem)
    rows = n
    cols = n
    k = n

    # Deterministic generation of hor and ver matrices
    # hor: rows x cols
    hor = [[(i * cols + j) % 7 + 1 for j in range(cols)] for i in range(rows)]
    # ver: (rows-1) x cols
    ver = [[((i + 1) * cols + j) % 9 + 1 for j in range(cols)] for i in range(rows - 1)]

    grid = [[0] * cols for _ in range(rows)]

    if k % 2:
        result = [["-1"] * cols for _ in range(rows)]

    else:
        for _ in range(k // 2):
            new_grid = [[roll(i, j, rows, cols, hor, ver, grid) for j in range(cols)] for i in range(rows)]
            grid = new_grid
        result = [[str(grid[i][j]) for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        # print(" ".join(result[i]))
        pass
if __name__ == "__main__":
    main(5)