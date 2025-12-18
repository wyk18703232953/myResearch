import sys
input = sys.stdin.readline

n, mod = map(int, input().split())
fac = [1] + [0] * (n + 1)
inv = [1] + [0] * (n + 1)
C = [[0] * (n + 2) for _ in range(n + 2)]
p2 = [1] + [0] * (n + 1)
for i in range(1, n + 2):
    fac[i] = fac[i - 1] * i % mod
    p2[i] = p2[i - 1] * 2 % mod
inv[-1] = pow(fac[-1], mod - 2, mod)
for i in range(n, 0, -1):
    inv[i] = inv[i + 1] * (i + 1) % mod
for i in range(n + 2):
    for j in range(i + 1):
        C[i][j] = fac[i] * inv[j] % mod * inv[i - j] % mod
dp = [[0] * (n + 2) for _ in range(n + 2)]
dp[0][0] = 1
for i in range(n):
    for j in range(i + 1):
        for k in range(1, n - i + 1):
            dp[i + k + 1][j + k] += dp[i][j] * p2[k - 1] % mod * C[j + k][k] % mod
            dp[i + k + 1][j + k] %= mod
ans = 0
for i in range(n + 1):
    ans = (ans + dp[n + 1][i]) % mod
print(ans)