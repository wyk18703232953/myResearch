from math import ceil, floor, gcd, log, log2, factorial, sqrt
from collections import defaultdict, Counter, OrderedDict, deque
from itertools import combinations, permutations
from string import ascii_lowercase, ascii_uppercase
from bisect import *
from functools import reduce
from operator import mul

mod = int(1e9 + 7)
maxx = float('inf')


def nCr(n, r):
    return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)


def ceill(n, x):
    return (n + x - 1) // x


def solve_from_string(s):
    arr = [int(ch) for ch in s]
    d = {0}
    s_mod = 0
    ans = 0
    for i in arr:
        s_mod += i
        s_mod %= 3
        if s_mod in d:
            ans += 1
            s_mod = 0
            d = {0}
        d.add(s_mod)
    return ans


def main(n):
    if n < 1:
        n = 1
    digits = ["012", "120", "201"]
    s_chars = [digits[(i // 3) % 3][i % 3] for i in range(n)]
    s = "".join(s_chars)
    result = solve_from_string(s)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)