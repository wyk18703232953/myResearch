n,s=int(input()),input()
p,q,r=len(set(s)),{},10**6
for i in range(n):
    q[s[i]]=i
    if len(q)==p:r=min(r,max(q.values())-min(q.values()))
print(r+1)