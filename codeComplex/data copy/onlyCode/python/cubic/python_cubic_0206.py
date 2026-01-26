r,g,b=map(int,input().split())
rs=sorted(list(map(int,input().split())))
gs=sorted(list(map(int,input().split())))
bs=sorted(list(map(int,input().split())))
dp=[[[0 for i in range(b+1)] for j in range(g+1)] for k in range(r+1)]
ans=0
for i in range(r+1):
    for j in range(g+1):
        for k in range(b+1):
            if i>0 and k>0:
                dp[i][j][k]=max(dp[i][j][k],dp[i-1][j][k-1]+rs[i-1]*bs[k-1])
            if i>0 and j>0:
                dp[i][j][k]=max(dp[i][j][k],dp[i-1][j-1][k]+rs[i-1]*gs[j-1])
            if j>0 and k>0:
                dp[i][j][k]=max(dp[i][j][k],dp[i][j-1][k-1]+gs[j-1]*bs[k-1])
            ans=max(ans,dp[i][j][k])
print(ans)
