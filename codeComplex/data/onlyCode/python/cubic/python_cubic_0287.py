R,G,B = map(int,input().split())
r = list(map(int, input().split()))
g = list(map(int, input().split()))
b = list(map(int, input().split()))
area = 0
r.sort(reverse=True)
b.sort(reverse=True)
g.sort(reverse=True)
L = max(len(r),len(g),len(b))
dp = [[[0]*(B+1) for i in range(G+1)]for j in range(R+1)]
# print(dp[r][g][b])
tr = 0
tg = 0
tb = 0
for i in range(R+1):
	for j in range(G+1):
		for k in range(B+1):
			if i>0 and j>0:
				dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k]+r[i-1]*g[j-1])
			if j>0 and k>0:
				dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1]+g[j-1]*b[k-1])
			if i>0 and k>0:
				dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1]+r[i-1]*b[k-1])
			area = max(area,dp[i][j][k])
print(area)