import sys
import math
import collections
import heapq
import decimal
input=sys.stdin.readline
n,m,k = map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
b=[]
for i in range(n-1):
    b.append(list(map(int,input().split())))
if(k%2==1):
    for i in range(n):
        for j in range(m):
            print(-1,end = " ")
        print()
else:
    k//=2
    pre=[[0 for i in range(m)]for j in range(n)]
    for x in range(k):
        curr = [[float("inf") for i in range(m)]for j in range(n)]
        for i in range(n):
            for j in range(m):
                if(j>0):
                    curr[i][j]=min(curr[i][j],pre[i][j-1]+a[i][j-1])
                if(i<n-1):
                    curr[i][j]=min(curr[i][j],pre[i+1][j]+b[i][j])
                if(j<m-1):
                    curr[i][j]=min(curr[i][j],pre[i][j+1]+a[i][j])
                if(i>0):
                    curr[i][j]=min(curr[i][j],pre[i-1][j]+b[i-1][j])
        pre=curr[:]
    for i in range(n):
        for j in range(m):
            print(2*pre[i][j],end = " ")
        print()