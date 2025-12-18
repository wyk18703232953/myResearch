n,k=map(int,input().split())
mod=998244353
dp=[[0,0,0,0] for _ in range(k+1)]
#dp[0][0]=dp[0][1]=dp[0][2]=dp[0][3]=
dp[1][0]=dp[1][3]=1
if k>1:
    dp[2][2]=dp[2][1]=1
for x in range(1,n):
    g=[[0,0,0,0] for _ in range(k+1)]
    # 0 - bb
    # 1 - bw
    # 2 - wb
    # 3 - ww
    g[1][0]=g[1][3]=1
    for i in range(2,k+1):
        g[i][0]=(dp[i][0]+dp[i][1]+dp[i][2]+dp[i-1][3])%mod
        g[i][1]=(dp[i-1][0]+dp[i][1]+dp[i-2][2]+dp[i-1][3])%mod
        g[i][2]=(dp[i-1][0]+dp[i-2][1]+dp[i][2]+dp[i-1][3])%mod
        g[i][3]=(dp[i-1][0]+dp[i][1]+dp[i][2]+dp[i][3])%mod
    dp=g
print(sum(dp[-1])%mod)