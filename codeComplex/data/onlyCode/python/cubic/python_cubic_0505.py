from collections import defaultdict
from sys import stdout,stdin
n,m,K=map(int,input().split())
dp=[[[0 for h in range(11)]for j in range(m+1)] for i in range(n+1)]
l1=[list(map(int,stdin.readline().split())) for i in range(n)]#i,j i,j+1
l2=[list(map(int,stdin.readline().split())) for i in range(n-1)]#i,j i+1,j
if K%2:
    for i in range(n):
        for j in range(m):
            print('-1',end=' ')
        print()
else:
    for k in range(1,K//2+1):
     for i in range(n):
        for j in range(m):
                res=100000000
                if i-1>=0 and j>=0:
                     res=min(res,l2[i-1][j]+dp[i-1][j][k-1])
                if i+1<n and j>=0:
                     res=min(res,l2[i][j]+dp[i+1][j][k-1])
                if 0<=i and j+1<m:
                     res=min(res,l1[i][j]+dp[i][j+1][k-1])
                if 0<=i and j-1>=0:
                     res=min(res,l1[i][j-1]+dp[i][j-1][k-1])
                dp[i][j][k]=res
    for i in range(n):
        for j in range(m):
            stdout.write(str(2*dp[i][j][K//2])+' ')
        stdout.write('\n')