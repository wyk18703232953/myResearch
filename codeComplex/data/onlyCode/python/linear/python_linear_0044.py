n,k=map(int,input().split())
a=list(map(int,input().split()))
q={0}
e=0
l=[]
for i in range(n):
    if a[i] not in q:
        e+=1
        q.add(a[i])
    if e==k:
        e=0
        q={0}
        l+=[i]
w=10**5
t=0
for i in l:
    e=0
    q={0}
    for j in range(i,-1,-1):
        if a[j] not in q:
            e+=1
            q.add(a[j])
        if e==k:
            if w>len(q):
                w=j+1
                t=i+1
            break
if len(set(a))>=k:print(w,t)
else:print(-1,-1)
