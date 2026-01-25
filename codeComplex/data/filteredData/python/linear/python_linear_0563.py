#!/usr/bin/python
# encoding:UTF-8

import copy
from math import sqrt, fabs, ceil
from itertools import permutations, combinations
from collections import namedtuple


def get_array(x, initial=None):
    dimension = len(x)
    if dimension == 1:
        return [copy.deepcopy(initial) for _ in range(x[0])]
    else:
        return [get_array(x[1:], initial) for _ in range(x[0])]


def solve_from_data(n, f):
    new_f = [0] + f
    for i in range(0, n):
        new_f[i] -= 1
    f = new_f
    chs = get_array([n], [])
    for i, p in enumerate(f):
        if p >= 0:
            chs[p].append(i)
    q = [x for x in range(0, n) if not chs[x]]
    vis = [0] * n
    count = [0] * n
    while q:
        x = q.pop(0)
        if not chs[x]:
            count[x] = 1
        if f[x] >= 0:
            vis[f[x]] += 1
            if vis[f[x]] == len(chs[f[x]]):
                q.append(f[x])
            count[f[x]] += count[x]
    count = sorted(count)
    return count


def main(n):
    if n <= 0:
        print("")
        return
    f = [((i + 1) // 2 + 1) for i in range(n)]
    res = solve_from_data(n, f)
    print(" ".join(str(x) for x in res))


if __name__ == "__main__":
    main(10)