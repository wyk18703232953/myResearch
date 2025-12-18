#!/usr/bin/python3
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

MOD = m
MAX_N = 10**3

# Construct factorial table
fac = [1] + [0] * MAX_N
for i in range(1, MAX_N+1):
    fac[i] = fac[i-1] * (i) % MOD

fac_inv = [1] + [0] * MAX_N
# Femrmat's little theorem says a**(p-1) mod p == 1
# then, a * a**(p-2) mod p == 1
# it means that a**(p-2) is the inverse element
# Here, Get 1 / n! first
fac_inv[MAX_N] = pow(fac[MAX_N], MOD-2, MOD)
for i in range(MAX_N, 1, -1):
    fac_inv[i-1] = fac_inv[i] * i % MOD

def mod_nCr(n, r):
    if n < r or n < 0 or r < 0:
        return 0
    tmp = fac_inv[n-r] * fac_inv[r] % MOD
    return tmp * fac[n] % MOD

pow2 = [0] * (n+1)
pow2[0] = 1
for i in range(1, n+1):
    pow2[i] = pow2[i-1] * 2 % MOD

table = [[0] * 500 for _ in range(500)]
for i in range(500):
    for j in range(i+1):
        table[i][j] = mod_nCr(i, j)

# dp[i-th][j used]
dp = [[0] * (n+1) for _ in range(n)]
for i in range(n):
    dp[i][i+1] = pow2[i]
for i in range(n-1):
    for j in range(i // 2 + 1, n-1):
        if dp[i][j] == 0:
            continue
        dp[i][j] %= MOD
        for k in range(1, n-j):
            if i + k + 1 >= n:
                break
            # create new
            dp[i+k+1][j+k] += dp[i][j] * pow2[k-1] * table[k + j][k]

ans = sum(dp[-1]) % MOD
print(ans)