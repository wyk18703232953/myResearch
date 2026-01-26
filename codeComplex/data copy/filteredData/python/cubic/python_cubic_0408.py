def main(n):
    # Map n to grid size and k
    # For scalability: let m = n, rows = n, and k = 2 * n (even)
    rows = n
    m = n
    k = 2 * n

    # Deterministic generation of p (rows x m) and q ((rows-1) x m)
    p = [[(i * m + j) % 7 + 1 for j in range(m)] for i in range(rows)]
    if rows > 1:
        q = [[(i * m + j) % 5 + 1 for j in range(m)] for i in range(rows - 1)]

    else:
        q = []

    def f(g):
        r = [[0] * m for _ in range(rows)]
        for i in range(rows):
            for j in range(m):
                l = []
                if i - 1 >= 0:
                    l.append(g[i - 1][j] + q[i - 1][j])
                if i + 1 < rows:
                    l.append(g[i + 1][j] + q[i][j])
                if j - 1 >= 0:
                    l.append(g[i][j - 1] + p[i][j - 1])
                if j + 1 < m:
                    l.append(g[i][j + 1] + p[i][j])
                r[i][j] = min(l)
        return r

    g = [[0] * m for _ in range(rows)]
    if k % 2 != 0:
        for i in range(rows):
            for j in range(m):
                g[i][j] = -1
            # print(*g[i])
            pass

    else:
        for _ in range(k // 2):
            g = f(g)
        for i in range(rows):
            for j in range(m):
                g[i][j] *= 2
            # print(*g[i])
            pass
if __name__ == "__main__":
    main(5)