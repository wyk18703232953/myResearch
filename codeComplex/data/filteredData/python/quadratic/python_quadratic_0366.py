def main(n):
    # Define grid size based on n
    # For scalability: n_rows = n, n_cols = n
    # Ensure at least 3x3 to allow algorithm's inner loops to run meaningfully
    n_rows = max(3, n)
    m_cols = max(3, n)

    # Deterministic grid generation of '*' and '.'
    # Pattern: c[i][j] = '*' if (i + j) % 3 != 0 else '.'
    c = []
    for i in range(n_rows):
        row = []
        for j in range(m_cols):
            if (i + j) % 3 != 0:
                row.append("*")

            else:
                row.append(".")
        c.append(row)

    n = n_rows
    m = m_cols

    a = []
    e = []
    g = []

    for j in range(n):
        k = [0] * m
        e.append(k)
    for j in range(n):
        k = [0] * m
        g.append(k)

    dpu = []
    for j in range(n):
        k = [0] * m
        dpu.append(k)
    dpd = []
    for j in range(n):
        k = [0] * m
        dpd.append(k)
    dpl = []
    for j in range(n):
        k = [0] * m
        dpl.append(k)
    dpr = []
    for j in range(n):
        k = [0] * m
        dpr.append(k)

    for i in range(n):
        for j in range(m):
            if c[i][j] == "*":
                if i > 0:
                    dpu[i][j] += dpu[i - 1][j] + 1

                else:
                    dpu[i][j] = 1
                if j > 0:
                    dpl[i][j] = dpl[i][j - 1] + 1

                else:
                    dpl[i][j] = 1

    i = n - 1
    while i >= 0:
        j = m - 1
        while j >= 0:
            if c[i][j] == "*":
                if i < (n - 1):
                    dpd[i][j] += dpd[i + 1][j] + 1

                else:
                    dpd[i][j] = 1
                if j < (m - 1):
                    dpr[i][j] = dpr[i][j + 1] + 1

                else:
                    dpr[i][j] = 1
            j += -1
        i += -1

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if c[i][j] == "*":
                k = min(dpd[i][j] - 1, dpu[i][j] - 1, dpr[i][j] - 1, dpl[i][j] - 1)
                if k == 0:
                    pass
                elif k > 0:
                    a.append([i + 1, j + 1, k])
                    e[i - k][j] += 1
                    if (i + k) < (n - 1):
                        e[i + k + 1][j] += -1
                    g[i][j - k] += 1
                    if (j + k) < (m - 1):
                        g[i][j + k + 1] += -1

    for i in range(m):
        for j in range(1, n):
            if c[j - 1][i] == "*":
                e[j][i] += e[j - 1][i]

    for i in range(n):
        for j in range(1, m):
            if c[i][j - 1] == "*":
                g[i][j] += g[i][j - 1]

    f = 0
    for i in range(n):
        for j in range(m):
            if c[i][j] == "*" and e[i][j] <= 0 and g[i][j] <= 0:
                f = 1
                break
        if f == 1:
            break

    if f == 1:
        # print(-1)
        pass

    else:
        # print(len(a))
        pass
        for j in a:
            # print(*j)
            pass
if __name__ == "__main__":
    main(10)