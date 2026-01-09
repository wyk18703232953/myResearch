from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush, heappop, heapify
import math
from collections import *
from functools import reduce, cmp_to_key
from itertools import accumulate
from functools import lru_cache

M = mod = 998244353


def factors(n):
    return sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))


def inv_mod(n):
    return pow(n, mod - 2, mod)


def makenum(s):
    return int(''.join(str(e) for e in s))


def givemax(a, b):
    if len(a) > len(b):
        return a
    elif len(b) > len(a):
        return b

    else:
        for j in range(len(a)):
            if a[j] > b[j]:
                return a
            elif b[j] > a[j]:
                return b
        return a


def solve(a, b):
    n = len(str(a))
    a_list = [int(i) for i in str(a)]
    a_list.sort()
    if len(str(b)) > n:
        return ''.join(str(x) for x in sorted(a_list, reverse=1))

    b_list = [int(i) for i in str(b)]

    @lru_cache(None)
    def dp(l, equal=1):
        if len(l) == 1:
            return str(-float('inf')) if l[0] > b_list[-1] and equal else str(l[0])
        if not equal:
            return ''.join(str(e) for e in sorted(l, reverse=1))
        ans = ''
        l_list = list(l)
        curr = b_list[n - len(l_list)]
        for i in range(len(l_list)):
            remaining = tuple(l_list[:i] + l_list[i + 1:])
            if l_list[i] < curr and dp(remaining, 0) != '-inf':
                ans = givemax(ans, str(l_list[i]) + dp(remaining, 0))
            elif l_list[i] == curr and dp(remaining, 1) != '-inf':
                ans = givemax(ans, str(l_list[i]) + dp(remaining, 1))
        return str(ans)

    return dp(tuple(a_list), 1)


def main(n):
    if n <= 0:
        # print("")
        pass
        return
    # Deterministic construction of a and b from n
    # a is an n-digit number with a simple repeating pattern
    digits_a = [(i % 10) for i in range(1, n + 1)]
    if digits_a[0] == 0:
        digits_a[0] = 1
    a = int(''.join(str(d) for d in digits_a))

    # b is another n-digit number, derived deterministically from a
    digits_b = [((d + 3) % 10) for d in digits_a]
    if digits_b[0] == 0:
        digits_b[0] = 2
    b = int(''.join(str(d) for d in digits_b))

    result = solve(a, b)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)