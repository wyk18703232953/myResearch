l,r=list(map(int,input().split()))
if l==r:
    print(0)
else:
    x=l^r
    c=0
    while x>0:
        x=x//2
        c=c+1
    print(2**c-1)