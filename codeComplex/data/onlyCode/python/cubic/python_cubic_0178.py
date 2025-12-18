import sys
input = sys.stdin.readline
n = int(input().strip())
a = [int(x) for x in input().strip().split()]
dp = [[0]*n for i in range(n)]
for i in range(n):
    dp[i][i] = [a[i], 1]
for i in range(1, n):
    for j in range(n-i):
        v, c = -1, i+1
        for k in range(i):
            if dp[j][j+k][0]!=-1 and dp[j][j+k][0] == dp[j+k+1][j+i][0]:
                v,c = dp[j][j+k][0]+1, 1
                break
            else:
                v, c = -1, min(c, dp[j][j+k][1] + dp[j+k+1][j+i][1])
        dp[j][j+i] = [v, c]
print(dp[0][-1][1])


