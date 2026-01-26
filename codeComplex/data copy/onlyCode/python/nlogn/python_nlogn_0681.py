n, m = map( int, input().split() )
b = list(map(int, input().split()))
g = list(map(int, input().split()))
b.sort()
g.sort()
if b[-1] > g[ 0 ]:
    print( -1 )
else:
    ans = sum(b)*m
    if g[ 0 ] != b[ -1 ]:
        ans += g[ 0 ] - b[ -2 ]
    for i in range( 1, m):
        ans += g[ i ] - b[ -1 ]
    print( ans )