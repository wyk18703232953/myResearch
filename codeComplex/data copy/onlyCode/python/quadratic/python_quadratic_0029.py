MOD = int(1e9+7)
n = int(input())
a = [input() for i in range(n)]
dp = [1]
for i in range(n):
    if a[i] == 'f':
        dp.append(0)
        continue
    for j in range(1, len(dp)):
        dp[j] = (dp[j] + dp[j-1]) % MOD
print(dp[-1])
