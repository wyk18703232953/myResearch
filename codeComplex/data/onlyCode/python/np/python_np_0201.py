n,l,r,d=[int(i) for i in input().split()]
op=[int(i) for i in input().split()]
c=0
for i in range(2,2**n):
    s=0
    k=0
    maxx=0
    minn=1000001
    x=bin(i)[2:]
    x='0'*(n-len(x))+x
    for j in range(n):
        if x[j]=='1':
            s+=op[j]
            k+=1
            if maxx<op[j]:
                maxx=op[j]
            if op[j]<minn:
                minn=op[j]
    if l<=s<=r and maxx-minn>=d and k>=2:
        c+=1
print(c)