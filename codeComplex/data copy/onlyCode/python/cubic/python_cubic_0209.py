r,g,b = map(int,input().split())

R = list(map(int,input().split()))
G = list(map(int,input().split()))
B = list(map(int,input().split()))

R.sort(reverse=True)
G.sort(reverse=True)
B.sort(reverse=True)
# dp[i][j][k]

dp = [[[0]*(b+1) for _ in range(g+1)] for _ in range(r+1)]

for j in range(g-1,-1,-1):
    for k in range(b-1,-1,-1):
        dp[r][j][k] = G[j]*B[k] + dp[r][j+1][k+1]

for i in range(r-1,-1,-1):
    for k in range(b-1,-1,-1):
        dp[i][g][k] = R[i]*B[k] + dp[i+1][g][k+1]

for i in range(r-1,-1,-1):
    for j in range(g-1,-1,-1):
        dp[i][j][b] = R[i]*G[j] + dp[i+1][j+1][b]

for i in range(r-1,-1,-1):
    for j in range(g-1,-1,-1):
        for k in range(b-1,-1,-1):
            case1 = dp[i+1][j][k]
            case2 = dp[i][j+1][k]
            case3 = dp[i][j][k+1]

            case4 = R[i]*G[j] + dp[i+1][j+1][k]
            case5 = R[i]*B[k] + dp[i+1][j][k+1]
            case6 = G[j]*B[k] + dp[i][j+1][k+1]

            dp[i][j][k] = max(case1,case2,case3,case4,case5,case6)

print(dp[0][0][0])
