# -*- coding:utf-8 -*-

import bisect
import heapq
from typing import List, Tuple
import random


class Node:
    val = None

    def __init__(self, val):
        self.val = val
        self.left = Node
        self.right = None


def solve(W: int, H: int, N: int, A: List[Tuple[int, int]]) -> List[int]:
    xs = [0] + [v for t, v in A if t == 0] + [W]
    ys = [0] + [v for t, v in A if t == 1] + [H]
    xs.sort()
    ys.sort()

    xlist = Node(0)
    h = xlist
    xnodes = {0: h}
    maxw = max([xs[i + 1] - xs[i] for i in range(len(xs) - 1)] or [0])
    maxh = max([ys[i + 1] - ys[i] for i in range(len(ys) - 1)] or [0])
    for v in xs[1:]:
        n = Node(v)
        xnodes[v] = n
        h.right = n
        n.left = h
        h = n

    ylist = Node(0)
    h = ylist
    ynodes = {0: h}
    for v in ys[1:]:
        n = Node(v)
        ynodes[v] = n
        h.right = n
        n.left = h
        h = n

    ans = []
    maxarea = maxh * maxw
    for t, v in reversed(A):
        ans.append(maxarea)
        if t == 0:
            node = xnodes[v]
            w = node.right.val - node.left.val
            maxw = max(maxw, w)
        else:
            node = ynodes[v]
            h = node.right.val - node.left.val
            maxh = max(maxh, h)
        node.left.right = node.right
        node.right.left = node.left
        maxarea = maxh * maxw

    return ans[::-1]


def generate_test_data(n: int, max_coord: int = 10**9):
    """
    生成测试数据：
    - W, H: 在 (1, max_coord] 内随机
    - N: 使用参数 n
    - A: 随机生成 N 次切割，保证切割坐标在 (0, W) 或 (0, H) 之内
    方向：0 表示竖切(V)，1 表示横切(H)
    """
    W = random.randint(1, max_coord)
    H = random.randint(1, max_coord)
    N = n

    A = []
    # 为避免大量重复，可以从可选坐标中选；但是不强制唯一
    for _ in range(N):
        t = random.randint(0, 1)  # 0: V, 1: H
        if t == 0:
            if W > 1:
                v = random.randint(1, W - 1)
            else:
                v = 0
        else:
            if H > 1:
                v = random.randint(1, H - 1)
            else:
                v = 0
        A.append((t, v))

    return W, H, N, A


def main(n: int):
    W, H, N, A = generate_test_data(n)
    ans = solve(W, H, N, A)
    print('\n'.join(map(str, ans)))


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)