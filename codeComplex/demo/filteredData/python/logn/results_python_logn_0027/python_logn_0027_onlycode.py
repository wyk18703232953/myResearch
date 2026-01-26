vals=list(map(int,input().split()))
l=vals[0]
r=vals[1]

if l==r:
    print("0")
else:
    i=0
    j=0
    while l>0 or r>0:
        i+=1
        if (l&1)^(r&1)==1:
            j=i
        l=l>>1
        r=r>>1
    ans=1
    for i in range(0,j):
        ans=ans*2
    ans-=1
    print(ans)