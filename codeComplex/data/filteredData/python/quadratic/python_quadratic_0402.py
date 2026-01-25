from math import ceil, floor, gcd, log, log2, factorial
from collections import *

maxx = float('inf')


def generate_input(n):
    if n < 1:
        n = 1
    # s: length n, periodic pattern "ab"
    s = ''.join('ab'[i % 2] for i in range(n))
    # k: a scale-dependent repetition factor
    k = n
    return n, k, s


def core_logic(n, k, s):
    i = 1
    # find smallest i such that suffix from i equals prefix without last i chars
    while s[i:] != s[:-i]:
        i += 1
        if i >= len(s):  # safety guard, though normally loop finds a match
            break
    return s[:i] * k + s[i:]


def main(n):
    n, k, s = generate_input(n)
    result = core_logic(n, k, s)
    print(result)


if __name__ == "__main__":
    main(10)