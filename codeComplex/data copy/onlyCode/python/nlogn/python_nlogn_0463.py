from sys import stdin
input = stdin.buffer.readline
 
n,k=map(int,input().split())
arr=[int(x) for x in input().split()]
 
l=[]
for i in range(n):
    l.append((arr[i],i))
 
l.sort(reverse=True)
 
dp=[]
x=0
for i in range(k):
    dp.append(l[i][1])
    x=x+l[i][0]
 
print(x)
dp.sort()
dp=[-1]+dp
 
l=len(dp)
for i in range(1,l-1):
    print(dp[i]-dp[i-1],end=" ")
print(n-1-dp[l-2])    