import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
f=[[0]*n for i in range(n)]
for i in range(n):
    f[0][i]=a[i]
for i in range(1,n):
    for j in range(n-i):
        f[i][j]=f[i-1][j]^f[i-1][j+1]
for i in range(1,n):
    for j in range(n-i):
        f[i][j]=max(f[i][j],f[i-1][j],f[i-1][j+1])
q=int(input())
for _ in range(q):
    l,r=map(int,input().split())
    print(f[r-l][l-1])