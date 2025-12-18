n,v = map(int,input().split())

if n <= v + 1:
    print( n - 1 )
else:
    b = n - v
    print( v - 1 + ((b*(b+1))//2))
