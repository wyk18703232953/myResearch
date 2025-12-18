n=int(input())
l=list(map(int,input().split()))
ans=0
m=[]
for i in range(2*n-1,-1,-1):
    if l[i] not in m:
        m.append(l[i])

for tt in range(0,n):
    i=m[tt]
    j=l.index(i)
    l.pop(j)
    k=l.index(i)
    l.insert(k,j)
    ans+=k-j
print(ans)
