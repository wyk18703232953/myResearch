def raschot(d, e, g, h):
    if d > e:
        return 1
    key = d, g, h
    if key in b:
        return b[key]
    f = 0
    for x in (['0', '1'] if a0[d] == '?' else [a0[d]]):
        if d == e:
            a = [x]
        else:
            a = ['0', '1'] if a0[e] == '?' else [a0[e]]
        for y in a:
            if not ((g and x > y) or (h and x == y == '1')):
                f += raschot(d + 1, e - 1, g and x == y, h and x != y)
    b[key] = f
    return f


n, m = map(int, input().split())
m += 1
a0 = ['?'] * n
for i in range(n):
    a0[i] = '0'
    b = {}
    c = raschot(0, n - 1, True, True)
    if m > c:
        m -= c
        a0[i] = '1'
if a0[0] == '0':
    print(''.join(a0))
else:
    print(-1)
