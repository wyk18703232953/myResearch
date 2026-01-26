import bisect
n,q=map(int,input().split())
strength=list(map(int,input().split()))
arrows=list(map(int,input().split()))
for i in range(1,n):
    strength[i]+=strength[i-1]
No_arrows=0
n-=1
for i in range(q):
    No_arrows+=arrows[i]
    if(No_arrows>=strength[-1]):
        No_arrows=0
        print(n+1)
    else:
        it=bisect.bisect_left(strength,No_arrows)
        if(strength[it]==No_arrows):
            print(n-it)
        else:
            print(n-it+1)
