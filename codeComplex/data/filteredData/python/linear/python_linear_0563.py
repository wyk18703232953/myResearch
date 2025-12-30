#!/usr/bin/python
# encoding:UTF-8
# Converted version with main(n) and no input()

import random
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


def solve_with_data(n, f):
    # 原 solve(fin) 的逻辑，只是把读入的数据改成参数
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
    print(' '.join(str(x) for x in count))


def main(n):
    """
    n 为规模，自动生成测试数据并调用原算法。
    生成规则：
    - 原始输入为：
        第一行：n
        第二行：n 个整数 f[i]
      程序中会对 f 做：new_f = [0] + f; 然后 new_f[i] -= 1 (i 从 0 到 n-1)
      因此为保证逻辑合理，我们生成 f[i] ∈ [1, n]。
      这样 new_f[i] ∈ [0, n-1]，始终是合法下标。
    """
    if n <= 0:
        return

    # 生成测试数据：f 为长度为 n 的数组，每个元素在 [1, n] 范围内
    f = [random.randint(1, n) for _ in range(n)]

    solve_with_data(n, f)


if __name__ == '__main__':
    # 示例：调用 main(10)，实际使用时可在外部按需调用 main(n)
    main(10)