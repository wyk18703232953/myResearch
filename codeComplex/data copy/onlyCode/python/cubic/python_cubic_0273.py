
r,g,b = map(int,input().split())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l3 = list(map(int,input().split()))
l1.sort(reverse=True)
l2.sort(reverse=True)
l3.sort(reverse=True)
dp = [[ ['*' for cc1 in range(b+1)] for cc2 in range(g+1)] for r in range(r+1)]
ans = 0
for i in range(r+1):
    for j in range(g+1):
        for k in range(b+1):
            if i == 0 and j == 0:
                dp[i][j][k] = 0
            if j == 0 and k == 0:
                dp[i][j][k] = 0
            if i == 0 and k == 0:
                dp[i][j][k] = 0
            if i>0 and j>0 and k>0:
                dp[i][j][k] = max(l1[i-1]*l2[j-1] + dp[i-1][j-1][k],l1[i-1]*l3[k-1] + dp[i-1][j][k-1],l2[j-1]*l3[k-1] + dp[i][j-1][k-1])
            else:
                if i>0 and j>0:
                    dp[i][j][k] = l1[i-1]*l2[j-1] + dp[i-1][j-1][k]
                elif i>0 and k>0:
                    dp[i][j][k] = l1[i-1]*l3[k-1] + dp[i-1][j][k-1]
                elif j>0 and k>0:
                    dp[i][j][k] = l2[j-1]*l3[k-1] + dp[i][j-1][k-1]
            ans = max(ans,dp[i][j][k])
                    
print(ans)
                                   
                
            
