def cal(r, g, b):
	if dp[r][g][b] != -1:
		return dp[r][g][b]

	area = 0
	if r<R and g<G:
		area = max(area, rl[r] * gl[g] + cal(r+1, g+1, b))
	if r<R and b<B:
		area = max(area, rl[r] * bl[b] + cal(r+1, g, b+1))
	if g<G and b<B:
		area = max(area, gl[g] * bl[b] + cal(r, g+1, b+1))
	dp[r][g][b] = area
	return area

if __name__ == "__main__":
	R, G, B = map(int,input().split())
	rl = sorted(list(map(int,input().split())), reverse=True)
	gl = sorted(list(map(int,input().split())), reverse=True)
	bl = sorted(list(map(int,input().split())), reverse=True)
	dp = [[[-1]*(B+1) for i in range(G+1)] for i in range(R+1)]
	print(cal(0,0,0))
