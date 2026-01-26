import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import sys
import string
import random
from typing import List
sys.setrecursionlimit(99999)

n,k = map(int,input().split())
arr = list(map(int,input().split()))
cs = collections.Counter(arr)
ks = list(cs.keys())
ks.sort()
ans= 0
for i in range(1,len(ks)):
    if ks[i]<=ks[i-1]+k:
        continue
    else:
        ans+=cs[ks[i-1]]
ans+= cs[ks[-1]]
print(ans)