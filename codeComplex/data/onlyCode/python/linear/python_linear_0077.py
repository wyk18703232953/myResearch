from sys import stdin,stdout
# input=stdin.readline
mod=10**9+7
t=1
for _ in range(t):
    a=input()
    b=input()
    n=len(a)
    m=len(b)
    dp=[[0 for i in range(2)] for j in range(m+1)]
    dp[1][0]=int(b[0])^1
    dp[1][1]=int(b[0])
    for i in range(2,m+1):
        dp[i][0]=dp[i-1][0]+(int(b[i-1])^1)
        dp[i][1]=dp[i-1][1]+int(b[i-1])
    ans=0
    for i in range(n):
        count0=dp[m-n+i+1][0]-dp[i][0]
        count1=dp[m-n+i+1][1]-dp[i][1]
        ans+=count0*int(a[i])+count1*(int(a[i])^1)
    print(ans)