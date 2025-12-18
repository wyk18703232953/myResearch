n, m, k = map(int, input().split())
reb1 = [list(map(int, input().split())) for i in range(n)]
reb2 = [list(map(int, input().split())) for i in range(n - 1)]
if k % 2:
    for i in range(n):
        for j in range(m):
            print(-1, end=" ")
        print()
    exit(0)
minsum = [[0] * m for i in range(n)]
nminsum = [[0] * m for i in range(n)]
for it in range(k // 2):
    for i in range(n):
        for j in range(m):
            cmin = 1000000000010
            if i != 0:
                cmin = min(cmin, minsum[i - 1][j] + reb2[i - 1][j])
            if i != n - 1:
                cmin = min(cmin, minsum[i + 1][j] + reb2[i][j])
            if j != 0:
                cmin = min(cmin, minsum[i][j - 1] + reb1[i][j - 1])
            if j != m - 1:
                cmin = min(cmin, minsum[i][j + 1] + reb1[i][j])
            nminsum[i][j] = cmin
    for i in range(n):
        for j in range(m):
            minsum[i][j] = nminsum[i][j]
for i in minsum:
    for j in i:
        print(j * 2, end=" ")
    print()
            
