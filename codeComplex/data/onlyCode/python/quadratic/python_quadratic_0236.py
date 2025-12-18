n=int(input())
s=list(map(int,input().split()))
c=list(map(int,input().split()))
dp=[float('inf')]*(n)
for i in range(1,n):
    mn=float('inf')
    for j in range(i):
        if s[i]>s[j]:
            mn=min(mn,c[i]+c[j])
    dp[i]=mn
res=float('inf')
for i in range(1,n):
    for j in range(i):
        if s[i]>s[j]:
            res=min(res,c[i]+dp[j])
if res==float('inf'):
    res=-1
print(res)
            
    
    