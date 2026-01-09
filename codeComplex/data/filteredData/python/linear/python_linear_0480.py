import math, functools, itertools, operator, bisect, fractions, statistics
from collections import deque, defaultdict, OrderedDict, Counter
from fractions import Fraction
from decimal import Decimal
from heapq import heappush, heappop, heapify, _heapify_max, _heappop_max, nsmallest, nlargest

def intersection(l1, r1, l2, r2):
    if l1 > r2 or r1 < l2:
        return [0, 0]

    else:
        return [max(l1, l2), min(r1, r2)]

def core_algorithm(z):
    n = len(z)
    pref = []
    suff = []

    pix, piy = intersection(z[0][0], z[0][1], z[0][0], z[0][1])
    six, siy = intersection(z[-1][0], z[-1][1], z[-1][0], z[-1][1])

    for i in range(n):
        pix, piy = intersection(pix, piy, z[i][0], z[i][1])
        pref.append([pix, piy])

    for i in range(n - 1, -1, -1):
        six, siy = intersection(six, siy, z[i][0], z[i][1])
        suff.append([six, siy])
    suff = suff[::-1]

    if n == 1:
        return 0

    if n == 2:
        return max(suff[1][1] - suff[1][0], pref[0][1] - pref[0][0])

    ans = max(suff[1][1] - suff[1][0], pref[n - 2][1] - pref[n - 2][0])
    for i in range(1, n - 1):
        inter = intersection(pref[i - 1][0], pref[i - 1][1], suff[i + 1][0], suff[i + 1][1])
        ans = max(ans, inter[1] - inter[0])
    return ans

def generate_intervals(n):
    # Deterministic generation of n intervals [l_i, r_i]
    # Ensure l_i <= r_i and values grow with i to scale input size
    intervals = []
    for i in range(n):
        l = i
        r = i + (i % 5) + 1
        intervals.append([l, r])
    return intervals

def main(n):
    if n <= 0:
        # print(0)
        pass
        return
    z = generate_intervals(n)
    ans = core_algorithm(z)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)