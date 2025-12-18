get = lambda : list(map(int, input().split(' ')))
n, m, k = get()
rlist, clist = [], []
for _ in range(n):
    rlist.append(get())
for _ in range(n-1):
    clist.append(get())

dway = [[0,1],[0,-1],[1,0],[-1,0]]
if k%2:
    res = [[-1]*m for _ in range(n)]
else:
    flist = [[0]*m for _ in range(n)]
    for _ in range(k//2):
        glist = [[10**9]*m for _ in range(n)]
        for dx, dy in dway:
            klist = rlist if dx == 0 else clist
            for x in range(n):
                for y in range(m):
                    xx, yy = x+dx, y+dy
                    if not (0<=xx<n) or not (0<=yy<m):
                        continue
                    tx = xx if dx==-1 else x
                    ty = yy if dy==-1 else y
                    glist[x][y] = min(glist[x][y], flist[xx][yy] + klist[tx][ty] * 2)
        flist = glist
    res = flist
for row in res:
    print(' '.join(map(str, row)))