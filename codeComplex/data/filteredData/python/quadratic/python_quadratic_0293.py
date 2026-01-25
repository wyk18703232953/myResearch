import os
from io import BytesIO, IOBase
import sys
from collections import defaultdict, deque, Counter
from math import sqrt, pi, ceil, log, inf, gcd, floor
from itertools import combinations, permutations
from bisect import *
from fractions import Fraction
from heapq import *

def solve(a, n):
    ans = 0
    for i in range(0, 2 * n, 2):
        if a[i] != a[i + 1]:
            for j in range(i + 1, 2 * n):
                if a[j] == a[i]:
                    for k in range(j, i + 1, -1):
                        a[k], a[k - 1] = a[k - 1], a[k]
                        ans += 1
                    break
    return ans

def generate_input(n):
    if n <= 0:
        n = 1
    # generate 2*n elements forming n pairs; pattern depends deterministically on n
    a = []
    for i in range(n):
        if i % 2 == 0:
            # already adjacent pair
            v = (i % 5) + 1
            a.extend([v, v])
        else:
            # create a misaligned pair to trigger swaps
            v1 = (i % 7) + 1
            v2 = (i % 11) + 1
            a.append(v1)
            a.append(v2)
    return a, n

def main(n):
    a, size = generate_input(n)
    ans = solve(a, size)
    print(ans)

if __name__ == "__main__":
    main(5)