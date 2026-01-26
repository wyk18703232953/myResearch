'''
      Mayank Sheoran 
      BITS PILANI GOA CAMPUS 
''' 

n,m,k = map(int,input().split())
right = [[9999999 for i in range(m-1)] for j in range(n)]
down =  [[9999999 for i in range(m)] for j in range(n-1)]
for i in range(n):
    right[i] = list(map(int,input().split()))
for i in range(n-1):
    down[i] = list(map(int,input().split()))

if(k%2==1):
    for i in range(n):
        for j in range(m):
            print("-1",end=" ")
        print()
else:
    k = k//2
    row = n
    col = m
    dp  = [[[9999999 for i in range(m)] for j in range(n)] for ii in range(k+1)]
    for steps in range(k+1):
        for i in range(row):
            for j in range(col):
                if(steps==0):
                    dp[steps][i][j] = 0
                    continue
                ans = 99999999999
                if(i>0):
                    ans = min(ans,dp[steps-1][i-1][j]+down[i-1][j])
                if(i<n-1):
                    ans = min(ans,dp[steps-1][i+1][j]+down[i][j])
                if(j<m-1):
                    ans = min(ans,dp[steps-1][i][j+1]+right[i][j])
                if(j>0):
                    ans = min(ans,dp[steps-1][i][j-1]+right[i][j-1])
                dp[steps][i][j] = ans
                
    for i in range(n):
        for j in range(m):
            print(2*dp[k][i][j],end=" ")
        print()
    