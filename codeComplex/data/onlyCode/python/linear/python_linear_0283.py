import sys
import io, os
input = sys.stdin.readline

n = int(input())
S = [str(input().rstrip()) for i in range(n)]
from collections import defaultdict
d1 = defaultdict(lambda: 0)
d2 = defaultdict(lambda: 0)
ans = 0
for i, s in enumerate(S):
    cum1 = 0
    flag1 = True
    for c in s:
        if c == '(':
            cum1 += 1
        else:
            cum1 -= 1
        if cum1 < 0:
            flag1 = False
    if flag1:
        ans += d2[cum1]
    cum2 = 0
    flag2 = True
    for i in reversed(range(len(s))):
        c = s[i]
        if c == ')':
            cum2 += 1
        else:
            cum2 -= 1
        if cum2 < 0:
            flag2 = False
    if flag2:
        ans += d1[cum2]
    if cum1 == 0 and cum2 == 0 and flag1 and flag2:
        ans += 1
    if flag1:
        d1[cum1] += 1
    if flag2:
        d2[cum2] += 1

print(ans)
