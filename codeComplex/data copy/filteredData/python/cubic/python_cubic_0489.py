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
    # n controls matrix size and k
    if n <= 0:
        return
    rows = n
    cols = n
    k = 2 * n

    hor = [[(i + j) % 7 for j in range(cols)] for i in range(rows)]
    ver = [[(i * 3 + j * 5) % 11 for j in range(cols)] for i in range(rows - 1)]

    grid = [[0] * cols for _ in range(rows)]
    if k % 2:
        for _ in range(rows):
            # print(" ".join(["-1"] * cols))
            pass

    else:
        for _ in range(k // 2):
            new_grid = [[roll(i, j, rows, cols, hor, ver, grid) for j in range(cols)] for i in range(rows)]
            grid = new_grid
        for i in range(rows):
            # print(" ".join(map(str, grid[i])))
            pass
if __name__ == "__main__":
    main(5)