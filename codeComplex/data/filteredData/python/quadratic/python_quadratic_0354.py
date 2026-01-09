def main(n):
    # Interpret n as the grid size: original m x n becomes n x n
    # We generate a deterministic n x n grid of '*' and '.'
    # Pattern: cell (i,j) is '*' if (i + j) % 2 == 0, else '.'
    m = n
    cols = n

    # Build grid with padding as in original code
    padded_m, padded_n = m + 2, cols + 2
    inner_grid_rows = []
    for i in range(m):
        row_chars = []
        for j in range(cols):
            if (i + j) % 2 == 0:
                row_chars.append('*')

            else:
                row_chars.append('.')
        inner_grid_rows.append(''.join(row_chars))

    grid = ['.' * padded_n]
    grid += ['.' + inner_grid_rows[i] + '.' for i in range(m)]
    grid += ['.' * padded_n]

    up = [[0] * padded_n for _ in range(padded_m)]
    dw = [[0] * padded_n for _ in range(padded_m)]
    lf = [[0] * padded_n for _ in range(padded_m)]
    rg = [[0] * padded_n for _ in range(padded_m)]
    rs = [[0] * padded_n for _ in range(padded_m)]
    cs = [[0] * padded_n for _ in range(padded_m)]

    for i in range(1, padded_m - 1):
        for j in range(1, padded_n - 1):
            if grid[i][j] == '*':
                up[i][j] = 1 + up[i - 1][j]
                lf[i][j] = 1 + lf[i][j - 1]

    for i in range(padded_m - 1, 0, -1):
        for j in range(padded_n - 1, 0, -1):
            if grid[i][j] == '*':
                dw[i][j] = 1 + dw[i + 1][j]
                rg[i][j] = 1 + rg[i][j + 1]

    ans = []
    for i in range(1, padded_m - 1):
        for j in range(1, padded_n - 1):
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

    for i in range(1, padded_m - 1):
        for j in range(1, padded_n - 1):
            rs[i][j] += rs[i - 1][j]
            cs[i][j] += cs[i][j - 1]

    for i in range(1, padded_m - 1):
        for j in range(1, padded_n - 1):
            if grid[i][j] == '.':
                continue
            if rs[i][j] == 0 and cs[i][j] == 0:
                # print(-1)
                pass
                return

    # print(len(ans))
    pass
    for i, j, s in ans:
        # print(i, j, s)
        pass
if __name__ == "__main__":
    main(10)