import sys
import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

n, m = map(int, input().split())

MAX = 0
MIN = 10**18
for i in range(n):
    l = i*(i+1)//2
    r = (n-1-i)*(n-1-i+1)//2
    MAX= max(MAX, l+r)
    MIN = min(MIN, l+r)

ans = 0
for i in range(m):
    x, d = map(int, input().split())
    ans += n*x
    if d  >= 0:
        ans += d*MAX
    else:
        ans += d*MIN
print(ans/n)
