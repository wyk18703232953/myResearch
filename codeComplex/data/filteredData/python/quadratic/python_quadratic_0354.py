import random

def main(n: int):
    # n: problem scale, here used as grid size (n x n)

    if n < 1:
        return

    # generate random grid of '.' and '*' of size n x n
    # you can adjust probability as needed
    p_star = 0.5
    m0, n0 = n, n
    inner_grid = []
    for _ in range(m0):
        row = ''.join('*' if random.random() < p_star else '.' for _ in range(n0))
        inner_grid.append(row)

    # add padding border of '.'
    m, n = m0 + 2, n0 + 2
    grid = ['.' * n]
    grid += ['.' + row + '.' for row in inner_grid]
    grid += ['.' * n]

    up = [[0] * n for _ in range(m)]
    dw = [[0] * n for _ in range(m)]
    lf = [[0] * n for _ in range(m)]
    rg = [[0] * n for _ in range(m)]
    rs = [[0] * n for _ in range(m)]
    cs = [[0] * n for _ in range(m)]

    # prefix lengths up/left
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if grid[i][j] == '*':
                up[i][j] = 1 + up[i - 1][j]
                lf[i][j] = 1 + lf[i][j - 1]

    # prefix lengths down/right
    for i in range(m - 2, 0, -1):
        for j in range(n - 2, 0, -1):
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
                print(-1)
                return

    print(len(ans))
    for i, j, s in ans:
        print(i, j, s)