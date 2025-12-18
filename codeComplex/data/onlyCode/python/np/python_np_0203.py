import sys
def fastio():
    from io import StringIO
    from atexit import register
    global input
    sys.stdin = StringIO(sys.stdin.read())
    input = lambda : sys.stdin.readline().rstrip('\r\n')
    sys.stdout = StringIO()
    register(lambda : sys.__stdout__.write(sys.stdout.getvalue()))
fastio()

def debug(*var, sep = ' ', end = '\n'):
    print(*var, file=sys.stderr, end = end, sep = sep)

INF = 10**20
MOD = 10**9 + 7
I = lambda:list(map(int,input().split()))
from math import gcd
from math import ceil
from collections import defaultdict as dd, Counter
from bisect import bisect_left as bl, bisect_right as br

n, l, r, x = I()
a = I()
ans = 0
for i in range(1, 2 ** n):
    if i & (i - 1) == 0:
        continue
    mn, mx, total = INF, -INF, 0
    for j in range(n):
        if (i >> j) & 1:
            mn = min(mn, a[j])
            mx = max(mx, a[j])
            total += a[j]
    if l <= total <= r and mx - mn >= x:
        ans += 1
print(ans)