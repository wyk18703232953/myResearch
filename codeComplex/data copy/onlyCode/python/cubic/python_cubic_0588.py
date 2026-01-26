from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush,heappop,heapify
import math
from collections import *
from functools import reduce,cmp_to_key
import sys
input = sys.stdin.readline

from itertools import accumulate
from functools import lru_cache

M = mod = 998244353
def factors(n):return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n):return pow(n, mod - 2, mod)
 
def li():return [int(i) for i in input().rstrip('\n').split()]
def st():return input().rstrip('\n')
def val():return int(input().rstrip('\n'))
def li2():return [i for i in input().rstrip('\n')]
def li3():return [int(i) for i in input().rstrip('\n')]


a = val()
b = val()

n = len(str(a))

a = [int(i) for i in str(a)]
a.sort()
if len(str(b)) > n:
    
    print(*sorted(a, reverse = 1), sep = '')
    exit()

b = str(b)
b = [int(i) for i in b]


def makenum(s):return int(''.join(str(e) for e in s))

def givemax(a, b):
    if len(a) > len(b):return a
    elif len(b) > len(a):return b
    else:
        for j in range(len(a)):
            if a[j] > b[j]:return a
            elif b[j] > a[j]:return b
        return a


@lru_cache(None)
def dp(l, equal = 1):

    if len(l) == 1:return str(-float('inf')) if l[0] > b[-1] and equal else str(l[0])
    if not equal:return ''.join(str(e) for e in sorted(l, reverse = 1))
    ans = ''
    l = list(l)
    curr = b[n - len(l)]
    for i in range(len(l)):
        if l[i] < curr and dp(tuple(l[:i] + l[i + 1:]), 0) != '-inf':
            ans = givemax(ans, str(l[i]) + dp(tuple(l[:i] + l[i + 1:]), 0))
        elif l[i] == curr and dp(tuple(l[:i] + l[i + 1:]), 1) != '-inf':
            ans = givemax(ans, str(l[i]) + dp(tuple(l[:i] + l[i + 1:]), 1))

    return str(ans)

print(dp(tuple(a), 1))