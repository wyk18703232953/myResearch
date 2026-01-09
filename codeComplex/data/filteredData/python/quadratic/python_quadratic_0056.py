import sys,math,itertools
from collections import Counter,deque,defaultdict
from bisect import bisect_left,bisect_right 
from heapq import heappop,heappush,heapify, nlargest
from copy import deepcopy
mod = 10**9+7
INF = float('inf')

def main(n):
    # Interpret n as array length; number of queries q is set to n
    # Deterministic construction of array a
    a = [(i * 3 + 1) % (2 * n + 1) for i in range(n)]

    res = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i] > a[j]:
                res = 1 - res

    q = n
    for k in range(q):
        # Deterministic generation of (l, r) within [0, n-1]
        l = k % n
        r = (k * 2 + 1) % n
        if l > r:
            l, r = r, l
        m = r - l + 1
        swap = m * (m - 1) // 2
        if swap % 2:
            res = 1 - res
        # print('odd' if res else 'even')
        pass
if __name__ == "__main__":
    main(5)