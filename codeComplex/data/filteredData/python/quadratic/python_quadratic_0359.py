def main(n):
    # Map n to grid size: create an n x n grid
    rows = n
    cols = n

    # Deterministic grid generation:
    # Pattern: cells where (i + j) % 3 == 0 are '*', others are '.'
    s = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if (i + j) % 3 == 0:
                row.append('*')

            else:
                row.append('.')
        s.append(row)

    n_local = rows
    m_local = cols

    u = [[-1 for _ in range(m_local)] for _ in range(n_local)]
    d = [[-1 for _ in range(m_local)] for _ in range(n_local)]
    l = [[-1 for _ in range(m_local)] for _ in range(n_local)]
    r = [[-1 for _ in range(m_local)] for _ in range(n_local)]

    for i in range(m_local):
        acum = 0
        for j in range(n_local):
            if s[j][i] == ".":
                acum = 0

            else:
                acum += 1
            u[j][i] = acum

    for i in range(m_local):
        acum = 0
        for j in range(n_local - 1, -1, -1):
            if s[j][i] == ".":
                acum = 0

            else:
                acum += 1
            d[j][i] = acum

    for i in range(n_local):
        acum = 0
        for j in range(m_local):
            if s[i][j] == ".":
                acum = 0

            else:
                acum += 1
            l[i][j] = acum

    for i in range(n_local):
        acum = 0
        for j in range(m_local - 1, -1, -1):
            if s[i][j] == ".":
                acum = 0

            else:
                acum += 1
            r[i][j] = acum

    ans = []
    t1 = [[0 for _ in range(m_local)] for _ in range(n_local)]
    t2 = [[0 for _ in range(m_local)] for _ in range(n_local)]

    for i in range(n_local):
        for j in range(m_local):
            d1 = min(l[i][j], r[i][j], u[i][j], d[i][j]) - 1
            if d1 > 0:
                ans.append([i + 1, j + 1, d1])
                if 0 <= i + d1 < n_local:
                    t1[i + d1][j] += 1
                if 0 <= i - d1 < n_local:
                    t1[i - d1][j] -= 1
                if 0 <= j - d1 < m_local:
                    t2[i][j - d1] += 1
                if 0 <= j + d1 < m_local:
                    t2[i][j + d1] -= 1

    dp = [['.' for _ in range(m_local)] for _ in range(n_local)]

    for i in range(n_local):
        acum = 0
        for j in range(m_local):
            acum += t2[i][j]
            if acum != 0 or t2[i][j] != 0:
                dp[i][j] = '*'

    for i in range(m_local):
        acum = 0
        for j in range(n_local):
            acum += t1[j][i]
            if acum != 0 or t1[j][i] != 0:
                dp[j][i] = '*'

    if dp != s:
        # print(-1)
        pass
        return

    # print(len(ans))
    pass
    for triple in ans:
        # print(*triple)
        pass
if __name__ == "__main__":
    main(10)