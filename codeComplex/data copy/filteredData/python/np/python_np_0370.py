import sys
from math import factorial
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush

mod = 998244353
INF = float('inf')

def comb(n, m): return factorial(n) / (factorial(m) * factorial(n - m)) if n >= m else 0
def perm(n, m): return factorial(n) // (factorial(n - m)) if n >= m else 0
def mdis(x1, y1, x2, y2): return abs(x1 - x2) + abs(y1 - y2)

def generate_test_case(case_id, n):
    rows = n
    cols = min(n, 10)
    arr = []
    base = case_id * 100000
    for i in range(rows):
        row = [((base + i * cols + j) % 1000) for j in range(cols)]
        arr.append(row)
    return rows, cols, arr

def solve_single(n, m, arr):
    larr = [list(i) for i in zip(*arr)]
    larr.sort(key=lambda a: max(a), reverse=True)
    larr = larr[:n]

    res = 0

    def dfs(lst, pos=0):
        nonlocal res
        if pos == min(n, len(larr)):
            res = max(res, sum(lst))
            return
        for i in range(n):
            nex = lst.copy()
            for j in range(n):
                if j < len(larr[pos]):
                    idx = (i + j) % n
                    val = larr[pos][j]
                    if val > nex[idx]:
                        nex[idx] = val
            dfs(nex, pos + 1)

    dfs([0] * n)
    return res

def main(n):
    t = max(1, n)
    outputs = []
    for case_id in range(t):
        rows, cols, arr = generate_test_case(case_id, n)
        res = solve_single(rows, cols, arr)
        outputs.append(res)
    for val in outputs:
        print(val)

if __name__ == "__main__":
    main(5)