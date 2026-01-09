import math
from heapq import *

gcd = math.gcd
sqrt = math.sqrt
ceil = math.ceil

def ind(ch):
    return ord(ch) - ord("a")

def generate_cost_and_perm(n):
    b = [0]
    cost = b + [(i * 3 + 7) % (2 * n + 5) + 1 for i in range(1, n + 1)]
    arr = b + [0] * n
    for i in range(1, n):
        arr[i] = i + 1
    arr[n] = 1
    return cost, arr

def main(n):
    cost, arr = generate_cost_and_perm(n)
    b = [0]
    cost = cost
    arr = arr
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
    # print(s)
    pass
if __name__ == "__main__":
    main(10)