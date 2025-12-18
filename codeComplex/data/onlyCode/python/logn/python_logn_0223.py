def case(mid):
    res=0
    for k,x in enumerate(str(mid)):
        res+=int(x)
    return res
n,s=map(int,input().split())
i,j=0,n
while i+1<j:
    mid=(i+j)//2
    result=case(mid)
    if mid-case(mid)<s:i=mid
    else:j=mid
if i-case(i)>=s:print(n-i+1)
else:
    if j==n:
        if j-case(j)>=s:print(1)
        else:print(0)
    else:print(n-j+1)