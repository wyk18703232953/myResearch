a,b,c,n=map(int,input().split())
if n-a-b+c>=1:
    if a<c or b<c:
        print(-1)
    else:
        print(n-a-b+c)
else:
    print(-1)