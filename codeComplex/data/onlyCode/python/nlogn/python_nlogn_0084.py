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
# sys.setrecursionlimit(999)


n,k = map(int,input().split())
t = []
for _ in [0]*n:
    t.append(list(map(int,input().split())))
t.sort(key=lambda x:(-x[0],x[1]))

pt = t[k-1]

print(t.count(pt))
