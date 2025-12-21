import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right
import random
import string

start_time = time.time()

def solve(s):
    mx = 0
    visited = set()
    for left in range(len(s)):
        for right in range(left, len(s)):
            substring = s[left : right + 1]
            if substring not in visited:
                visited.add(substring)
            elif substring in visited:
                mx = max(mx, len(substring))
    print(mx)
    return mx

def main(n):
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    return solve(s)

if __name__ == "__main__":
    main(10)