N = 1010

dp = [[[0] * 4 for j in range(N*2)] for i in range(N)]
dp[0][1][0] = dp[0][1][1] = dp[0][2][2] = dp[0][2][3] = 1
m = 998244353
for i in range(N-1):
    for j in range(1,N*2-5):
        for me in range(4):
            for he in range(4):
                if me <= 1:
                    if he <= 1:
                        dp[i+1][j+(he!=me)][he] = (dp[i+1][j+(he!=me)][he] + dp[i][j][me]) % m
                    else:
                        dp[i+1][j+1][he] = (dp[i+1][j+1][he] + dp[i][j][me]) % m
                else:
                    if he <= 1:
                        dp[i+1][j][he] = (dp[i+1][j][he] + dp[i][j][me]) % m
                    else:
                        dp[i+1][j + (he != me)*2][he] = (dp[i+1][j+(he!=me)*2][he] + dp[i][j][me]) % m
n,k = map(int,input().split())
print(sum(dp[n-1][k])%m)                        
