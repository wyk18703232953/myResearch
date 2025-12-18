n = int(input())
dp = [0]*101
dp[1] = 1
dp[2] = 2
for i in range(3, 101):
    dp[i] = dp[i-2]+i
print(dp[n])
