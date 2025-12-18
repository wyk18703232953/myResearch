from math import gcd

n = int(input())
d = dict()
qs = []
for i in range(n):
    s = input()
    a = int(s[1:s.index('+')])
    b = int(s[s.index('+') + 1: s.index(')')])
    c = int(s[s.index(')') + 2:])
    a = a + b
    gc = gcd(a, c)
    res = (a // gc, c // gc)
    qs.append(res)
    if res in d:
        d[res] += 1
    else:
        d[res] = 1
for q in qs:
    print(d[q], end=' ')
