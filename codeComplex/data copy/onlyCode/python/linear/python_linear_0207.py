from __future__ import division
from sys import stdin, stdout
from collections import *

rstr = lambda: stdin.readline().strip()
rstrs = lambda: [str(x) for x in stdin.readline().split()]
rstr_2d = lambda n: [rstr() for _ in range(n)]
rint = lambda: int(stdin.readline())
rints = lambda: [int(x) for x in stdin.readline().split()]
rint_2d = lambda n: [rint() for _ in range(n)]
rints_2d = lambda n: [rints() for _ in range(n)]
pr = lambda args, sep: stdout.write(sep.join(map(str, args)) + '\n')
ceil1, out = lambda a, b: (a + b - 1) // b, []

n, s = rints()
a, ans = rints_2d(n), -1

for i in range(26):
    for j in range(60):
        tem = i * 60 + j
        ans = (i, j)
        for h, m in a:
            tem2 = h * 60 + m
            if tem <= tem2:
                if tem2 - (tem + 1) < s:
                    ans = -1
                    break
            else:
                if tem - (tem2 + 1) < s:
                    ans = -1
                    break

        if ans != -1:
            print('%d %d' % (ans[0], ans[1]))
            exit()
