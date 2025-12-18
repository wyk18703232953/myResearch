a,b,c,n=map(int, input().split())
p=n-(a+b-c)
if c>a or c>b or p<=0:
    print(-1)
    exit()
if p<1:
    print(-1)
else:
    print(p)