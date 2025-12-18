
import sys
input = sys.stdin.buffer.readline

n,k=map(int,input().split())
arr=[int(x) for x in input().split()]

x=0
dp=[]
for i in range(n):
    x=x+arr[i]
    dp.append(x)

ans=0
for i in range(n):
    for j in range(i+k-1,n):
        ans=max(ans,((dp[j]-dp[i])+arr[i])/(j-i+1))
print(ans) 