def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

# B. Minimum Diameter Tree

from collections import Counter

n, s = mi()
d = Counter()
for i in range(n - 1):
    u, v = mi()
    d[u] += 1
    d[v] += 1

l = sum(v == 1 for v in d.values())
ans = s / l * 2
print('%.10f' % (ans,))
