from __future__ import division
from sys import stdin

rints = lambda: [int(x) for x in stdin.readline().split()]
n, m = rints()
a, cur, ans = rints()[::-1], 2, -1

for i in range(n - 2):
    cur = max(cur, i + 2)
    for j in range(cur, n):
        if a[i] - a[j] > m:
            break

        cur += 1
        v = (a[i] - a[j - 1]) / (a[i] - a[j])
        ans = max(ans, v)

print(ans)
