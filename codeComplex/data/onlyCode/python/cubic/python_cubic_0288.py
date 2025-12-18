R,G,B = map(int,input().split())
r = list(map(int,input().split()))
g = list(map(int,input().split()))
b = list(map(int,input().split()))
r.sort()
g.sort()
b.sort()
dp = []
for i in range(R+1):
	d = []
	for j in range(G+1):
		d.append([0]*(B+1))
	dp.append(d)
for i in range(R+1):
	for j in range(G+1):
		for k in range(B+1):
			if i+j+k<2:
				continue
			if i>0 and j>0:
				dp[i][j][k] = max(dp[i][j][k],dp[i-1][j-1][k]+r[i-1]*g[j-1])
			if i>0 and k>0:
				dp[i][j][k] = max(dp[i][j][k],dp[i-1][j][k-1]+r[i-1]*b[k-1])
			if j>0 and k>0:
				dp[i][j][k] = max(dp[i][j][k],dp[i][j-1][k-1]+g[j-1]*b[k-1])
print(dp[R][G][B])

