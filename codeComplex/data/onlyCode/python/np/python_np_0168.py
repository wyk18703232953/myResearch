n,l,r,x=map(int,input().split())
a=list(map(int,input().split()))
count=0
t=0
ans=[]
for i in range(3,(2**n)+1):
    c=i
    ans=[]
    sum=0
    while c!=0:
        c=c&(c-1)
        count+=1
    if count>1:
        for j in range(n):
            if i & (1 << j):
                sum+=a[j]
                ans.append(a[j])
        if l<=sum<=r and (max(ans)-min(ans))>=x:
            t+=1
print(t)
