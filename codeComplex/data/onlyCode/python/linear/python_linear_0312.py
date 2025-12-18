n,m=map(int, input().split())
a=list(map(int, input().split()))
t=n//m
remain=[[] for i in range(m)]
for i in range(n):
    x=a[i]%m
    remain[x].append(i)
ans=0
f=[]
for i in range(2*m):
    cur=i%m
    while len(remain[cur])>t:
        elm=remain[cur].pop()
        f.append([elm,i])
    while len(remain[cur])<t and len(f)!=0:
        elm,j=f.pop()
        remain[cur].append(elm)
        a[elm]+=abs(i-j)
        ans+=abs(i-j)
print(ans)
print(*a)
