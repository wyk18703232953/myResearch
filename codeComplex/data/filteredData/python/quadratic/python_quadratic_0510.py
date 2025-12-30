import copy
import random

def main(n):
    # 生成一个 n×n 的随机网格，字符为 '#' 或 '.'
    m = n
    grid = []
    for _ in range(n):
        row = ['#' if random.random() < 0.5 else '.' for _ in range(m)]
        grid.append(row)

    grid2 = copy.deepcopy(grid)

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if (grid[i - 1][j] == '#' and
                grid[i - 1][j + 1] == '#' and
                grid[i][j + 1] == '#' and
                grid[i + 1][j + 1] == '#' and
                grid[i + 1][j] == '#' and
                grid[i + 1][j - 1] == '#' and
                grid[i][j - 1] == '#' and
                grid[i - 1][j - 1] == '#'):
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
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)