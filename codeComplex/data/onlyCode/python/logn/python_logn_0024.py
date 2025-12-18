l,r=map(int,input().split())
r1=len(bin(r))-3
l1=len(bin(l))-3
ans=0
while(l>0):
    if l1==r1:
        r-=(1<<l1)
        l-=(1<<l1)
    else:
        ans=(1<<(r1+1))-1
        break


    z1=min(l,r)
    z2=max(l,r)
    l,r=z1,z2
    r1 = len(bin(r)) - 3
    l1 = len(bin(l)) - 3


if ans==0:
    if l1==r1:
        if r==1:
            print(1)
        else:
            print(0)
    else:
        print((1<<(r1+1))-1)

else:
    print(ans)



