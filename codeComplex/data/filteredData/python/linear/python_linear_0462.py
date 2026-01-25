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


def generate_s(n):
    if n <= 0:
        return ""
    base = ['b', 'w']
    s_chars = [base[i % 2] for i in range(n)]
    return ''.join(s_chars)


def core_algorithm(s):
    s = 2 * s + "333"
    le = (len(s) - 3) // 2
    a = []
    for ch in s:
        if ch == 'b':
            a.append(0)
        if ch == 'w':
            a.append(1)
        if ch == '3':
            a.append(3)

    pehla = [0, 1] * len(s)
    doosra = [1, 0] * len(s)

    k = [0] * len(s)
    for i in range(len(s)):
        if a[i] == pehla[i]:
            k[i] = 1

    ans = 0
    t = 0
    for v in k:
        if v == 1:
            t += 1
        else:
            ans = max(ans, t)
            t = 0

    k = [0] * len(s)
    for i in range(len(s)):
        if a[i] == doosra[i]:
            k[i] = 1

    t = 0
    for v in k:
        if v == 1:
            t += 1
        else:
            ans = max(ans, t)
            t = 0

    return min(le, ans)


def main(n):
    s = generate_s(n)
    result = core_algorithm(s)
    print(result)


if __name__ == "__main__":
    main(10)