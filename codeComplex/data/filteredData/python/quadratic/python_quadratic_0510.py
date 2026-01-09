def main(n):
    # n controls grid size: use n x n grid
    # Construct a deterministic grid pattern of '.' and '#'
    m = n
    grid = []
    for i in range(n):
        row = []
        for j in range(m):
            # Deterministic pattern: '#' when (i+j) is even, else '.'
            if (i + j) % 2 == 0:
                row.append('#')

            else:
                row.append('.')
        grid.append(row)

    # Deep copy of grid
    grid2 = [row[:] for row in grid]

    # Core algorithm logic unchanged
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if (
                grid[i - 1][j] == '#'
                and grid[i - 1][j + 1] == '#'
                and grid[i][j + 1] == '#'
                and grid[i + 1][j + 1] == '#'
                and grid[i + 1][j] == '#'
                and grid[i + 1][j - 1] == '#'
                and grid[i][j - 1] == '#'
                and grid[i - 1][j - 1] == '#'
            ):
                grid2[i - 1][j] = '.'
                grid2[i - 1][j + 1] = '.'
                grid2[i][j + 1] = '.'
                grid2[i + 1][j + 1] = '.'
                grid2[i + 1][j] = '.'
                grid2[i + 1][j - 1] = '.'
                grid2[i][j - 1] = '.'
                grid2[i - 1][j - 1] = '.'

    match = True
    for row in grid2:
        for ch in row:
            if ch == '#':
                match = False
                break
        if not match:
            break

    if match:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)