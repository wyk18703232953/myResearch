n,x=map(int,input().split())
a=[]
k={}
for _ in range(n):
    p,q=map(int,input().split())
    if p not in k:
        k[p]=1
    a.append([p,q])
a.sort()
k=sorted(k)
p=[]
k=k[::-1]
for i in k:
    for j in a:
        if j[0]==i:
            p.append(j)
print(p.count(p[x-1]))