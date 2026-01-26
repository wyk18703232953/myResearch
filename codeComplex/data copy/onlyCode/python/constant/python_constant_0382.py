a,b,c,n = map(int,input().split())
a-=c
b-=c
if a>=0 and b>=0:
    if (a+b+c)<n:
        n-=(a+b+c)
        print(n)
    else:
        print(-1)
else:
    print(-1)