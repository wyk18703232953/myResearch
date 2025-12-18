a,b,c,n = map(int,input().split())
if c > a or c > b or (a+b) - c >=n:
    print(-1)
else:
    print(n -((a+b)-c))