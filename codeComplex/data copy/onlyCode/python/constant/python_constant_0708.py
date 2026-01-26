n, v = map(int, input().split())
if n - 1 > v:
    print(v + (n - v + 2) * (n - v - 1) // 2)
else:
    print(n - 1)