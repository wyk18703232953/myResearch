a, b, c, n= map(int, input().split())
p = a + b - c
if p <= n-1 and a - c >= 0 and b - c >= 0:
    print(n - p)
else :
    print(-1)
