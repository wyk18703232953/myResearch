import sys
input=sys.stdin.readline
from collections import defaultdict as dc
from collections import Counter
from bisect import bisect_right, bisect_left
import math
from operator import itemgetter
from heapq import heapify, heappop, heappush
from queue import PriorityQueue as pq
n=int(input())
if n<=5:
    print(-1)
else:
    for i in range(2,5):
        print(1,i)
    for i in range(5,n+1):
        print(2,i)
for i in range(2,n+1):
    print(1,i)