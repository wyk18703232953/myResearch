from sys import stdin,stdout
nmbr = lambda: int(stdin.readline())
lst = lambda: list(map(int, stdin.readline().split()))
for _ in range(1):#nmbr()):
    n=nmbr()
    a=lst()
    b=lst()
    ans=PI=float('inf')
    dp=[[PI for _ in range(4)] for _ in range(n)]
    for i in range(n):
        dp[i][1]=b[i]
        for j in range(i):
            if a[j]<a[i]:
                dp[i][2]=min(dp[i][2],dp[j][1]+b[i])
                dp[i][3]=min(dp[i][3],dp[j][2]+b[i])
                ans=min(ans,dp[i][3])
    print(ans if ans!=PI else -1)