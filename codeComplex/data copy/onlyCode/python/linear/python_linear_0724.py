import sys
import collections
import math
import heapq
import bisect
from operator import itemgetter

def getint():
    return int(input())

def getints():
    return [int(x) for x in input().split(' ')]

n, m = getints()
b = getints()
g = getints()

result = 0

bMax, bMax2, bSum = -1, -1, 0
for i, bb in enumerate(b):
    bSum += bb
    if bb > bMax:
        bMax2, bMax = bMax, bb
    elif bb > bMax2:
        bMax2 = bb

gMin, gSum = float('inf'), 0
for j, gg in enumerate(g):
    gSum += gg
    if gg < gMin:
        gMin = gg

if bMax > gMin:
    result = -1
else:
    result = bSum * m
    result += gSum
    result -= bMax * m
    if gMin > bMax:
        result += bMax - bMax2

print(str(result))