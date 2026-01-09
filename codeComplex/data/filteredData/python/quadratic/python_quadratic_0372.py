import os, sys, atexit
from cStringIO import StringIO as BytesIO

sys.stdout = BytesIO()
atexit.register(lambda: os.write(1, sys.stdout.getvalue()))


def main(n):
    h = n
    w = n
    grid = []
    for i in range(h):
        row_str = []
        for j in range(w):
            if (i * 7 + j * 11) % 5 == 0:
                row_str.append('*')

            else:
                row_str.append('.')
        grid.append(''.join(row_str))

    m = w
    n_local = h

    row = [[[] for _ in range(m)] for _ in range(n_local)]
    col = [[[] for _ in range(m)] for _ in range(n_local)]
    visr, out, all_cnt = [[-1 for _ in range(m)] for _ in range(n_local)], [], 0
    visc = [[-1 for _ in range(m)] for _ in range(n_local)]

    for i in range(n_local):
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

    for i in range(m):
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

    dis = set()
    for i in range(n_local):
        j, ma = 0, -1
        while j < m:
            ma = max(ma, visr[i][j])
            if ma >= j:
                dis.add((i, j))
            j += 1

    for i in range(m):
        j, ma = 0, -1
        while j < n_local:
            ma = max(ma, visc[j][i])
            if ma >= j:
                dis.add((j, i))
            j += 1

    if len(dis) != all_cnt:
        sys.stdout.write("-1\n")

    else:
        sys.stdout.write('%d\n%s\n' % (len(out), '\n'.join(out)))


if __name__ == "__main__":
    main(10)