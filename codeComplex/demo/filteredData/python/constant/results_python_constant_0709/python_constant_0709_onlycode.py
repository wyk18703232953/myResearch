n,v=[int(x) for x in input().split()]
if v>=(n-1):
    print(n-1)
else:
    print(int((((n-v)*(n-v+1))/2)-1+v))
    
    