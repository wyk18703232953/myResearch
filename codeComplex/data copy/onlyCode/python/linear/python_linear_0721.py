n, m = map(int, input().split())
a = []
b = []
ma = 0
macount = 0
mi = 1000000000000000000000000000
su = 0
for el in map(int, input().split()):
    if el > ma:
        ma = el
        macount = 1
    elif el == ma:
        macount += 1
    a.append(el)
for el in map(int, input().split()):
    mi = min(el, mi)
    b.append(el)
    su += el
if ma > mi:
    print(-1)
elif ma == mi or macount > 1:
    f = True
    for i in range(n):
        if a[i] == ma and f:
            f = False
        else:
            su += a[i] * m
    print(su)
else:
    secmax = 0
    for el in a:
        if el > secmax and el < ma:
            secmax = el
    f = True
    for i in range(n):
        if a[i] == ma and f:
            f = False
        else:
            su += a[i] * m
    print(su + ma - secmax)
