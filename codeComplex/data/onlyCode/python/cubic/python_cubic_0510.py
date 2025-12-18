import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline    
 
n,m,k = [int(i) for i in input().split()]
h = []
for i in range (n):
    h.append([int(i) for i in input().split()])
v = []
for i in range (n-1):
    v.append([int(i) for i in input().split()])
if k%2:
    for i in range (n):
        for j in range (m):
            print(-1,end=" ")
        print()
    exit()
dp = [[[float('inf')]*m for i in range (n)] for j in range (k//2+1)]
for i in range (n):
    for j in range (m):
        dp[0][i][j] = 0
for x in range (1,k//2+1):
    for i in range (n):
        for j in range (m):
            if i!=0:
                dp[x][i][j] = min(dp[x][i][j], dp[x-1][i-1][j] + v[i-1][j])
            if i!=n-1:
                dp[x][i][j] = min(dp[x][i][j], dp[x-1][i+1][j] + v[i][j])
            if j!=0:
                dp[x][i][j] = min(dp[x][i][j], dp[x-1][i][j-1] + h[i][j-1])
            if j!=m-1:
                dp[x][i][j] = min(dp[x][i][j], dp[x-1][i][j+1] + h[i][j])
 
for i in range (n):
    for j in range (m):
        print(2*dp[k//2][i][j],end=" ")
    print()