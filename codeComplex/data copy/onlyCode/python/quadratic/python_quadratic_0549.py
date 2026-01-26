n, e = map( int, input().split() )
d = (n - e) // 2
q = []
while n > 0:
    i = min(n, d)
    while i > 0:
        q.append('1')
        i -= 1
        n -= 1
    if n > 0:
        q.append('0')
        n -= 1

print( "".join(q) )