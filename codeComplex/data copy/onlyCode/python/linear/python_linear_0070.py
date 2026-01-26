import sys
from math import sqrt, log, log2, ceil, log10, gcd, floor, pow, sin, cos, tan, pi, inf, factorial
from copy import copy, deepcopy
from sys import exit, stdin, stdout
from collections import Counter, defaultdict, deque
from itertools import permutations
import heapq
from bisect import bisect_left 
from bisect import bisect_right
# sys.setrecursionlimit(100000000)
mod = 1000000007
iinp = lambda: int(sys.stdin.readline())
inp = lambda: sys.stdin.readline().strip()
strl = lambda: list(inp().strip().split(" "))
intl = lambda: list(map(int, inp().split(" ")))
mint = lambda: map(int, inp().split())
flol = lambda: list(map(float, inp().split(" ")))
flush = lambda: stdout.flush()
# ========================================================Functions====================================================
def solve():
 
    n,s=mint()
    cm=0
    for i in range(n):
        fi,ti=mint()
        if i==0:
            cm=fi+ti
        if i!=0:
            if fi+ti>cm:
                cm=fi+ti
    if cm>s:
        print(cm)
    else:
        print(s)
 
 
# ========================================================Main Code=====================================================
# t=iinp()
t=1
for _ in range(t):
        solve()