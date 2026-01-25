from math import ceil, floor, gcd, log, log2, factorial, sqrt
from collections import defaultdict, Counter, OrderedDict, deque
from itertools import combinations, permutations
from string import ascii_lowercase, ascii_uppercase
from bisect import *
from functools import reduce
from operator import mul

mod = int(1e9 + 7)
maxx = float('inf')

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


def generate_input(n):
    # Generate a deterministic list of single-digit integers using n as size.
    # Values cycle through 1..9, never 0, so S() in original is a string of digits.
    if n <= 0:
        n = 1
    arr = [(i % 9) + 1 for i in range(1, n + 1)]
    return arr


def main(n):
    arr = generate_input(n)
    ans = solve(arr)
    print(ans)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)