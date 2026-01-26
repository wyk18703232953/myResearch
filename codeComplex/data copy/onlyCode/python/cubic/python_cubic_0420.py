import sys

def ints():
    return map(int, input().split())

n, m, k = ints()
right = []
for i in range(n):
    right.append(list(ints()))
down = []
for i in range(n-1):
    down.append(list(ints()))

INF = int(1e8)

def around(r, c):
    a = []
    for i, j in [[r-1, c], [r, c+1], [r+1, c], [r, c-1]]:
        if not (i < 0 or i >= n or j < 0 or j >= m):
            a.append([i, j])
    return a

def mink(dist, si, sj):
    minn = INF
    for i in range(max(0, si-k//2), min(n, si+k//2+1)):
        for j in range(max(0, sj-k//2), min(m, sj+k//2+1)):
            if dist[i][j] < minn:
                minn = dist[i][j]
    return minn

def solve():
    pdist = [[0] * m for i in range(n)]
    if k & 1:
        return [[-1] * m for i in range(n)]
    for step in range(k//2):
        dist = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                adist = []
                for ip, jp in around(i, j):
                    if ip == i:
                        if jp > j:
                            w = right[i][j]
                        else:
                            w = right[i][jp]
                    else:
                        if ip > i:
                            w = down[i][j]
                        else:
                            w = down[ip][j]
                    adist.append(pdist[ip][jp] + w)
                dist[i][j] = min(adist)
        pdist = dist
    for i in range(n):
        for j in range(m):
            pdist[i][j] *= 2
    return pdist

for row in solve():
    print(*row)