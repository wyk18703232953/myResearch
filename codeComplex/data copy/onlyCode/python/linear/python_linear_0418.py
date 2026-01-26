n,x=list(map(int,input().split()))
b=list(map(int,input().split()))
d={}
flag=0
for i in b:
    if d.get(i):
        flag=1
        break
    else:
        d[i]=1
if flag:
    print(0)
else:
    flag=0
    c=set()
    for i in b:
        a=i&x
        c.add(a)
        if d.get(a) and a!=i:
            flag=1
            break
    if flag:
        print(1)
    elif len(c)<n and flag==0:
        print(2)
    else:
        print(-1)

        
        
