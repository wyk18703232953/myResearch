def solve():
  r, g, b = map(int, input().split());R,G,B = sorted(list(map(int, input().split()))),sorted(list(map(int, input().split()))),sorted(list(map(int, input().split())));dp = [[[0]*(b+1) for _ in range(g+1)] for _ in range(r+1)]
  for i in range(r+1):
    for j in range(g+1):
      for k in range(b+1):
        if i+j+k<2:continue
        if i>0 and j>0:dp[i][j][k] = max(dp[i][j][k],dp[i-1][j-1][k]+R[i-1]*G[j-1])
        if i>0 and k>0:dp[i][j][k] = max(dp[i][j][k],dp[i-1][j][k-1]+R[i-1]*B[k-1])
        if j>0 and k>0:dp[i][j][k] = max(dp[i][j][k],dp[i][j-1][k-1]+G[j-1]*B[k-1])
  return dp[r][g][b]
print(solve())