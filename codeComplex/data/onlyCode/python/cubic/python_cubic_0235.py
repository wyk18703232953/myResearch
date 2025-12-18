from sys import stdin
from array import array
def recSolve(dp,r,g,b,rx,gx,bx, R, G, B):
	if rx == R:
		return sum(a * b for a, b in zip(g[gx:], b[bx:]))
	if gx == G:
		return sum(a * b for a, b in zip(r[rx:], b[bx:]))
	if bx == B:
		return sum(a * b for a, b in zip(g[gx:], r[rx:]))
	if dp[rx * G * B + gx * B + bx] != -1:
		return dp[rx * G * B + gx * B + bx]
	rg = recSolve(dp, r, g, b, rx + 1, gx + 1, bx, R, G, B) + r[rx] * g[gx]
	bg = recSolve(dp, r, g, b, rx, gx + 1, bx + 1, R, G, B) + b[bx] * g[gx]
	rb = recSolve(dp, r, g, b, rx + 1, gx, bx + 1, R, G, B) + r[rx] * b[bx]
	ans = max(rg, bg, rb)
	dp[rx * G * B + gx * B + bx] = ans
	return ans
input = stdin.readline
R, G, B = map(int, input().split())
r = sorted([*map(int, input().split())], reverse = True)
g = sorted([*map(int, input().split())], reverse = True) 
b = sorted([*map(int, input().split())], reverse = True) 
dp = array('q', (-1 for x in range(R * G * B)))
print(recSolve(dp, r, g, b, 0, 0, 0, R, G, B))