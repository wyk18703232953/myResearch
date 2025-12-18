c = [[0 for i in range(5205)] for j in range(5205)]
K = 998244353
inv = [0 for i in range(5205)]

def mu(a, n):
	if n == 0: return 1
	q = mu(a, n // 2)
	if n % 2 == 0:
		return q * q % K
	else: return q * q % K * a % K

def calc(m, d, S):
	res = 0
	if m == 0:
		if S == 0: return 1
		return 0

	for u in range(0, m + 1):
		if (u * d > S): break
		U = c[m][u] * c[S - u * d + m - 1][m - 1] % K 
		if u % 2 == 0:
			res = (res + U) % K
		else: res = (res - U + K) % K 
	return res


c[0][0] = 1
inv[0] = 1
for i in range(1, 5101):
	inv[i] = mu(i, K - 2)

for i in range(1, 5101):
	c[i][0] = 1
	for j in range (1, i):
		c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % K
	c[i][i] = 1

p, s, r = map(int, input().split())

res = 0
den = 0

for i in range(1, p + 1):
	A = 0
	for d in range(r, s // i + 1):
		if (i < p): A = (A + calc(p - i, d, s - d * i)) % K
		else:
			if (s - i * d == 0): A += 1
	A = A * inv[i] % K
	res = (res + A * c[p - 1][i - 1] % K) % K

den = c[s - r + p - 1][p - 1]
res = res * mu(den, K - 2) % K
print(res)


