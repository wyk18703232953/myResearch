a, b, c, n = map(int, input().split())
t = a+b-c
if c > a or c > b:
    print(-1)
    exit()
if n-t >= 1:
    print(n-t)
else:
    print(-1)
