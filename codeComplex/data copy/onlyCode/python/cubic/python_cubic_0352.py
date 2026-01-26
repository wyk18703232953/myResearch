def nr(): return nrs()[0]
def nrs(): return [int(i) for i in input().split()]

n = 10**7
squares = [i * i for i in range(1, 3162)]

p = [i for i in range(n + 1)]
for i in range(1, n + 1):
	if p[i] == i:
		for sq in squares:
			if i * sq > n: break
			p[i * sq] = i

for _ in range(nr()):
	N, K = nrs()
	A = [p[a] for a in nrs()]
	dp = [N] * (K + 1)
	dp[0] = 1
	used = [set()] * (K + 1)
	for a in A:
		for j in range(K, -1, -1):
			if dp[j] == N: continue
			if a in used[j]:
				if j < K and dp[j + 1] > dp[j]:
					dp[j + 1] = dp[j]
					used[j + 1] = used[j]
				dp[j] += 1
				used[j] = set([a])
			else:
				used[j].add(a)
	print(min(dp))
