import sys
import string

from collections import Counter, defaultdict
from math import fsum, sqrt, gcd, ceil, factorial
from operator import *
from itertools import accumulate, count

inf = float("inf")
# input = sys.stdin.readline
flush = lambda: sys.stdout.flush
comb = lambda x, y: (factorial(x) // factorial(y)) // factorial(x - y)


# inputs
# ip = lambda : input().rstrip()
ip = lambda: input()
ii = lambda: int(input())
r = lambda: map(int, input().split())
rr = lambda: list(r())


arr = ip()
n = len(arr)
ms = ""
mn = 0


def counter(s, x):
    p = len(x)
    px = 0
    for i in range(len(s)):
        if s[i : i + p] == x:
            px += 1

    return px


for i in range(n):
    s = ""
    for j in range(i, n):
        s += arr[j]
        c = counter(arr, s)
        if c > 1 and len(s) > mn:
            ms = s
            mn = len(s)

print(mn)