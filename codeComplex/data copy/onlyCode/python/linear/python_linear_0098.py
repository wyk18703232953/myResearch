def bs(l, h):
    while l < h:
        m = (l + h) // 2
        if gf(m):
            h = m
        else:
            l = m + 1
    return l

def gf(x):
    d = {}
    for i in range(x):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    if len(d) == len(u):
        return 1
    for i in range(x, n):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
        d[s[i - x]] -= 1
        if not d[s[i - x]]:
            del d[s[i - x]]
        if len(d) == len(u):
            return 1
    return 0

n = int(input())
s = input()
u = set([*s])
print(bs(1, n))