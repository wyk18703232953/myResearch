import copy

def generate_grid(n):
    # Define grid size based on n
    rows = max(3, n)
    cols = max(3, n)
    grid = [['.' for _ in range(cols)] for _ in range(rows)]

    # Deterministically fill grid with '#' based on simple arithmetic
    for i in range(rows):
        for j in range(cols):
            if (i * cols + j) % 3 == 0:
                grid[i][j] = '#'

    # Ensure at least one full 3x3 ring of '#', if possible
    if rows >= 3 and cols >= 3:
        center_i = rows // 2
        center_j = cols // 2
        if 1 <= center_i < rows - 1 and 1 <= center_j < cols - 1:
            for di, dj in [(-1, 0), (-1, 1), (0, 1), (1, 1),
                           (1, 0), (1, -1), (0, -1), (-1, -1)]:
                grid[center_i + di][center_j + dj] = '#'
    return rows, cols, grid

def core_algorithm(n, m, grid):
    grid2 = copy.deepcopy(grid)

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if (grid[i - 1][j] == '#' and grid[i - 1][j + 1] == '#' and
                grid[i][j + 1] == '#' and grid[i + 1][j + 1] == '#' and
                grid[i + 1][j] == '#' and grid[i + 1][j - 1] == '#' and
                grid[i][j - 1] == '#' and grid[i - 1][j - 1] == '#'):
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

    return "YES" if match else "NO"

def main(n):
    rows, cols, grid = generate_grid(n)
    result = core_algorithm(rows, cols, grid)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)