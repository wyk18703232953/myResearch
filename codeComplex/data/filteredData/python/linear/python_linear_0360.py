from math import ceil, floor, gcd, log, log2, factorial, sqrt
from collections import defaultdict, Counter, OrderedDict, deque
from itertools import combinations, permutations
from string import ascii_lowercase, ascii_uppercase
from bisect import *
from functools import reduce
from operator import mul

mod = int(1e9 + 7)
maxx = float('inf')
localsys = 0

nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)


def ceill(n, x):
    return (n + x - 1) // x


def solve(arr):
    s, cnt, ans = 0, 0, 0
    for i in arr:
        s, cnt = s + i, cnt + 1
        if i % 3 == 0 or cnt % 3 == 0 or s % 3 == 0:
            s, cnt, ans = 0, 0, ans + 1
    return ans


def main(n):
    if n <= 0:
        n = 1
    # deterministically generate "digits" similar to list(map(int, S()))
    # we use a repeating pattern of 0..9 to control divisibility by 3
    arr = [(i % 10) for i in range(n)]
    ans = solve(arr)
    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)