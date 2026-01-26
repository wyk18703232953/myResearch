import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int,input().split()))


#[i,j)
dp = [[1000]*(n+1) for i in range(n+1)]
val = [[0]*(n+1) for i in range(n+1)]

for i in range(n):
    dp[i][i+1] = 1
    val[i][i+1] = a[i]


for p in range(2,n+1):
    for i in range(n-p+1):
        j = i+p
        for k in range(i+1,j):
            if dp[i][k] == dp[k][j] == 1 and val[i][k] == val[k][j]:
                dp[i][j] = 1
                val[i][j] = val[i][k] + 1
            else:
                dp[i][j] = min(dp[i][j] , dp[i][k]+dp[k][j])
print(dp[0][n])

