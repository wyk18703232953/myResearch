import math as mt
import sys
input=sys.stdin.readline
I=lambda:list(map(int,input().split()))
n,m=I()
a=[I() for i in range(n)]
ans=[]
lo=0
hi=10**9
def vanguda(mid: int) -> bool:
    global ans
    f={}
    for i in range(n):
        bi=0
        for j in range(m):
            if a[i][j]>=mid:
                bi+=1
            bi<<=1
        f[bi>>1]=i
    for aa,bb in f.items():
        for cc,dd in f.items():
            if aa|cc==(2**m-1):
                ans =bb+1,dd+1
                return True
    return False

while lo<=hi:
	mid=(lo+hi)//2
	if vanguda(mid):
		lo=mid+1
	else:
		hi=mid-1
print(*ans)


