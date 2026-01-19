import math
import sys
from bisect import bisect_right, bisect_left, insort_right
from collections import Counter, defaultdict
from heapq import heappop, heappush
from itertools import accumulate
from sys import stdout

R = lambda: map(int, input().split())
t = input()
s = input()
k = t.count('+') - s.count('+')
n = s.count('?')
if k > n or k < 0:
    print('0.0')
else:
    print(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)) / 2**n)