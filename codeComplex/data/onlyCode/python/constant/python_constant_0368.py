a, b, c, n = [int(j) for j in input().split()]
a -= c
b -= c
if n - a - b - c >= 1 and a >= 0 and b >= 0:
    print(n - a - b - c)
else:
    print(-1)
