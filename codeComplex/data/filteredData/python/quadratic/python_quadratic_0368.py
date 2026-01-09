def main(n):
    # Map n to a grid of about n^2 cells: choose rows ~ n and cols ~ n
    # Use a simple deterministic mapping: rows = n, cols = max(1, n)
    rows = n
    cols = max(1, n)

    # Deterministically generate grid l: pattern of '*' and '.'
    # Example pattern: cell (i,j) is '*' if (i + 2*j) % 3 == 0, else '.'
    l = []
    for i in range(rows):
        row_str = []
        for j in range(cols):
            if (i + 2 * j) % 3 == 0:
                row_str.append('*')

            else:
                row_str.append('.')
        l.append(''.join(row_str))

    n_local = rows
    m_local = cols

    tot = []
    done = [[0 for _ in range(m_local)] for _ in range(n_local)]
    colsum = [[0 for _ in range(m_local)] for _ in range(n_local)]
    rowsum = [[0 for _ in range(m_local)] for _ in range(n_local)]
    col = [[0 for _ in range(m_local)] for _ in range(n_local)]
    row = [[0 for _ in range(m_local)] for _ in range(n_local)]

    for i in range(n_local):
        for j in range(m_local):
            if l[i][j] == '*':
                rowsum[i][j] = 1
                colsum[i][j] = 1
                row[i][j] = 1
                col[i][j] = 1

    for i in range(n_local):
        for j in range(1, m_local):
            if l[i][j] == '.':
                continue
            rowsum[i][j] += rowsum[i][j - 1]

    for i in range(n_local):
        for j in range(m_local - 2, -1, -1):
            if l[i][j] == '.':
                continue
            row[i][j] += row[i][j + 1]

    for i in range(m_local):
        for j in range(n_local - 2, -1, -1):
            if l[j][i] == '.':
                continue
            col[j][i] += col[j + 1][i]

    for i in range(m_local):
        for j in range(1, n_local):
            if l[j][i] == '.':
                continue
            colsum[j][i] += colsum[j - 1][i]

    def check(x, y):
        i = x
        j = y
        ans = min(row[i][j], rowsum[i][j], colsum[i][j], col[i][j]) - 1
        if ans == 0:
            return []
        return [ans]

    h = [[0 for _ in range(m_local + 1)] for _ in range(n_local)]
    v = [[0 for _ in range(m_local)] for _ in range(n_local + 1)]
    for i in range(n_local):
        for j in range(m_local):
            if l[i][j] == '*':
                ans_list = check(i, j)
                for j1 in ans_list:
                    tot.append([i + 1, j + 1, j1])
                    if j - j1 >= 0:
                        h[i][j - j1] += 1
                    if j + j1 + 1 <= m_local:
                        h[i][j + j1 + 1] -= 1
                    if i - j1 >= 0:
                        v[i - j1][j] += 1
                    if i + j1 + 1 <= n_local:
                        v[i + j1 + 1][j] -= 1

    for i in range(n_local):
        for j in range(1, m_local):
            h[i][j] += h[i][j - 1]

    for i in range(m_local):
        for j in range(1, n_local):
            v[j][i] += v[j - 1][i]

    impossible = False
    for i in range(n_local):
        for j in range(m_local):
            if l[i][j] == '*' and h[i][j] == 0 and v[i][j] == 0:
                impossible = True
                break
        if impossible:
            break

    if impossible:
        # print(-1)
        pass
        return

    # print(len(tot))
    pass
    for item in tot:
        # print(*item)
        pass
if __name__ == "__main__":
    main(5)