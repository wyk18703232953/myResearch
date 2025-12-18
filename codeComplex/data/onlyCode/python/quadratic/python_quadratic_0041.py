mod=10**9+7
n=int(input())
l=[]
c=0
for i in range(n):
    l.append(input())
dp=[[0]*(n+2) for i in range(n+1)]
for i in range(n+2):
    dp[n][i]=1
for i in range(n-1,0,-1):
    s=0
    for j in range(n+1):
        s+=dp[i+1][j]
        s%=mod
        if l[i-1]=='f':
            dp[i][j]=dp[i+1][j+1]
        else:
            dp[i][j]=s

print(dp[1][0])
    
