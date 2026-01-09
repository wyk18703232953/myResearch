import sys
import string

from collections import Counter, defaultdict
from math import fsum, sqrt, gcd, ceil, factorial
from operator import *
from itertools import accumulate, count

inf = float("inf")
flush = lambda: sys.stdout.flush
comb = lambda x, y: (factorial(x) // factorial(y)) // factorial(x - y)


def counter(s, x):
    p = len(x)
    px = 0
    for i in range(len(s)):
        if s[i : i + p] == x:
            px += 1
    return px


def main(n):
    # deterministic generation of input string of length n
    base_chars = "abcdefghijklmnopqrstuvwxyz"
    base_len = len(base_chars)
    arr = "".join(base_chars[i % base_len] for i in range(n))

    length = len(arr)
    ms = ""
    mn = 0

    for i in range(length):
        s = ""
        for j in range(i, length):
            s += arr[j]
            c = counter(arr, s)
            if c > 1 and len(s) > mn:
                ms = s
                mn = len(s)
    # print(mn)
    pass
if __name__ == "__main__":
    main(10)