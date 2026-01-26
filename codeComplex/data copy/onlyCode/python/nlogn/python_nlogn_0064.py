def sum(l):
    s=0
    for i in range(len(l)):
        s+=l[i]
    return s
 
n=int(input())
cns=list(map(int,input().split()))
xs,nm,c=0,0,0
cns.append(0)
while(xs<=nm):
    m=max(cns)
    cns.remove(m)
    xs+=m
    nm=sum(cns)
    c+=1
print(c)
    