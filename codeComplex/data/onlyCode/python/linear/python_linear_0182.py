from sys import stdin, stdout
from itertools import accumulate
nmbr = lambda: int(stdin.readline())
lst = lambda: list(map(int, stdin.readline().split()))
for _ in range(1):#nmbr()):
    n,k=lst()
    a=lst()
    b=lst()
    ps=list(accumulate(a))
    dp=[[0 for _ in range(2)] for _ in range(1+n)]
    for i in range(1,n+1):
        dp[i][0]=dp[i-1][0]+a[i-1]*b[i-1]
        dp[i][1]=max(dp[i-1][1]+a[i-1]*b[i-1],ps[i-1]-(ps[i-k-1] if i-k-1>=0 else 0)+dp[max(i-k,0)][0])
    # print(dp)
    print(max(dp[n]))