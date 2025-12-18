n=int(input())
g={}
for i in range(1,n):
    p=int(input())
    if g.get(p):g[p].append(i+1)
    else:g[p]=[i+1]
ams='YES'
for i in g:
    c=0
    for j in g[i]:
        if j not in g:c+=1 
    if c<3:ams='NO'
print(ams)