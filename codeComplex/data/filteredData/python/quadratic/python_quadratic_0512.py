import random

def check(grid, i, j, sx, sy, N, M):
    if i - sx >= 0 and j - sy >= 0 and i + 2 - sx < N and j + 2 - sy < M:
        i -= sx
        j -= sy
        v = (
            grid[i][j] == '#' and grid[i + 1][j] == '#' and grid[i + 2][j] == '#' and
            grid[i][j + 1] == '#' and grid[i + 2][j + 1] == '#' and
            grid[i][j + 2] == '#' and grid[i + 1][j + 2] == '#' and grid[i + 2][j + 2] == '#'
        )
        return v
    return False

def main(n):
    # 根据规模 n 生成一个 N x M 的网格测试数据
    # 这里简单设定 N = M = n，并随机生成 '#' 和 '.'。
    N = n
    M = n
    random.seed(0)
    grid = []
    for _ in range(N):
        row = []
        for _ in range(M):
            row.append('#' if random.random() < 0.5 else '.')
        grid.append(row)

    for m in range(M):
        for i in range(N):
            if grid[i][m] == '#':
                if not (
                    check(grid, i, m, 0, 0, N, M) or
                    check(grid, i, m, 1, 0, N, M) or
                    check(grid, i, m, 2, 0, N, M) or
                    check(grid, i, m, 0, 1, N, M) or
                    check(grid, i, m, 2, 1, N, M) or
                    check(grid, i, m, 0, 2, N, M) or
                    check(grid, i, m, 1, 2, N, M) or
                    check(grid, i, m, 2, 2, N, M)
                ):
                    print("NO")
                    return
    print("YES")