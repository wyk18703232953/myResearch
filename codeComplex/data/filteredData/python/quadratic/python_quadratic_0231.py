import math
import functools
import itertools
import operator
import bisect
import fractions
import statistics
from collections import deque, defaultdict, OrderedDict, Counter
from fractions import Fraction
from decimal import Decimal
from heapq import heappush, heappop, heapify, _heapify_max, _heappop_max, nsmallest, nlargest

INF = 99999999999999999999999999999999


def main(n):
    if n <= 0:
        print(-1)
        return
    mod = 1000000007

    tc = 1
    for _ in range(tc):
        size = n
        s = [i % (n + 3) for i in range(size)]
        c = [(i * 2 + 3) % (n + 7) + 1 for i in range(size)]

        ans = INF
        for i in range(size):
            mid = s[i]
            mcl = INF
            mrl = INF
            for j in range(i - 1, -1, -1):
                if s[j] < mid:
                    if c[j] < mcl:
                        mcl = c[j]
            for j in range(i + 1, size):
                if s[j] > mid:
                    if c[j] < mrl:
                        mrl = c[j]
            cur = c[i] + mcl + mrl
            if cur < ans:
                ans = cur
        if ans == INF:
            print(-1)
        else:
            print(ans)


if __name__ == "__main__":
    main(10)