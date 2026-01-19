from math import *


def nCr(n, r):
    f = factorial
    return f(n) / f(r) / f(n - r)


s1, s2 = [input() for i in range(2)]
s1_pos, s2_pos, s1_neg, s2_neg, s1_q = s1.count('+'), s2.count('+'), s1.count('-'), s2.count('-'), s2.count('?')
# print(s1_pos, s2_pos, s1_neg, s2_neg, s1_q)

ans = 0
if s1_q == 0:
    if s1_pos == s2_pos:
        ans = 1
    else:
        ans = 0
else:
    diff1 = s1_pos - s2_pos
    if diff1 > s1_q or diff1 < 0:
        ans = 0
    else:
        ans = nCr(s1_q, diff1) / 2 ** s1_q

print('{:.12f}'.format(ans))
