
s = [input(), input()]
n = len(s[0])

dp = [[0,0,0] for _ in range(n+1)]

for i in range(n-2,-1,-1):
    dp[i] = [dp[i+1][0]]*3
    vals = [0,0,0,0]
    if s[0][i] == '0' and s[0][i+1] == '0' and s[1][i] == '0':
        vals[0] = dp[i+1][2] + 1
    if s[0][i] == '0' and s[0][i+1] == '0' and s[1][i+1] == '0':
        vals[1] = dp[i+2][0] + 1
    if s[1][i] == '0' and s[0][i+1] == '0' and s[1][i+1] == '0':
        vals[2] = dp[i+2][0] + 1
    if s[0][i] == '0' and s[1][i] == '0' and s[1][i+1] == '0':
        vals[3] = dp[i+1][1] + 1
    dp[i][1] = max(dp[i+1][0], vals[1])
    dp[i][2] = max(dp[i+1][0], vals[2])
    dp[i][0] = max(dp[i][1], dp[i][2], *vals)

result = max(dp[0])
print(result)
