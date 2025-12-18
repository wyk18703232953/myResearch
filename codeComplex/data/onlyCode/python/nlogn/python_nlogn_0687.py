n, m = map(int, input().split())
b = list(map(int, input().split()))
g = list(map(int, input().split()))
b.sort()
g.sort()
if b[-1] > g[0]:
    print(-1)
    import sys
    sys.exit(0)
a = 0
a += sum(g) - g[0]
if g[0] == b[-1]:
    a += g[0]
    a += m * sum(b[:-1])
    print(a)
else:
    a += g[0]
    a += m * sum(b[:-2]) + (m - 1) * b[-2] + b[-1]
    print(a)
