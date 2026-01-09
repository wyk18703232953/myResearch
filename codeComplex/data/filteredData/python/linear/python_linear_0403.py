import math
import heapq
import bisect
from collections import Counter, defaultdict
from io import BytesIO, IOBase
import string


def prefix_sums(a):
    p = [0]
    for x in a:
        p.append(p[-1] + x)
    return p


def binary_search(good, left, right, delta=1, right_true=False):
    limits = [left, right]
    while limits[1] - limits[0] > delta:
        if delta == 1:
            mid = sum(limits) // 2

        else:
            mid = sum(limits) / 2
        if good(mid):
            limits[int(right_true)] = mid

        else:
            limits[int(~right_true)] = mid
    if good(limits[int(right_true)]):
        return limits[int(right_true)]

    else:
        return False


def solve_a(n, m, a, b):
    def good(k):
        for i in range(n):
            k -= (m + k) / a[i]
            k -= (m + k) / b[i]
        return k >= 0

    ans = binary_search(good, 0, 10 ** 9 + 1, delta=10 ** (-6), right_true=True)
    if not ans:
        return -1

    else:
        return ans


def main(n):
    m = n * 10
    a = [i % 7 + 2 for i in range(1, n + 1)]
    b = [i % 5 + 3 for i in range(1, n + 1)]
    result = solve_a(n, m, a, b)
    # print(result)
    pass
if __name__ == "__main__":
    main(5)