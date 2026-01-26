import sys

n, m, k = map(int, input().split())

#process cost
hor = [list(map(int, input().split())) for _ in range(n)]
#hor[i][j] --> i,j and i, j+1
ver = [list(map(int, input().split())) for _ in range(n-1)]
#ver[i][j] --> i, j and i+1, j

#dp
if k % 2:
    for i in range(n):
        print(*([-1]*m))
    sys.exit()

k = k // 2
dp = [[[0]*m for _ in range(n)] for _ in range(k+1)]

for x in range(1, k+1):
    for y in range(n):
        for z in range(m):
            hold = float('inf')
            if y != 0:
                hold = min(hold, dp[x-1][y-1][z] + ver[y-1][z] )
            if y != n-1:
                hold = min(hold, dp[x-1][y+1][z] + ver[y][z] )
            if z != 0:
                hold = min(hold, dp[x-1][y][z-1] + hor[y][z-1] )
            if z != m-1:
                hold = min(hold, dp[x-1][y][z+1] + hor[y][z] )
            dp[x][y][z] = hold

for row in dp[k]:
    print(*map(lambda i: i*2, row))
