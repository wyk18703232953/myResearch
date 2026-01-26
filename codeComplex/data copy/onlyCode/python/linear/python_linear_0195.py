n,a,b,c,t=map(int,input().split())
l=list(map(int,input().split()))
if c>b:
    r=0
    for i in l:
        k=t-i
        k*=(c-b)
        r+=k
    print(a*n+r)
else:
    print(a*n)
