def main(n):
    # Map n to grid size and k
    # For scalability: use n as both number of rows and columns, and k proportional to n
    rows = max(1, n)
    cols = max(1, n)
    k = max(1, 2 * (n // 2))  # ensure k is even for most n, but deterministic

    # Deterministic construction of h (rows x (cols-1)) and v ((rows-1) x cols)
    # Original code expects:
    # h: n rows, m-1 columns (horizontal edges)
    # v: n-1 rows, m columns (vertical edges)
    h = []
    for i in range(rows):
        row = [(i + j + 1) % 10 + 1 for j in range(cols - 1)]
        h.append(row)

    v = []
    for i in range(rows - 1):
        row = [(i * 2 + j + 3) % 10 + 1 for j in range(cols)]
        v.append(row)

    n_rows = rows
    m_cols = cols

    if k % 2 == 0:
        d = [[0] * m_cols for _ in range(n_rows)]
        for _ in range(k // 2):
            dt = [[0] * m_cols for _ in range(n_rows)]
            for i in range(n_rows):
                for j in range(m_cols):
                    x = float('inf')
                    if i - 1 >= 0:
                        x = min(x, d[i - 1][j] + v[i - 1][j] * 2)
                    if i + 1 < n_rows:
                        x = min(x, d[i + 1][j] + v[i][j] * 2)
                    if j - 1 >= 0:
                        x = min(x, d[i][j - 1] + h[i][j - 1] * 2)
                    if j + 1 < m_cols:
                        x = min(x, d[i][j + 1] + h[i][j] * 2)
                    dt[i][j] = x
            d = dt.copy()

    else:
        d = [[-1] * m_cols for _ in range(n_rows)]

    for row in d:
        # print(*row)
        pass
if __name__ == "__main__":
    main(5)