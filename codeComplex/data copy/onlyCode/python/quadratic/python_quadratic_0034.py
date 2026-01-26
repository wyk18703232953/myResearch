modulo = int(1e9+7)
n = int(input())
arr = [input() for i in range(n)]
dp = [1]
for i in range(n):
    if arr[i] == 'f':
        dp.append(0)
        continue;
    for j in range(1, len(dp)):
        dp[j] = (dp[j] + dp[j-1]) % modulo
print(dp[-1])