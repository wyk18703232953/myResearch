n,k = [int(x) for x in input().split()]
dp = [[[0 for _ in range(4)] for _ in range(k+2)] for _ in range(2)]
dp[1][2][0] = 1
dp[1][2][1] = 1
dp[1][1][2] = 1
dp[1][1][3] = 1



for n1 in range(1,n):
    for k1 in range(1,k+1):
        
        dp[0][k1][0] = dp[1][k1][0]
        dp[0][k1][1] = dp[1][k1][1]
        dp[0][k1][2] = dp[1][k1][2]
        dp[0][k1][3] = dp[1][k1][3]
        
        dp[1][k1][0] = (dp[0][k1][0] + (dp[0][k1-2][1] if k1-2>=0 else 0) + dp[0][k1-1][2] + dp[0][k1-1][3])% 998244353 
        
        dp[1][k1][1] = (dp[0][k1][1] + (dp[0][k1-2][0] if k1-2>=0 else 0) + dp[0][k1-1][2] + dp[0][k1-1][3])% 998244353 
        
        dp[1][k1][2] = (dp[0][k1][2] + (dp[0][k1][1]) + dp[0][k1][0] + dp[0][k1-1][3])% 998244353 
        
        dp[1][k1][3] = (dp[0][k1][3] + (dp[0][k1][1]) + dp[0][k1][0] + dp[0][k1-1][2])% 998244353 
total = 0
#print(dp)
for i in range(4):
    total += dp[1][k][i] % 998244353 
#print(dp)
print(total% 998244353 )
        
        
                        
