import math
a,b=map(int,input().split())
c=[]
e=[]
f=0
for i in range(a):
    d=str(input())
    for j in range(b):
        if d[j]=="B":
            c=c+[i]
            e=e+[j]
p=min(c)
p1=min(e)
p2=max(c)
plus=(max(c)-min(c))//2
p3=p+plus+1
p4=p1+plus+1
print(p3,p4)
