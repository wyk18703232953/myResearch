from sys import stdin, stdout
n=int(input())
s=list(map(int,stdin.readline().strip().split()))
dp=[[-1 for i in range(n+1)]for j in range(n+1)]
for i in range(n):
    dp[0][i]=s[i]
for i in range(1,n):
    for j in range(n-i):
        dp[i][j]=dp[i-1][j]^dp[i-1][j+1]
for i in range(1,n):
    for j in range(n-i):
        dp[i][j]=max(dp[i-1][j],dp[i-1][j+1],dp[i][j])
q=int(input())
ans=""
for i in range(q):
    l,r=map(int,stdin.readline().strip().split())
    print(dp[r-l][l-1])
