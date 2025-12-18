from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

R,G,B=nii()
r=lnii()
g=lnii()
b=lnii()

r.sort(reverse=True)
g.sort(reverse=True)
b.sort(reverse=True)

dp=[[[0]*(B+1) for i in range(G+1)] for j in range(R+1)]

for i in range(R+1):
  for j in range(G+1):
    for k in range(B+1):
      c=False
      if i<R and j<G:
        dp[i+1][j+1][k]=max(dp[i+1][j+1][k],dp[i][j][k]+r[i]*g[j])
        c=True
      if j<G and k<B:
        dp[i][j+1][k+1]=max(dp[i][j+1][k+1],dp[i][j][k]+g[j]*b[k])
        c=True
      if k<B and i<R:
        dp[i+1][j][k+1]=max(dp[i+1][j][k+1],dp[i][j][k]+b[k]*r[i])
        c=True

      if not c:
        if i<R:
          dp[i+1][j][k]=max(dp[i+1][j][k],dp[i][j][k])
        if j<G:
          dp[i][j+1][k]=max(dp[i][j+1][k],dp[i][j][k])
        if k<B:
          dp[i][j][k+1]=max(dp[i][j][k+1],dp[i][j][k])

ans=0
for i in dp:
  for j in i:
    ans=max(ans,max(j))

print(ans)