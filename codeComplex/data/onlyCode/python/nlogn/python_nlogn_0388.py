a=input()
b=input()
c=input()
info=a.split()
info=list(map(int, info))
y=b.split()
powers=list(map(int, y))
z=c.split()
coins=list(map(int, z))
l=sorted(zip(powers,coins,range(info[0])))
final=[0]*info[0]
s=0
w=[]
for _, c, i in l:
    s+=c
    final[i]=s
    w=sorted(w+[c])
    if len(w)>info[1]:
        s-=w[0]
        del w[0]
print(*final)