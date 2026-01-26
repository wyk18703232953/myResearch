n,m,a,b = map(int,input().split())
if n%m!=0:
    mn = n//m * m
    mx = n//m * m + m
    print(min(((n - mn) * b),((mx - n) * a)))
else:print(0) 