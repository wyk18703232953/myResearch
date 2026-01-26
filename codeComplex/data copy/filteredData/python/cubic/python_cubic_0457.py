class node:
    def __init__(self, l, r, u, d):
        self.u = u
        self.d = d
        self.l = l
        self.r = r
        if l == 20000001 and r == 20000001 and u == 20000001 and d == 20000001:
            self.marr = [20000001 for _ in range(11)]

        else:
            self.marr = [0 for _ in range(11)]
            self.marr[1] = min(l, r, u, d)

    def mo(self, st):
        return self.marr[st - 1]


def main(n):
    # Map n to grid size and steps:
    # choose n as total number of cells approximately: n ≈ N*M
    # we will use N = M = max(1, int(n**0.5)), and s = min(10, 2 * max(1, int(n**0.5)))
    if n <= 0:
        return
    m = max(1, int(n ** 0.5))
    rows = m
    cols = m
    s = min(10, 2 * m)  # ensure s is even and <= 10 (since marr size is 11)

    n_rows = rows
    n_cols = cols

    hor = [[20000001 for _ in range(n_cols + 3)] for _ in range(n_rows + 2)]
    ver = [[20000001 for _ in range(n_cols + 2)] for _ in range(n_rows + 3)]

    # Deterministically generate horizontal edges
    for i in range(1, n_rows + 1):
        # original code reads m numbers for positions 2..m+1
        # we generate using a simple formula depending on i and j
        row_vals = [(i * 31 + j * 17) % 1000 + 1 for j in range(1, n_cols + 1)]
        hor[i][2:1 + n_cols] = row_vals

    # Deterministically generate vertical edges
    for i in range(2, 1 + n_rows):
        col_vals = [(i * 19 + j * 23) % 1000 + 1 for j in range(1, n_cols + 1)]
        ver[i][1:n_cols + 1] = col_vals

    if s % 2 == 0:
        nds = [[node(hor[i][j], hor[i][j + 1], ver[i][j], ver[i + 1][j])
                for j in range(n_cols + 2)] for i in range(n_rows + 2)]
        for st in range(2, s // 2 + 1):
            for i in range(1, n_rows + 1):
                for j in range(1, n_cols + 1):
                    x = nds[i][j].marr[1]
                    l = nds[i][j].l
                    r = nds[i][j].r
                    u = nds[i][j].u
                    d = nds[i][j].d
                    nds[i][j].marr[st] = min(
                        x * st,
                        r + nds[i][j + 1].mo(st),
                        l + nds[i][j - 1].mo(st),
                        u + nds[i - 1][j].mo(st),
                        d + nds[i + 1][j].mo(st),
                    )
        ans = [[nds[i][j].marr[s // 2] * 2 for j in range(1, n_cols + 1)] for i in range(1, n_rows + 1)]
        for i in range(n_rows):
            # print(*tuple(ans[i]))
            pass

    else:
        a = [[-1 for _ in range(n_cols)] for _ in range(n_rows)]
        for i in range(n_rows):
            # print(*tuple(a[i]))
            pass
if __name__ == "__main__":
    main(1000)