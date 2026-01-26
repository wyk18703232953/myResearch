n=int(input())
d={}
for _ in range(n):
    a,x=map(int,input().split())
    if a in d:
        d[a][0]+=1
        d[a][1].append(x)
    else:
        d[a]=[1,[x]]
 
 
m=int(input())
for _ in range(m):
    a,x=map(int,input().split())
    if a in d:
        d[a][0]+=1
        d[a][1].append(x)
    else:
        d[a]=[1,[x]]
 
s=0
for x in d:
    if d[x][0]==1:
        s+=d[x][1][0]
    else:
        s+=max(d[x][1])
print(s)