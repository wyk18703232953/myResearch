import math
from collections import deque, defaultdict, OrderedDict, Counter
from fractions import Fraction
from decimal import Decimal
from heapq import heappush, heappop, heapify, _heapify_max, _heappop_max, nsmallest, nlargest

INF = 99999999999999999999999999999999

def main(n):
    # n: input size (length of arrays s and c)
    if n <= 0:
        # print(-1)
        pass
        return

    # Deterministic data generation
    # s: some varying sequence
    # c: cost sequence
    s = [(i * 3 + 1) % (n + 7) for i in range(n)]
    c = [(i * 5 + 2) % (n + 11) + 1 for i in range(n)]

    ans = INF
    for i in range(n):
        mid = s[i]
        mcl = INF
        mrl = INF
        for j in range(i - 1, -1, -1):
            if s[j] < mid:
                if c[j] < mcl:
                    mcl = c[j]
        for j in range(i + 1, n):
            if s[j] > mid:
                if c[j] < mrl:
                    mrl = c[j]
        cur = c[i] + mcl + mrl
        if cur < ans:
            ans = cur

    if ans == INF:
        # print(-1)
        pass

    else:
        # print(ans)
        pass
if __name__ == "__main__":
    # Example deterministic call for timing/experiments
    main(1000)