import sys

maxN = 10**6 + 5
dp = [0] * maxN
b = [0] * maxN

N = int(sys.stdin.readline())
for _ in range(N):
    beacon = [int(x) for x in sys.stdin.readline().split()]
    b[beacon[0]] = beacon[1]

if b[0] > 0:
    dp[0] = 1

for i in range(1, maxN):
    if b[i] == 0:
        dp[i] = dp[i-1]
    else:
        if b[i] >= i:
            dp[i] = 1
        else:
            dp[i] = dp[i-b[i]-1]+1
print(N-max(dp))

