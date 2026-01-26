from sys import stdin,stdout
for _ in range(1):#int(stdin.readline())):
    # n=int(stdin.readline())
    moves,left=list(map(int,stdin.readline().split()))
    # ATE=?
    l=1;r=10**9+1
    while l<=r:
        mid=(l+r)>>1
        fx=(mid*(mid+1))//2-left+mid
        # print(l,r,mid)
        if fx<=moves:l=mid+1
        else:r=mid-1
    print(moves-r)