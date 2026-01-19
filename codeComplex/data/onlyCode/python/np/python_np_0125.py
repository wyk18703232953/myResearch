import math
g=0
n=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
dp=dict()
dp[0]=0
s=set([0])
for i in range(n):
    for j in s:
        g=math.gcd(j,b[i])
        if g in dp:
            dp[g]=min(dp[g],dp[j]+c[i])
        else:
            dp[g]=dp[j]+c[i]

    s=set(dp.keys())



if 1 in dp.keys():
    print(dp[1])
else:
    print(-1)