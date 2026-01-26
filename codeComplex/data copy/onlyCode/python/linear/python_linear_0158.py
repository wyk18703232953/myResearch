from collections import defaultdict
from sys import stdin

input = stdin.readline

dct = defaultdict(int)
n = int(input())
lst = [0] * n
for i in range(n):
    t = input().strip()
    a, b, c = map(int, (t[1:t.index('+')], t[t.index('+') + 1:t.index(')')], t[t.index('/') + 1:]))
    x = (a + b) / c
    lst[i] = x
    dct[x] += 1
for i in lst:
    print(dct[i], end=' ')
