
from sys import stdin
input = stdin.buffer.readline

n,m=map(int,input().split())
arr=[int(x) for x in input().split()]

dp=[[] for i in range(m)]
for i in range(n):
    dp[arr[i]%m].append(i)

res=0
k=n//m
ans=arr.copy()
s=[]
for t in range(2):
    for i in range(m):
        if len(dp[i])<k:
            while len(s)!=0 and len(dp[i])<k:
                x=s.pop()
                y=arr[x]%m
                if i>y:
                    ans[x]=ans[x]+(i-y)
                    res=res+(i-y)
                else:
                    ans[x]=ans[x]+(m-1-y)+(i+1)
                    res=res+(m-1-y)+(i+1)    
                dp[i].append("xxx")
        if len(dp[i])>k:
            while len(dp[i])>k:
                s.append(dp[i].pop())   

print(res)
print(*ans)