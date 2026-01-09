def main(n):
    # Interpret n as both number of rows and columns: n x n grid
    # Deterministically generate the grid s: pattern of '*' and '.'
    # Example pattern: cell (i,j) is '*' if (i + j) % 3 != 0, else '.'
    rows = n
    cols = n
    s = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if (i + j) % 3 != 0:
                row.append("*")

            else:
                row.append(".")
        s.append(row)

    n_local = rows
    m_local = cols

    t = [[1000] * m_local for _ in range(n_local)]
    ok1 = [[0] * m_local for _ in range(n_local)]
    ok2 = [[0] * m_local for _ in range(n_local)]

    for i in range(n_local):
        si = s[i]
        c = 0
        for j in range(m_local):
            if si[j] == "*":
                c += 1

            else:
                c = 0
            if c < t[i][j]:
                t[i][j] = c
        c = 0
        for j in range(m_local - 1, -1, -1):
            if si[j] == "*":
                c += 1

            else:
                c = 0
            if c < t[i][j]:
                t[i][j] = c

    for j in range(m_local):
        c = 0
        for i in range(n_local):
            if s[i][j] == "*":
                c += 1

            else:
                c = 0
            if c < t[i][j]:
                t[i][j] = c
        c = 0
        for i in range(n_local - 1, -1, -1):
            if s[i][j] == "*":
                c += 1

            else:
                c = 0
            if c < t[i][j]:
                t[i][j] = c

    ans = []
    for i in range(n_local):
        for j in range(m_local):
            tij = t[i][j] - 1
            if tij >= 1:
                ans.append((i + 1, j + 1, tij))
                up_i = i - tij
                if up_i < 0:
                    up_i = 0
                ok1[up_i][j] += 1
                down_i = i + tij + 1
                if down_i < n_local:
                    ok1[down_i][j] -= 1
                left_j = j - tij
                if left_j < 0:
                    left_j = 0
                ok2[i][left_j] += 1
                right_j = j + tij + 1
                if right_j < m_local:
                    ok2[i][right_j] -= 1

    for i in range(1, n_local):
        for j in range(1, m_local):
            ok1[i][j] += ok1[i - 1][j]
            ok2[i][j] += ok2[i][j - 1]

    valid = True
    for i in range(n_local):
        for j in range(m_local):
            if s[i][j] == "*":
                if not (ok1[i][j] or ok2[i][j]):
                    valid = False
                    break
        if not valid:
            break

    if not valid:
        # print(-1)
        pass
        return

    k = len(ans)
    # print(k)
    pass
    for ans0 in ans:
        # print(*ans0)
        pass
if __name__ == "__main__":
    main(5)