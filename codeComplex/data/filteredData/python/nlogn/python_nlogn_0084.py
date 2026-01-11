import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import random
import re
import sys
import time
import string
from typing import List

def generate_input(n):
    if n < 2:
        n = 2
    k = n // 2 + 1
    t = []
    for i in range(n):
        a = n - (i % 5)
        b = (i * 3) % 7
        t.append([a, b])
    return n, k, t

def solve(n, k, t):
    t.sort(key=lambda x: (-x[0], x[1]))
    pt = t[k-1]
    return t.count(pt)

def main(n):
    n, k, t = generate_input(n)
    ans = solve(n, k, t)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)