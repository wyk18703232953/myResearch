R, G, B = map(int, input().split())
L = [sorted(map(int, input().split())) for _ in range(3)]
 
DP = [0] * ((R+1) * (G+1) * (B+1))
def idx(r, g, b): return r * (G+1) * (B+1) + g * (B+1) + b
 
for r in range(R+1):
	for g in range(G+1):
		for b in range(B+1):
			best = 0
 
			if r:
				if g: best = L[0][r-1] * L[1][g-1] + DP[idx(r-1, g-1, b)]
				if b: best = max(best, L[0][r-1] * L[2][b-1] + DP[idx(r-1, g, b-1)])
 
			if g and b:
				best = max(best, L[1][g-1] * L[2][b-1] + DP[idx(r, g-1, b-1)])
 
			DP[idx(r, g, b)] = best
 
print(max(DP))