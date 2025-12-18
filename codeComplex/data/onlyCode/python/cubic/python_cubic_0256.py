from sys import stdin
inp = lambda : stdin.readline().strip()

nr, ng, nb = [int(x) for x in inp().split()]

r = [int(x) for x in inp().split()]
g = [int(x) for x in inp().split()]
b = [int(x) for x in inp().split()]
r.sort()
g.sort()
b.sort()
dp = [[[0 for _ in range(201)] for _ in range(201)] for _ in range(201)]
for i in range(nr+1):
    for j in range(ng+1):
        for k in range(nb+1):
            if i and j:
                dp[i][j][k]=max(dp[i][j][k], dp[i-1][j-1][k]+r[i-1]*g[j-1]);
            if i and k:
                dp[i][j][k]=max(dp[i][j][k], dp[i-1][j][k-1]+r[i-1]*b[k-1]);
            if j and k:
                dp[i][j][k]=max(dp[i][j][k], dp[i][j-1][k-1]+g[j-1]*b[k-1]);
 
print(dp[nr][ng][nb])