#573_C

import math

ln = [int(i) for i in input().split(" ")]

n = ln[0]
m = ln[1]
k = ln[2]

p = [int(i) for i in input().split(" ")]

i = 0
ct = 0
ops = 0
while i < len(p):
    nm = p[i] - ct
    if nm % k == 0:
        mnm = nm
    else:
        mnm = (nm // k) * k + k
    si = i
    while p[i] - ct <= mnm:
        i += 1
        if i >= len(p):
            break
    ct += i - si
    ops += 1
    if i >= len(p):
        break
print(ops)
