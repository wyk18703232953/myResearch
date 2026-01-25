def main(n):
    # Map n to grid size: n -> n x n grid
    rows = max(1, n)
    cols = max(1, n)

    # Deterministic grid generation using simple arithmetic pattern
    # Pattern: g[i][j] is '*' if (i + j) % 3 == 0 else '.'
    g = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if (i + j) % 3 == 0:
                row.append('*')
            else:
                row.append('.')
        g.append(row)

    m = cols
    n_local = rows

    c = [[0 for _ in range(m)] for _ in range(n_local)]
    for i in range(n_local):
        v = 0
        for j in range(m):
            v = (v + 1) * (g[i][j] == '*')
            c[i][j] = v
        v = 0
        for j in range(m - 1, -1, -1):
            v = (v + 1) * (g[i][j] == '*')
            c[i][j] = min(c[i][j], v)
    for j in range(m):
        v = 0
        for i in range(n_local):
            v = (v + 1) * (g[i][j] == '*')
            c[i][j] = min(c[i][j], v)
        v = 0
        for i in range(n_local - 1, -1, -1):
            v = (v + 1) * (g[i][j] == '*')
            c[i][j] = min(c[i][j], v)
    for i in range(n_local):
        for j in range(m):
            if c[i][j] == 1:
                c[i][j] = 0
    for i in range(n_local):
        v = 0
        for j in range(m):
            v = max(v - 1, c[i][j])
            if v:
                g[i][j] = '.'
        v = 0
        for j in range(m - 1, -1, -1):
            v = max(v - 1, c[i][j])
            if v:
                g[i][j] = '.'
    for j in range(m):
        v = 0
        for i in range(n_local):
            v = max(v - 1, c[i][j])
            if v:
                g[i][j] = '.'
        for i in range(n_local - 1, -1, -1):
            v = max(v - 1, c[i][j])
            if v:
                g[i][j] = '.'
    if all(g[i][j] == '.' for i in range(n_local) for j in range(m)):
        r = [(i + 1, j + 1, c[i][j] - 1) for i in range(n_local) for j in range(m) if c[i][j]]
        print(len(r))
        for t in r:
            print(*t)
    else:
        print(-1)


if __name__ == "__main__":
    main(5)