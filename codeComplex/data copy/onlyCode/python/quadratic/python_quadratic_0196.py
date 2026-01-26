from sys import stdin
from operator import xor

rints = lambda: [int(x) for x in stdin.readline().split()]
n, a, m = int(input()), [rints()], int(input())
qur, out = [rints() for _ in range(m)], []

for i in range(1, n):
    a.append(map(xor, a[-1][:-1], a[-1][1:]))

for i in range(n - 1):
    a[i + 1] = map(max, a[i][:-1], a[i][1:], a[i + 1])

for l, r in qur:
    out.append(a[r - l][l - 1])

print('\n'.join(map(str, out)))
