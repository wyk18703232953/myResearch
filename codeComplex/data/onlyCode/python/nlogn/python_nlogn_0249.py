from bisect import bisect_right

n,q=map(int,input().split())
a=[int(X) for X in input().split()]
k=[int(x) for x in input().split()]
for i in range(1,n):
    a[i]+=a[i-1]
an=0
for j in k:
    j+=an
    x=bisect_right(a,j)
    if x==n:
        print(n)
        an=0
    else:

        print(n-x)
        an=j

