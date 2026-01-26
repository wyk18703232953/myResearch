from sys import stdin
input=stdin.readline
n,m,k=map(int,input().split())
lr=[list(map(int,input().split())) for i in range(n)] # (i,j),(i,j+1)
ud=[list(map(int,input().split())) for i in range(n-1)] # (i,j),(i+1,j)
if k%2:
  arr=[-1]*m
  for i in range(n):
    print(*arr)
  exit()
kk=k//2
dp=[[[10**10]*(kk+1) for i in range(m)] for j in range(n)]
for i in range(n):
  for j in range(m):
    dp[i][j][0]=0
for z in range(1,kk+1):
  for i in range(n):
    for j in range(m):
      if i>0:
        dp[i][j][z]=min(dp[i][j][z],dp[i-1][j][z-1]+ud[i-1][j])
      if i<n-1:
        dp[i][j][z]=min(dp[i][j][z],dp[i+1][j][z-1]+ud[i][j])
      if j>0:
        dp[i][j][z]=min(dp[i][j][z],dp[i][j-1][z-1]+lr[i][j-1])
      if j<m-1:
        dp[i][j][z]=min(dp[i][j][z],dp[i][j+1][z-1]+lr[i][j])
ans=[[dp[i][j][kk]*2 for j in range(m)] for i in range(n)]
for i in range(n):
  print(*ans[i])