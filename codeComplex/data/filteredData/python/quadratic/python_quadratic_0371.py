def main(n):
    # Map n to grid size: use n x n grid
    rows = n
    cols = n
    # Deterministic grid generation:
    # Put '*' where (i + j) is even, '.' otherwise
    grid = []
    for i in range(rows):
        row_str = []
        for j in range(cols):
            if (i + j) % 2 == 0:
                row_str.append('*')

            else:
                row_str.append('.')
        grid.append(''.join(row_str))

    m = cols
    row = [[[] for _ in range(m)] for _ in range(rows)]
    col = [[[] for _ in range(m)] for _ in range(rows)]
    visr = [[-1 for _ in range(m)] for _ in range(rows)]
    visc = [[-1 for _ in range(m)] for _ in range(rows)]
    out = []
    all_cnt = 0

    # Process rows
    for i in range(rows):
        be, en = -1, -1
        for j in range(m):
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

    # Process columns
    for i in range(m):
        be, en = -1, -1
        for j in range(rows):
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

    # Compute crosses
    for i in range(rows):
        for j in range(m):
            if grid[i][j] == '*':
                all_cnt += 1
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

    # Verification
    dis = set()
    for i in range(rows):
        j = 0
        ma = -1
        while j < m:
            ma = max(ma, visr[i][j])
            if ma >= j:
                dis.add((i, j))
            j += 1

    for i in range(m):
        j = 0
        ma = -1
        while j < rows:
            ma = max(ma, visc[j][i])
            if ma >= j:
                dis.add((j, i))
            j += 1

    if len(dis) != all_cnt:
        # print(-1)
        pass

    else:
        # print('%d\n%s' % (len(out), '\n'.join(out)))
        pass
if __name__ == "__main__":
    # Example call for complexity experiments
    main(10)