import math
import itertools
from collections import Counter, deque, defaultdict
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush, heapify, nlargest
from copy import deepcopy

mod = 10**9 + 7
INF = float('inf')


def main(n):
    # Interpret n as the size of the array a
    # Number of queries q is chosen deterministically as n
    if n <= 0:
        return

    # Deterministic construction of array a of length n
    # Example pattern: a[i] = (i * 3) % (n // 2 + 1)
    a = [(i * 3) % (n // 2 + 1) for i in range(n)]

    # Initial parity computation of inversion count
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                res = 1 - res

    # Deterministic construction of queries
    # Use q = n queries
    q = n
    queries = []
    for i in range(q):
        # Create a segment [l, r] that depends deterministically on i and n
        l = i % n
        r = (n - 1) - (i // 2 % n)
        if l > r:
            l, r = r, l
        queries.append((l + 1, r + 1))  # original code used 1-based l, r

    # Process queries and print results
    for l, r in queries:
        m = r - l + 1
        swap = m * (m - 1) // 2
        if swap % 2:
            res = 1 - res
        # print('odd' if res else 'even')
        pass
if __name__ == "__main__":
    # Example deterministic call
    main(10)