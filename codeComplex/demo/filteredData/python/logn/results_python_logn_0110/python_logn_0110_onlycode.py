import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
l,r=list(map(int,input().split()))
if l==r:
    print(0)
else:
    a=bin(l)[2:]
    b=bin(r)[2:]
    x=len(a)
    y=len(b)
    if x!=y:
        ans=0
        for i in range(y):
            ans+=(2**i)
        print(ans)
    else:
        for i in range(x):
            if a[i]!=b[i]:
                ind=i
                break
        l=x-ind
        ans=0
        for i in range(l):
            ans+=(2**i)
        print(ans)
                
                