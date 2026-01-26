import sys, os, io
from math import log, gcd, ceil
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import math

def main(n):
    # generate deterministic intervals: n pairs (x, y) with x <= y
    # example: x = i, y = 2*i for i in 1..n
    intervals = [(i, 2 * i) for i in range(1, n + 1)]

    d = defaultdict(lambda: 0)
    d1 = defaultdict(lambda: 0)

    for x, y in intervals:
        d[x - 1] -= 1
        d[y] += 1

    xkeys = list(d.keys())
    xkeys.sort()
    if not xkeys:
        # print(" ".join("0" for _ in range(n)))
        pass
        return

    r = xkeys[-1]
    c = d[r]
    temp = 1
    for i in range(len(xkeys) - 2, -1, -1):
        l = xkeys[i] + 1
        d1[c] += r - l + temp
        c += d[xkeys[i]]
        r = l
        temp = 0

    output = []
    for i in range(1, n + 1):
        output.append(str(d1[i]))
    # print(" ".join(output))
    pass
if __name__ == "__main__":
    # example deterministic call; adjust n as needed for experiments
    main(10)