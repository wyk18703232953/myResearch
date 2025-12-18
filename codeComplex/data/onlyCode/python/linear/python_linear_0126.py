def if_spruce(n,l,m):
    d=[0]*(n+1)
    for i in range(1,n+1):
        if m[i]==0:
            d[l[i]]+=1
    for i in range(1,n+1):
        if m[i]>0 and d[i]<3:
            return "No"
    return "Yes"

n=int(input())
l,m,a=[0]*2,[0]*(n+1),0
for _ in range(n-1):
    a=int(input())
    l.append(a)
    m[a]+=1
print(if_spruce(n,l,m))