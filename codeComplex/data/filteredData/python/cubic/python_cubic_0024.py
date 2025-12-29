import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right
import random
import string

def solve(s):
    """
    Actual solution: find the maximum length of a substring
    that appears at least twice in the string s.
    """
    mx = 0
    visited = set()
    for left in range(len(s)):
        for right in range(left, len(s)):
            substring = s[left: right + 1]
            if substring not in visited:
                visited.add(substring)
            else:
                mx = max(mx, len(substring))
    print(mx)

def main(n):
    """
    Generate a test string of length n and run solve(s) on it.
    Here we generate a random lowercase string of length n.
    """
    # To increase chances of repeated substrings, restrict alphabet size.
    alphabet = string.ascii_lowercase[:5]  # 'abcde'
    s = ''.join(random.choice(alphabet) for _ in range(n))
    solve(s)

if __name__ == "__main__":
    # Example: run main with some n
    main(10)