from sys import stdin,stdout
from collections import deque
nmbr = lambda: int(input())
lst = lambda: list(map(int, input().split()))
PI=float('inf')
M=10**9+7
for _ in range(1):#nmbr()):
    n=nmbr()
    s=[input() for _ in range(n)]
    dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,n):
        for j in range(n):
            if i>=1 and s[i-1]=='f':
                if j>=1:dp[i][j]=dp[i-1][j-1]-(dp[i-1][j])
            elif i>=1:
                dp[i][j]=dp[i-1][j]
            dp[i][j]%=M
        for k in range(n-1,-1,-1):
            dp[i][k]=(dp[i][k]+dp[i][k+1])%M
    # print(*dp,sep='\n')
    print(dp[n-1][0]%M)