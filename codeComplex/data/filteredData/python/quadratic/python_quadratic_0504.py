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


def main(n):
    # 将 n 映射为网格规模：n x n
    rows = n
    cols = n

    # 确定性生成网格：
    # 使用模式：根据 (i + j) 的奇偶生成 '.' 或 '#'
    # '.' -> 0, '#' -> 1，和原程序一致
    grid = [[('.#'.index('#') if (i + j) % 3 == 0 else '.#'.index('.'))
             for j in range(cols)]
            for i in range(rows)]

    res = solve(rows, cols, grid)
    # print(res)
    pass
if __name__ == "__main__":
    main(10)