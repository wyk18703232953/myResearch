n,l,r,x = map(int,input().split())
c = list(map(int,input().split()))
c.sort()
ans = 0
for i  in range(2**n):
    s = []
    for j in range(n):
        if i&2**j:
            s.append(c[j])
    if sum(s)>=l and sum(s)<=r and max(s)-min(s)>=x:
        ans+=1

print(ans)        
        