import sys
import random


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
            for di, dj in [
                (0, 1), (0, 2),
                (1, 0), (1, 2),
                (2, 0), (2, 1), (2, 2)
            ]:
                if grid[i + di][j + dj] == 0:
                    if must:
                        return 'NO'
                    break
            else:
                for di, dj in [
                    (0, 1), (0, 2),
                    (1, 0), (1, 2),
                    (2, 0), (2, 1), (2, 2)
                ]:
                    grid[i + di][j + dj] = 2
                grid[i][j] = 2
    return 'YES'


def generate_grid(n, m):
    # 0 -> '.', 1 -> '#'
    return [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]


def main(n):
    # 这里根据 n 构造一个 n 行 n 列的网格
    m = n
    grid = generate_grid(n, m)
    result = solve(n, m, grid)

    # 按原程序风格，仅输出最终结果
    print(result)


if __name__ == "__main__":
    # 示例：可修改为需要的规模
    main(5)