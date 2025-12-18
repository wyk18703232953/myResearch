n, s = map( int, input().split() )

ans = 0
while s > 0:
    a = s // n
    s -= n * a
    ans += a
    n -= 1

print( ans )
