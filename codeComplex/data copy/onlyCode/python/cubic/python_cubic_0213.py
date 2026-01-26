r,g,b=map(int,input().split())
R=list(map(int,input().split()))
R.sort()
G=list(map(int,input().split()))
G.sort()
B=list(map(int,input().split()))
B.sort()
dp=[[[0]*(b+1) for i in range(g+1)] for j in range(r+1)]
for i in range(r+1):
    for j in range(g+1):
        for k in range(b+1):
            if i<r and j<g:
                dp[i+1][j+1][k]=max(dp[i+1][j+1][k],dp[i][j][k]+R[i]*G[j])
            if i<r and k<b:
                dp[i+1][j][k+1]=max(dp[i+1][j][k+1],dp[i][j][k]+R[i]*B[k])
            if j<g and k<b:
                dp[i][j+1][k+1]=max(dp[i][j+1][k+1],dp[i][j][k]+G[j]*B[k])
print(dp[r][g][b])