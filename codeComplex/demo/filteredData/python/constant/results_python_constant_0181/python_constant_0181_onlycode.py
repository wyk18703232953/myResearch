l,r = [int(x) for x in input().split()]
if l==r or l+1==r:
    print(-1)
elif l%2==0:
    print(l,l+1,l+2)
elif l%2!=0 and r-l+1>3:
    print(l+1,l+2,l+3)
else:
    print(-1)