x, y, z, t1, t2, t3 = map(int, raw_input().split())
elev = t3*3 + t2*(abs(z-x) + abs(x-y))
stairs = t1*abs(x - y)
if elev <= stairs:
    print('YES')
else:
    print('NO')
