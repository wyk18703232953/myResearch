R,G,B=list(map(int,input().split()))
r=list(map(int,input().split()))
g=list(map(int,input().split()))
b=list(map(int,input().split()))
r.sort(reverse=True)
g.sort(reverse=True)
b.sort(reverse=True)
dp = [[[0 for i in range(B + 1)] for j in range(G + 1)] for k in range(R + 1)]
ans=0
for i in range(R+1):
    for j in range(G+1):
        for k in range(B+1):
            if i<R and j<G:
                dp[i+1][j+1][k]=max(dp[i+1][j+1][k],r[i]*g[j]+dp[i][j][k])
            if i<R and k<B:
                dp[i+1][j][k+1]=max(dp[i+1][j][k+1],r[i]*b[k]+dp[i][j][k])
            if k<B and j<G:
                dp[i][j+1][k+1]=max(dp[i][j+1][k+1],b[k]*g[j]+dp[i][j][k])
            ans=max(ans,dp[i][j][k])
print(ans)