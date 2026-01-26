import math
from heapq import *

gcd = math.gcd
sqrt = math.sqrt
ceil = math.ceil


def ind(ch):
    return ord(ch) - ord("a")


def generate_data(n):
    if n < 1:
        n = 1
    cost = [0] * (n + 1)
    arr = [0] * (n + 1)
    for i in range(1, n + 1):
        cost[i] = (i * 7) % (n + 3) + 1
    for i in range(1, n + 1):
        # create a permutation-like mapping with a simple deterministic rule
        arr[i] = (i * 2) % n + 1
    return n, cost, arr


def core_logic(n, cost, arr):
    b = [0]
    cost = b + cost[1:]
    arr = b + arr[1:]
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
    n, cost, arr = generate_data(n)
    result = core_logic(n, cost, arr)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)