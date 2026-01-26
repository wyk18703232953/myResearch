n,k=map(int,input().split())
l=list(map(int,input().split()))
p=[]
a=sorted(l)
for i in a:
    if(i%k==0):
        if(i//k in p):
            pass
        else:
            p.append(i)
    else:
        p.append(i)
print(len(set(p)))
