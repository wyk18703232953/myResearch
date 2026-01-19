import sys
from math import gcd
from collections import defaultdict as dd
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
c=list(map(int,input().split()))
dp=dict()
for i in range(n):
    if dp.get(l[i]):
        dp[l[i]]=min(dp[l[i]],c[i])
    else:
        dp[l[i]]=c[i]
for ll in l:
    keys=list(dp.keys())
    for j in keys:
        g=gcd(j,ll)
        if dp.get(g):
            dp[g]=min(dp[g],dp[ll]+dp[j])
        else:
            dp[g]=dp[ll]+dp[j]
if 1 in dp:
    print(dp[1])
else:
    print(-1)