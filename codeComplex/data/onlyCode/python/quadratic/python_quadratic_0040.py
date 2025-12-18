import sys
input=sys.stdin.readline
n=int(input())
c=[" "]+[input().rstrip() for i in range(n)]
mod=10**9+7
dp=[[0]*(n+1) for i in range(n+1)]
dp[1][0]=1
sdp=[0]*(n+1)
sdp[0]=1
for i in range(1,n+1):
    if i>=2 and c[i-1]=="f":
        for j in range(1,n+1):
            dp[i][j]=dp[i-1][j-1]
            dp[i][j]%=mod
        dp[i][0]=0
    else:
        for j in range(n+1):
            dp[i][j]=sdp[j]
            dp[i][j]%=mod
    sdp=[dp[i][j] for j in range(n+1)]
    for j in range(1,n+1)[::-1]:
        sdp[j-1]+=sdp[j]
        sdp[j-1]%=mod
print(sdp[0]%mod)