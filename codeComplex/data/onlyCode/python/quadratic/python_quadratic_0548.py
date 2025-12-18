n, k = map( int, input().split() )

d = n - k
d = d // 2

l = []

while n > 0:
    i = min(n,d)
    while i>0:
        l.append('1')
        i -= 1
        n -= 1
    if n > 0:
        l.append('0')
        n -= 1

print( "".join( l ) )