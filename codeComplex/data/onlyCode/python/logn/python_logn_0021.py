l,r=map(int,input().split())
al=[]
ar=[]
while(r):
    p=r%2
    ar.append(p)
    r=r//2
while(l):
    p=l%2
    al.append(p)
    l=l//2
if len(ar)!=len(al):
    ans=(2**len(ar))-1
else:
    n=len(ar)
    s=0
    k=0
    for i in range(n-1,-1,-1):
        if ar[i]!=al[i]:
            k=i+1
            break
    ans=(2**k)-1
    if k==0:
        ans=0
print(ans)