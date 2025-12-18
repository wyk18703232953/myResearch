#   Author: yumtam
#   Created at: 2021-05-03 00:42

from __pypy__.intop import int_mulmod

n_, MOD = [int(t) for t in input().split()]

def mul(a, b):
    return int_mulmod(a, b, MOD)

N = 410
dp = [[0] * (N+1) for _ in range(N+1)]

fact = [1]
for x in range(1, N):
    fact.append(fact[-1] * x % MOD)

inv_fact = [0] * N
inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
for x in reversed(range(1, N)):
    inv_fact[x - 1] = inv_fact[x] * x % MOD

def nCr(n, r):
    return mul(fact[n], mul(inv_fact[n-r], inv_fact[r]))

for n in range(1, N+1):
    dp[n][n] = pow(2, n-1, MOD)
    for i in range(1, n-1):
        j = n-i-1
        for k in range(1, i+1):
            dp[n][k+j] = (dp[n][k+j]
                          + mul(nCr(k+j, k), mul(dp[i][k], dp[j][j]))) % MOD

print(sum(dp[n_]) % MOD)
