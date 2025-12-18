"""
    Template written to be used by Python Programmers.
    Use at your own risk!!!!
    Owned by enraged(rating - 5 star at CodeChef and Specialist at Codeforces).
"""
import sys
import bisect
import heapq
# from math import *
from collections import defaultdict as dd  # defaultdict(<datatype>) Free of KeyError.
from collections import deque  # deque(list) append(), appendleft(), pop(), popleft() - O(1)
from collections import Counter as c  # Counter(list)  return a dict with {key: count}
from itertools import combinations as comb
from bisect import bisect_left as bl, bisect_right as br, bisect
# sys.setrecursionlimit(2*pow(10, 6))
# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")
mod = pow(10, 9) + 7
mod2 = 998244353
def data(): return sys.stdin.readline().strip()


def out(var): sys.stdout.write(var)


def l(): return list(map(int, data().split()))


def sl(): return list(map(str, data().split()))


def sp(): return map(int, data().split())


def ssp(): return map(str, data().split())


def l1d(n, val=0): return [val for i in range(n)]


def l2d(n, m, val=0): return [[val for i in range(n)] for j in range(m)]


n = int(data())
arr = l()
dp = [[0 for j in range(500)] for i in range(500)]
dp2 = [0 for i in range(501)]
for i in range(n):
    dp[i][i] = arr[i]
i = n-2
while ~i:
    j = i+1
    while j < n:
        dp[i][j] = -1
        for k in range(i, j):
            if (~dp[i][k] and dp[i][k]) == dp[k+1][j]:
                dp[i][j] = dp[i][k]+1
        j += 1
    i -= 1
for i in range(1, n+1):
    dp2[i] = pow(10, 9)
    for j in range(i):
        if ~dp[j][i-1]:
            dp2[i] = min(dp2[i], dp2[j]+1)
out(str(dp2[n]))
