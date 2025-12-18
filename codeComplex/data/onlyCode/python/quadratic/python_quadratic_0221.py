from sys import stdin,stdout
nmbr=lambda:int(stdin.readline())
lst=lambda:list(map(int,stdin.readline().split()))
for _ in range(1):#nmbr()):
    n=nmbr()
    a=lst()
    b=lst()
    dp=[0]*n
    for i in range(n):
        v=float('inf')
        for j in range(i+1,n):
            if a[j]>a[i]:v=min(v,b[i]+b[j])
        dp[i]=v
    # print(dp)
    for i in range(n):
        v = float('inf')
        for j in range(i + 1, n):
            if a[j] > a[i]: v = min(v, b[i] + dp[j])
        dp[i] = v
    ans=min(dp)
    print(ans if ans!=float('inf') else -1)