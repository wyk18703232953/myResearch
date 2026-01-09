def main(n):
    # Map n to grid dimensions
    # Use a roughly square grid: rows = n, cols = n
    rows = n
    cols = n

    # Deterministic grid generation: pattern depending on indices
    # Use '*' when (i + j) % 3 == 0, otherwise '.'
    g = [
        ['*' if (i + j) % 3 == 0 else '.' for j in range(cols)]
        for i in range(rows)
    ]

    c = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        v = 0
        for j in range(cols):
            v = (v + 1) * (g[i][j] == '*')
            c[i][j] = v
        v = 0
        for j in range(cols - 1, -1, -1):
            v = (v + 1) * (g[i][j] == '*')
            c[i][j] = min(c[i][j], v)
    for j in range(cols):
        v = 0
        for i in range(rows):
            v = (v + 1) * (g[i][j] == '*')
            c[i][j] = min(c[i][j], v)
        v = 0
        for i in range(rows - 1, -1, -1):
            v = (v + 1) * (g[i][j] == '*')
            c[i][j] = min(c[i][j], v)
    for i in range(rows):
        for j in range(cols):
            if c[i][j] == 1:
                c[i][j] = 0
    for i in range(rows):
        v = 0
        for j in range(cols):
            v = max(v - 1, c[i][j])
            if v:
                g[i][j] = '.'
        v = 0
        for j in range(cols - 1, -1, -1):
            v = max(v - 1, c[i][j])
            if v:
                g[i][j] = '.'
    for j in range(cols):
        v = 0
        for i in range(rows):
            v = max(v - 1, c[i][j])
            if v:
                g[i][j] = '.'
        v = 0
        for i in range(rows - 1, -1, -1):
            v = max(v - 1, c[i][j])
            if v:
                g[i][j] = '.'
    if all(g[i][j] == '.' for i in range(rows) for j in range(cols)):
        r = [(i + 1, j + 1, c[i][j] - 1) for i in range(rows) for j in range(cols) if c[i][j]]
        # print(len(r))
        pass
        for t in r:
            # print(*t)
            pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(5)