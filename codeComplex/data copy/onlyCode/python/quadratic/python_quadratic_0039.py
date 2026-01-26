M=10**9+7
n=int(input())
a=[]
for i in range(n):
    a.append(input())
dp=[[0]*(n+5) for i in range(n+2)]
dp[0][0]=1
for i in range(1,n):
    count=0
    if a[i-1]=='f':
        for j in range(n-2,-1,-1):
            if dp[i-1][j]>0:
                dp[i][j+1]=(dp[i][j+1]+dp[i-1][j])%M
    else:
        for j in range(n-2,-1,-1):
            if dp[i-1][j]>0:
                count=(count+dp[i-1][j])%M
            dp[i][j]=(dp[i][j]+count)%M
print(sum(dp[n-1])%M)