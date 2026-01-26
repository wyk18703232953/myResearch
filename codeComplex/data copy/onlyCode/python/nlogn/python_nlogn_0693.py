n, m = map(int, input().split())
b = list(map(int, input().split()))
g = list(map(int, input().split()))

if max(b) > min(g):
    print(-1)
else:
    total = m*sum(b)
    b.sort()
    g.sort()
    while len(g) > 0:
        current = 0
        count = 1
        if len(b) > 0:
            current = b.pop()
        while len(g) > 0 and g[-1] > current and count < m:
            total += g[-1] - current
            g.pop()
            count += 1
        while len(g) > 0 and g[-1] == current:
            g.pop()
    print(total)
