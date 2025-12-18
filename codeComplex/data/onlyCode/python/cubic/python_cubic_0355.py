def nr(): return nrs()[0]
def nrs(): return [int(i) for i in input().split()]

def get_prime(n):
	res = []
	for i in range(2,n):
		is_prime = True
		for x in res:
			if i % x == 0:
				is_prime = False
				break
		if is_prime: res.append(i)
	return res

prime = get_prime(3162)

#cache = {}
def get_mask (num):
	#key = num
	#if key in cache: return cache[key]
	dv = []
	for p in prime:
		c = 0
		while num % p == 0:
			c += 1
			num = num // p
		if c % 2 == 1:
			dv.append(p)
		if num < p * p:
			break

	for x in dv:
		num *= x

	#cache[key] = num
	return num

for _ in range(nr()):
	N, K = nrs()
	A = nrs()
	dp = [N] * (K + 1)
	dp[0] = 1
	used = [{}] * (K + 1)
	for a in A:
		a = get_mask(a)
		for j in range(K, -1, -1):
			if dp[j] == N: continue
			if a in used[j]:
				if j < K and dp[j + 1] > dp[j]:
					dp[j + 1] = dp[j]
					used[j + 1] = used[j]
				dp[j] += 1
				used[j] = {}
			used[j][a] = 1
	print(min(dp))
