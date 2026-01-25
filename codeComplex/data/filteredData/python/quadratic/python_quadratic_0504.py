def solve(n, m, grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            must = cell == 1
            if i >= n - 2 or j >= m - 2:
                if must:
                    return 'NO'
                continue
            for di, dj in [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]:
                if grid[i + di][j + dj] == 0:
                    if must:
                        return 'NO'
                    break
            else:
                for di, dj in [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]:
                    grid[i + di][j + dj] = 2
                grid[i][j] = 2
    return 'YES'


def build_grid(n, m):
    grid = []
    for i in range(n):
        row = []
        for j in range(m):
            # Deterministic pattern from i, j:
            # 0 for some cells (like '#'), 1 for others (like '.')
            # Use a simple arithmetic rule to vary structure with n, m
            if (i * 31 + j * 17) % 7 == 0:
                row.append(0)
            else:
                row.append(1)
        grid.append(row)
    return grid


def main(n):
    if n < 1:
        n = 1
    # Map single scale n to a near-square grid n x n
    rows = n
    cols = n
    grid = build_grid(rows, cols)
    res = solve(rows, cols, grid)
    print(res)


if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(10)