n, K = map(int, input().split())
mod = 998244353
if K == 1:
    print(2)
    exit()
dp = [[0]*(2**2) for i in range(K+1)]
dp[1][0] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[1][3] = 1
for i in range(1, n):
    nx = [[0]*(2**2) for i in range(K+1)]
    for k in range(K+1):
        for j in range(4):
            if j == 0:
                nx[k][0] += dp[k][j]%mod
                if k+1 <= K:
                    nx[k+1][1] += dp[k][j]%mod
                    nx[k+1][2] += dp[k][j]%mod
                    nx[k+1][3] += dp[k][j]%mod
            elif j == 1:
                nx[k][0] += dp[k][j]%mod
                nx[k][1] += dp[k][j]%mod
                if k+2 <= K:
                    nx[k+2][2] += dp[k][j]%mod
                nx[k][3] += dp[k][j]%mod
            elif j == 2:
                nx[k][0] += dp[k][j]%mod
                if k+2 <= K:
                    nx[k+2][1] += dp[k][j]%mod
                nx[k][2] += dp[k][j]%mod
                nx[k][3] += dp[k][j]%mod
            else:
                if k+1 <= K:
                    nx[k+1][0] += dp[k][j]%mod
                    nx[k+1][1] += dp[k][j]%mod
                    nx[k+1][2] += dp[k][j]%mod
                nx[k][3] += dp[k][j]%mod
    dp = nx
#print(dp)
print(sum(dp[K])%mod)
