import sys
input=sys.stdin.buffer.readline

n=int(input())
a=list(map(int,input().split()))
dp=[[0]*(n) for i in range(n)]
for i in range(n):
    dp[i][i]=a[i]
count=1
for i in range(n-1):
    for j in range(n-i-1):
        dp[j][j+count]=dp[j][j+count-1]^dp[j+1][j+count]
    count+=1
count=1
for i in range(n-1):
    for j in range(n-i-1):
        dp[j][j+count]=max(dp[j][j+count],dp[j][j+count-1],dp[j+1][j+count])
    count+=1
for i in range(int(input())):
    l,r=map(int,input().split())
    l-=1
    r-=1
    print(dp[l][r])