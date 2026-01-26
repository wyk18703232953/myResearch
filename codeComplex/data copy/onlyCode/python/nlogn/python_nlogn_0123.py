x,y,z=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
c=0
s=z
t=False
while s<y and c<x:
    c+=1
    s=s+l[x-c]-1
if s<y:
    print(-1)
else:
    print(c)
    
    