
mod = 998244353
N,K = map(int, input().split())

dp = [[[0]*(K+2) for i in range(2)] for i in range(N)]
dp[0][0][0] = 1
dp[0][1][1] = 1

for i in range(1,N):
    for b in range(K):
        dp[i][0][b]   += dp[i-1][0][b]
        dp[i][0][b]   += dp[i-1][1][b]
        dp[i][0][b]   += dp[i-1][1][b]
        dp[i][0][b+1] += dp[i-1][0][b]
        dp[i][0][b]   %= mod

        dp[i][1][b+1] += dp[i-1][0][b]
        dp[i][1][b]   += dp[i-1][1][b]
        dp[i][1][b+2] += dp[i-1][1][b]
        dp[i][1][b+1] += dp[i-1][0][b]
        dp[i][1][b] %= mod

ans = 0
for x in range(2):
    ans += dp[N-1][x][K-1]

print(ans*2%mod)
