r,g,b = map(int,input().split())
R = list(map(int,input().split()))
G = list(map(int,input().split()))
B = list(map(int,input().split()))
R.sort()
G.sort()
B.sort()
dp = [[[-1 for i in range(b+1)] for j in range(g+1)] for k in range(r+1)]
def solve(r,g,b):
	if ((r==0 and g==0) or (g==0 and b==0) or (b==0 and r==0)):
		return 0
	if dp[r][g][b]==-1:
		if r==0:
			ans =  G[g-1]*B[b-1]+solve(r,g-1,b-1)
		elif g==0:
			ans =  R[r-1]*B[b-1]+solve(r-1,g,b-1)
		elif b==0:
			ans =  G[g-1]*R[r-1]+solve(r-1,g-1,b)
		else:
			ans =  max(G[g-1]*B[b-1]+solve(r,g-1,b-1),G[g-1]*R[r-1]+solve(r-1,g-1,b),R[r-1]*B[b-1]+solve(r-1,g,b-1))
		dp[r][g][b] = ans
	return dp[r][g][b]
ans = solve(r,g,b)
print(ans)