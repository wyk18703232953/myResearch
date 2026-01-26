import os,io
input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n,m,k=map(int,input().split())
dist1=[]
for i in range(n):
  dist1.append(list(map(int,input().split())))
dist2=[]
for i in range(n-1):
  dist2.append(list(map(int,input().split())))
if k%2:
  print(' '.join(map(str,[-1]*(n*m))))
  exit()
k//=2
dp=[10**9]*((k+1)*n*m)
for i in range(n):
  for j in range(m):
    dp[i*m+j]=0
for t in range(k):
  r=(t+1)*n*m
  q=t*n*m
  for i in range(n):
    for j in range(m):
      if i<n-1:
        dp[r+(i+1)*m+j]=min(dp[r+(i+1)*m+j],dp[q+i*m+j]+2*dist2[i][j])
      if i>0:
        dp[r+(i-1)*m+j]=min(dp[r+(i-1)*m+j],dp[q+i*m+j]+2*dist2[i-1][j])
      if j<m-1:
        dp[r+i*m+j+1]=min(dp[r+i*m+j+1],dp[q+i*m+j]+2*dist1[i][j])
      if j>0:
        dp[r+i*m+j-1]=min(dp[r+i*m+j-1],dp[q+i*m+j]+2*dist1[i][j-1])
ans=[]
for i in range(n):
  for j in range(m):
    ans.append(dp[k*n*m+i*m+j])
print(' '.join(map(str,ans)))