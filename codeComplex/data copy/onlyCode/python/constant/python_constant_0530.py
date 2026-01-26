x, y, z, t1, t2, t3, = map(int, input().split())
if abs(x-z)*t2 + abs((x-y))*t2 + t3*3 <= t1*abs((x-y)):
    print("YES")
else:
    print("NO")