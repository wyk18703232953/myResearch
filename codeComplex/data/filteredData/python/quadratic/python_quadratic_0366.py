def main(n):
    if n < 1:
        n = 1
    m = n
    c = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 2 == 0:
                row.append("*")

            else:
                row.append(".")
        c.append(row)

    a = []
    e = []
    g = []

    for _ in range(n):
        e.append([0] * m)
    for _ in range(n):
        g.append([0] * m)

    dpu = []
    for _ in range(n):
        dpu.append([0] * m)
    dpd = []
    for _ in range(n):
        dpd.append([0] * m)
    dpl = []
    for _ in range(n):
        dpl.append([0] * m)
    dpr = []
    for _ in range(n):
        dpr.append([0] * m)

    for i in range(n):
        for j in range(m):
            if c[i][j] == "*":
                if i > 0:
                    dpu[i][j] = dpu[i - 1][j] + 1

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
                if i < n - 1:
                    dpd[i][j] = dpd[i + 1][j] + 1

                else:
                    dpd[i][j] = 1
                if j < m - 1:
                    dpr[i][j] = dpr[i][j + 1] + 1

                else:
                    dpr[i][j] = 1
            j -= 1
        i -= 1

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if c[i][j] == "*":
                k = min(dpd[i][j] - 1, dpu[i][j] - 1, dpr[i][j] - 1, dpl[i][j] - 1)
                if k > 0:
                    a.append([i + 1, j + 1, k])
                    e[i - k][j] += 1
                    if i + k < n - 1:
                        e[i + k + 1][j] -= 1
                    g[i][j - k] += 1
                    if j + k < m - 1:
                        g[i][j + k + 1] -= 1

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
    main(5)