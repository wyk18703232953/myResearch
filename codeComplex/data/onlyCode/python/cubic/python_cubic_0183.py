n = int(input())
a = list(map(int, input().split()))
 
dp = [[505]*n for _ in range(n)]
Max = [[0]*n for _ in range(n)]
 
for i in range(n):  
    dp[i][i] = 1
    Max[i][i] = a[i]
 
for len in range(1, n+1):
    for i in range(n-len+1):
        j = i + len - 1
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
            if dp[i][k] == 1 and dp[k+1][j] == 1 and Max[i][k] == Max[k+1][j]:
                dp[i][j] = 1
                Max[i][j] = Max[i][k] + 1
print(dp[0][n-1])