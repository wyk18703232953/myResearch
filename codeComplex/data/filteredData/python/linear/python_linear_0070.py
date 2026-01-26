import sys
from math import sqrt, log, log2, ceil, log10, gcd, floor, pow, sin, cos, tan, pi, inf, factorial
from copy import copy, deepcopy
from sys import exit, stdin, stdout
from collections import Counter, defaultdict, deque
from itertools import permutations
import heapq
from bisect import bisect_left 
from bisect import bisect_right

mod = 1000000007

def main(n):
    t = 1
    for _ in range(t):
        solve(n)

def solve(n):
    s = n // 2
    n_val = max(1, n)
    cm = 0
    for i in range(n_val):
        fi = i
        ti = n_val - i
        if i == 0:
            cm = fi + ti

        else:
            if fi + ti > cm:
                cm = fi + ti
    if cm > s:
        # print(cm)
        pass

    else:
        # print(s)
        pass
if __name__ == "__main__":
    main(10)