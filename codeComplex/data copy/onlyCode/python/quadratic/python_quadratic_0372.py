import os, sys, atexit
from cStringIO import StringIO as BytesIO

sys.stdout = BytesIO()
atexit.register(lambda: os.write(1, sys.stdout.getvalue()))
input = BytesIO(os.read(0, os.fstat(0).st_size)).readline


rints = lambda: [int(x) for x in input().split()]
rstr = lambda: input().strip()
rstr_2d = lambda n: [rstr() for _ in range(n)]

n, m = rints()
grid = rstr_2d(n)
row = [[[] for _ in range(m)] for _ in range(n)]
col = [[[] for _ in range(m)] for _ in range(n)]
visr, out, all = [[-1 for _ in range(m)] for _ in range(n)], [], 0
visc = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
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
    for j in range(n):
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

for i in range(n):
    for j in range(m):
        if grid[i][j] == '*':
            all += 1
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
for i in range(n):
    j, ma = 0, -1
    while j < m:
        ma = max(ma, visr[i][j])
        if ma >= j:
            dis.add((i, j))

        j += 1

for i in range(m):
    j, ma = 0, -1
    while j < n:
        ma = max(ma, visc[j][i])
        if ma >= j:
            dis.add((j, i))

        j += 1

if len(dis) != all:
    print(-1)
else:
    sys.stdout.write('%d\n%s' % (len(out), '\n'.join(out)))
