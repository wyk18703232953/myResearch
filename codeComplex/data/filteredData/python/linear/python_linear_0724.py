import sys
import collections
import math
import heapq
import bisect
from operator import itemgetter

def main(n):
    # Interpret n as total number of elements; split between b and g
    if n < 2:
        n = 2
    m = n // 2
    if m == 0:
        m = 1
    # Ensure at least 2 boys to have bMax2 well-defined
    if m == 1:
        m = 2
    n = m + (n - m)

    # Generate b and g deterministically
    # b: increasing sequence with some variation
    b = [(i * 3 + 1) % (n + 5) + 1 for i in range(m)]
    # Ensure there are at least two distinct maximums possibility
    if len(b) >= 2 and b[0] == b[1]:
        b[1] += 1

    # g: values shifted from b to guarantee comparable scale
    g_len = n - m
    if g_len <= 0:
        g_len = 1
    g = [((i * 5 + 2) % (n + 7)) + 1 for i in range(g_len)]

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
        result = bSum * g_len
        result += gSum
        result -= bMax * g_len
        if gMin > bMax:
            result += bMax - bMax2

    # print(str(result))
    pass
if __name__ == "__main__":
    main(10000)