import sys
if locals()['__file__'][-2:] == 'py':
    sys.stdin = open('in.txt', 'r')
from sys import stdin
rl = lambda l: tuple(map(int, l.split()))
n, a, b = rl(input())
l = list(map(rl, stdin.readlines()))
c, d = {}, {}
r = 0
for _, x, y in l:
    i, j = a * x - y, (x, y)
    r += c.get(i, 0) - d.get(j, 0)
    c[i] = c.get(i, 0) + 1
    d[j] = d.get(j, 0) + 1
print(2 * r)
