import sys
from collections import defaultdict as dc
from collections import Counter
from bisect import bisect_right, bisect_left
import math
from operator import itemgetter
from heapq import heapify, heappop, heappush
from queue import PriorityQueue as pq

def core_algorithm(n, m, l):
    x = dc(int)
    p = 0
    for val in l:
        x[val] += 1
        f = 1
        for i in range(1, n + 1):
            if x[i] == 0:
                f = 0
                break
        if f:
            p += 1
            for i in range(1, n + 1):
                x[i] -= 1
    return p

def generate_input(n):
    if n <= 0:
        n = 1
    # Define n as the number of distinct values (1..n)
    # Let each value appear exactly n times → m = n * n
    m = n * n
    # Deterministic construction: block-wise repetition of 1..n
    l = [(i % n) + 1 for i in range(m)]
    return n, m, l

def main(n):
    n_val, m_val, l = generate_input(n)
    result = core_algorithm(n_val, m_val, l)
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)