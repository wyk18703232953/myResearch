import sys

from math import factorial
from collections import Counter, defaultdict
from heapq import heapify, heappop, heappush

mod = 998244353
INF = float('inf')


def comb(n, m):
    return factorial(n) / (factorial(m) * factorial(n - m)) if n >= m else 0


def perm(n, m):
    return factorial(n) // (factorial(n - m)) if n >= m else 0


def mdis(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def generate_matrix(n):
    if n <= 0:
        return 0, 0, []
    # Define matrix size based on n
    rows = n
    cols = max(1, n // 2)
    # Deterministic value generation: simple arithmetic pattern
    arr = [[(i * 37 + j * 91) % (10**9) for j in range(cols)] for i in range(rows)]
    return rows, cols, arr


def solve_with_matrix(n, m, arr):
    res = []

    def c(num):
        nonlocal res
        dic = {}
        for i in range(n):
            now = 0
            for j in range(m):
                if arr[i][j] >= num:
                    now |= 1 << j
            dic[now] = i + 1

        full = (1 << m) - 1
        for k, v in dic.items():
            for kk, vv in dic.items():
                if k | kk == full:
                    res = [v, vv]
                    return True
        return False

    l, r = 0, 10 ** 9
    while l <= r:
        mp = (l + r + 1) // 2
        now = c(mp)
        if now:
            l = mp + 1
        else:
            r = mp - 1

    return res


def main(n):
    n_rows, m_cols, arr = generate_matrix(n)
    if n_rows == 0 or m_cols == 0:
        print(-1, -1)
        return
    res = solve_with_matrix(n_rows, m_cols, arr)
    if res:
        print(*res)
    else:
        print(-1, -1)


if __name__ == "__main__":
    main(5)