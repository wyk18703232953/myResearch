R, G, B = map(int, input().split())
r = list(map(int, input().split()))
g = list(map(int, input().split()))
b = list(map(int, input().split()))
r.sort()
g.sort()
b.sort()
# State- dp[i][j][k] represents max value after choosing i elements from r, j elements from g, k elements from b
dp = [[[0]*202 for i in range(202)] for j in range(202)]
for i in range(R+1):
       for j in range(G+1):
              for k in range(B+1):
                     if i and j:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k]+r[i-1]*g[j-1])
                     if i and k:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1]+r[i-1]*b[k-1])
                     if k and j:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1]+g[j-1]*b[k-1])
print(dp[R][G][B])
