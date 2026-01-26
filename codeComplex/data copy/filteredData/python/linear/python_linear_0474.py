import math
from heapq import *
gcd = math.gcd
sqrt = math.sqrt
ceil = math.ceil

def ind(ch):
    return ord(ch) - ord("a")

def solve(n, cost, arr):
    b = [0]
    cost = b + cost
    arr = b + arr
    nv = [-1] * (n + 1)
    colors = []
    c = 0
    for i in range(1, n + 1):
        if nv[i] != -1:
            continue
        nv[i] = c
        dest = arr[i]
        while nv[dest] == -1:
            nv[dest] = c
            dest = arr[dest]
        if nv[dest] == c:
            colors.append(dest)
        c += 1
    s = 0
    for i in colors:
        mi = cost[i]
        nxt = arr[i]
        while nxt != i:
            mi = min(mi, cost[nxt])
            nxt = arr[nxt]
        s += mi
    return s

def main(n):
    if n <= 0:
        # print(0)
        pass
        return
    cost = [(i * 7) % (n + 3) + 1 for i in range(1, n + 1)]
    arr = [((i * 3) % n) + 1 for i in range(1, n + 1)]
    result = solve(n, cost, arr)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)