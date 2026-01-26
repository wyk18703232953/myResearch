#tests = int(input())
#for t in range(tests):
#    b= int(input())
#    ls = [int(x) for x in input()]

r,g,b = list(map(int, input().split()))
ls_r = sorted(list(map(int, input().split())))
ls_g = sorted(list(map(int, input().split())))
ls_b = sorted(list(map(int, input().split())))


dp = [[[None for _ in range(b+1)]for _ in range(g+1)]for _ in range(r+1)]

for i in range(r+1):
    dp[i][0][0] = 0
for i in range(g+1):
    dp[0][i][0] = 0
for i in range(b+1):
    dp[0][0][i] = 0

dp[1][1][0] = ls_r[0] * ls_g[0]
dp[0][1][1] = ls_g[0] * ls_b[0]
dp[1][0][1] = ls_r[0] * ls_b[0]    

for i in range(r+1):
    for j in range(g+1):
        for k in range(b+1):
            res1 = 0
            res2 = 0
            res3 = 0
            if i-1>=0 and j-1>=0:
                res1 += dp[i-1][j-1][k] + ls_r[i-1] * ls_g[j-1]
            if i-1>=0 and k-1>=0:
                res2 += dp[i-1][j][k-1] + ls_r[i-1] * ls_b[k-1]
            if j-1>=0 and k-1>=0:
                res3 += dp[i][j-1][k-1] + ls_g[j-1] * ls_b[k-1]
            dp[i][j][k] = max(res1,res2,res3)
print(dp[r][g][b])