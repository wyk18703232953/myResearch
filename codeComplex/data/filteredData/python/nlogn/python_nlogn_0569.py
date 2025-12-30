from bisect import bisect_right as br
from bisect import bisect_left as bl
from collections import defaultdict
from itertools import combinations
import sys
import math
import random

MAX = sys.maxsize
MAXN = 10**5 + 10
MOD = 10**9 + 7


def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def mhd(a, b, x, y):
    return abs(a - x) + abs(b - y)


def bfs(g, d, n):
    for i in range(n, 0, -1):
        while g[i]:
            x = g[i].pop()
            d[i] += d[x]
    return d


def main(n):
    # 生成测试数据：构造一个随机的父数组 l[1..n]
    # 原始代码中 l[1] 未被使用，l[2..n] 为父节点，范围 [1..i-1]
    if n <= 0:
        return

    if n == 1:
        print(1)
        return

    # 构造树的父关系 l[2..n]
    l = [0]  # 占位，使得索引从1开始
    l.append(0)  # l[1] 占位，不使用
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        l.append(parent)

    if n == 2:
        print(1, 1)
        return

    d = [0] * (n + 1)
    g = defaultdict(list)

    for i in range(2, n + 1):
        g[l[i]].append(i)
        d[i] += 1
        d[l[i]] += 1

    for i in range(1, n + 1):
        if g[i]:
            d[i] = 0

    x = bfs(g, d, n)
    x.sort()
    for i in range(1, n + 1):
        print(x[i], end=' ')
    print()


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)