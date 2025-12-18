a, b, c, n = map(int, input().split())
t = a + b - c
if a >= n or b >= n or c > a or c > b or t >= n:
    print(-1)
else:
    print(n - t)
