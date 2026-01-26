import os
import sys

def main(n):
    # Interpret n as both number of rows and columns
    rows = n
    cols = n

    # Deterministically generate a grid pattern of '*' and '.'
    # Example rule: cell (i, j) is '*' if (i + j) % 3 == 0, else '.'
    grid = []
    for i in range(rows):
        row_chars = []
        for j in range(cols):
            if (i + j) % 3 == 0:
                row_chars.append('*')

            else:
                row_chars.append('.')
        grid.append(''.join(row_chars))

    n_local = rows
    m_local = cols

    row = [[[] for _ in range(m_local)] for _ in range(n_local)]
    col = [[[] for _ in range(m_local)] for _ in range(n_local)]
    visr = [[-1 for _ in range(m_local)] for _ in range(n_local)]
    visc = [[-1 for _ in range(m_local)] for _ in range(n_local)]
    out = []
    all_stars = 0

    for i in range(n_local):
        be, en = -1, -1
        for j in range(m_local):
            if grid[i][j] == '*':
                en += 1
                if be == -1:
                    be = en = j

            else:
                if be != -1:
                    for k in range(be, en + 1):
                        row[i][k] = [be, en]
                be = -1
        if be != -1:
            for k in range(be, en + 1):
                row[i][k] = [be, en]

    for i in range(m_local):
        be, en = -1, -1
        for j in range(n_local):
            if grid[j][i] == '*':
                en += 1
                if be == -1:
                    be = en = j

            else:
                if be != -1:
                    for k in range(be, en + 1):
                        col[k][i] = [be, en]
                be = -1
        if be != -1:
            for k in range(be, en + 1):
                col[k][i] = [be, en]

    for i in range(n_local):
        for j in range(m_local):
            if grid[i][j] == '*':
                all_stars += 1
                hor = min(row[i][j][1] - j, j - row[i][j][0])
                ver = min(col[i][j][1] - i, i - col[i][j][0])
                if hor <= ver:
                    ver = hor

                else:
                    hor = ver
                if hor > 0 and ver > 0:
                    out.append('%d %d %d' % (i + 1, j + 1, hor))
                    visr[i][j - ver] = j + ver
                    visc[i - hor][j] = i + hor

    dis = set()
    for i in range(n_local):
        j, ma = 0, -1
        while j < m_local:
            ma = max(ma, visr[i][j])
            if ma >= j:
                dis.add((i, j))
            j += 1

    for i in range(m_local):
        j, ma = 0, -1
        while j < n_local:
            ma = max(ma, visc[j][i])
            if ma >= j:
                dis.add((j, i))
            j += 1

    if len(dis) != all_stars:
        # print(-1)
        pass

    else:
        sys.stdout.write('%d\n%s' % (len(out), '\n'.join(out)))


if __name__ == "__main__":
    # Example deterministic call; change n to scale the input size
    main(10)