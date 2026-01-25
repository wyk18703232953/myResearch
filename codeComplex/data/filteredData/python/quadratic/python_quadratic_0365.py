def main(n):
    if n <= 0:
        return
    # Define grid size based on n
    rows = n
    cols = n

    # Deterministically generate a pattern of '*' and '.'
    # Pattern rule: cell is '*' if (i * 31 + j * 17) % 7 != 0, else '.'
    c = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if (i * 31 + j * 17) % 7 != 0:
                row.append("*")
            else:
                row.append(".")
        c.append(row)

    n_local = rows
    m_local = cols

    a = []
    e = []
    g = []

    for _ in range(n_local):
        k = [0] * m_local
        e.append(k)
    for _ in range(n_local):
        k = [0] * m_local
        g.append(k)

    dpu = []
    for _ in range(n_local):
        k = [0] * m_local
        dpu.append(k)
    dpd = []
    for _ in range(n_local):
        k = [0] * m_local
        dpd.append(k)
    dpl = []
    for _ in range(n_local):
        k = [0] * m_local
        dpl.append(k)
    dpr = []
    for _ in range(n_local):
        k = [0] * m_local
        dpr.append(k)

    for i in range(n_local):
        for j in range(m_local):
            if c[i][j] == "*":
                if i > 0:
                    dpu[i][j] += dpu[i - 1][j] + 1
                else:
                    dpu[i][j] = 1
                if j > 0:
                    dpl[i][j] = dpl[i][j - 1] + 1
                else:
                    dpl[i][j] = 1

    i = n_local - 1
    while i >= 0:
        j = m_local - 1
        while j >= 0:
            if c[i][j] == "*":
                if i < (n_local - 1):
                    dpd[i][j] += dpd[i + 1][j] + 1
                else:
                    dpd[i][j] = 1
                if j < (m_local - 1):
                    dpr[i][j] = dpr[i][j + 1] + 1
                else:
                    dpr[i][j] = 1
            j += -1
        i += -1

    for i in range(1, n_local - 1):
        for j in range(1, m_local - 1):
            if c[i][j] == "*":
                k = min(dpd[i][j] - 1, dpu[i][j] - 1, dpr[i][j] - 1, dpl[i][j] - 1)
                if k == 0:
                    pass
                elif k > 0:
                    a.append([i + 1, j + 1, k])
                    e[i - k][j] += 1
                    if (i + k) < (n_local - 1):
                        e[i + k + 1][j] += -1
                    g[i][j - k] += 1
                    if (j + k) < (m_local - 1):
                        g[i][j + k + 1] += -1

    for i in range(m_local):
        for j in range(1, n_local):
            if c[j - 1][i] == "*":
                e[j][i] += e[j - 1][i]

    for i in range(n_local):
        for j in range(1, m_local):
            if c[i][j - 1] == "*":
                g[i][j] += g[i][j - 1]

    f = 0
    for i in range(n_local):
        for j in range(m_local):
            if c[i][j] == "*" and e[i][j] <= 0 and g[i][j] <= 0:
                f = 1
                break
        if f == 1:
            break

    if f == 1:
        print(-1)
    else:
        print(len(a))
        for j in a:
            print(*j)


if __name__ == "__main__":
    main(5)