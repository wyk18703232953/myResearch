import sys
from bisect import bisect_left as bsl, bisect_right as bsr
from collections import Counter, defaultdict as ddict, deque
from functools import lru_cache
from heapq import *
from itertools import *
from math import inf
from pprint import pprint as pp

cache = lru_cache(None)
mod = 1000000007
d4 = [(0, -1), (1, 0), (0, 1), (-1, 0)]
d8 = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
enum = enumerate


def solve(m, n, grid_inner):
    # Original logic, but using provided m, n (without padding) and inner grid
    m, n = m + 2, n + 2
    grid = ['.' * n]
    grid += ['.' + row + '.' for row in grid_inner]
    grid += ['.' * n]

    up = [[0] * n for _ in range(m)]
    dw = [[0] * n for _ in range(m)]
    lf = [[0] * n for _ in range(m)]
    rg = [[0] * n for _ in range(m)]
    rs = [[0] * n for _ in range(m)]
    cs = [[0] * n for _ in range(m)]

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if grid[i][j] == '*':
                up[i][j] = 1 + up[i - 1][j]
                lf[i][j] = 1 + lf[i][j - 1]

    for i in range(m - 1, 0, -1):
        for j in range(n - 1, 0, -1):
            if grid[i][j] == '*':
                dw[i][j] = 1 + dw[i + 1][j]
                rg[i][j] = 1 + rg[i][j + 1]

    ans = []
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if grid[i][j] == '.':
                continue
            s = min(up[i - 1][j], dw[i + 1][j], lf[i][j - 1], rg[i][j + 1])
            if s == 0:
                continue
            ans.append((i, j, s))
            rs[i - s][j] += 1
            rs[i + s + 1][j] -= 1
            cs[i][j - s] += 1
            cs[i][j + s + 1] -= 1

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            rs[i][j] += rs[i - 1][j]
            cs[i][j] += cs[i][j - 1]

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if grid[i][j] == '.':
                continue
            if rs[i][j] == 0 and cs[i][j] == 0:
                return -1, []

    return len(ans), ans


def generate_grid(m, n):
    # Deterministic grid generator of size m x n using simple arithmetic patterns
    # Rule: cell is '*' if (i + j) % 3 == 0, else '.'
    grid = []
    for i in range(m):
        row_chars = []
        for j in range(n):
            if (i + j) % 3 == 0:
                row_chars.append('*')
            else:
                row_chars.append('.')
        grid.append(''.join(row_chars))
    return grid


def main(n):
    # Interpret n as both dimensions of the grid: m = n, n = n
    # Ensure minimum size at least 1x1
    if n <= 0:
        n = 1
    m = n
    k = n

    grid_inner = generate_grid(m, k)
    count, ans = solve(m, k, grid_inner)

    if count == -1:
        print(-1)
        return

    print(count)
    for i, j, s in ans:
        print(i, j, s)


if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(5)