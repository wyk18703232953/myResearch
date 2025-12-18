import sys
from array import array
from bisect import bisect_right

n, k = map(int, input().split())
a = sorted(map(int, input().split())) + [10**9]
ans = n

for x in a[:-1]:
    if a[bisect_right(a, x)] <= x+k:
        ans -= 1

print(ans)
