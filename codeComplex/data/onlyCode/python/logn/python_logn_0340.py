def pow_mod(x, pwr, mod):
	res = 1
	multiplier = x
	while pwr > 0:
		if pwr%2 == 1: 
			res = res*multiplier % mod
		multiplier = multiplier*multiplier % mod

		pwr //= 2

	return res

[x, k] = map(int, input().split())

MOD = 1000000007

if x == 0:
	res = 0
else:
	res = pow_mod(2, k+1, MOD)*x % MOD
	res = (res - pow_mod(2, k, MOD)) % MOD
	res = (res + 1) % MOD

print(res)