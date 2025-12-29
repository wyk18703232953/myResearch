import sys
import math
import itertools
from collections import Counter, deque, defaultdict
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush, heapify, nlargest
from copy import deepcopy
import random

mod = 10 ** 9 + 7
INF = float('inf')


def main(n: int):
    """
    生成规模为 n 的测试数据并执行原逻辑。
    这里的规模 n 表示图中顶点数，边数 m 由 n 派生或随机生成。
    """

    # ========= 测试数据生成部分 =========
    # 生成一个有向图，带权边 (a, b, c)
    # 约定：1 <= a, b <= n，权值 c 为 [0, 10^9] 之间的整数
    # 边数 m：这里取 m = n * 2（可按需要修改）
    m = max(1, n * 2)

    abc = []
    for _ in range(m):
        a = random.randint(1, n)
        b = random.randint(1, n)
        c = random.randint(0, 10 ** 9)
        abc.append([a, b, c])

    # ========= 原逻辑开始（使用生成的 abc, n, m） =========

    def sol(X):
        g = [[] for _ in range(n)]
        ny = [0] * n
        for a, b, c in abc:
            if c > X:
                g[a - 1].append(b - 1)
                ny[b - 1] += 1
        seen = [0] * n
        q = deque()
        for i, x in enumerate(ny):
            if x == 0:
                q.append(i)
                seen[i] = 1
        while q:
            v = q.popleft()
            for u in g[v]:
                if seen[u]:
                    continue
                ny[u] -= 1
                if ny[u] == 0:
                    q.append(u)
                    seen[u] = 1
        return all(seen)

    def sol2(X):
        g = [[] for _ in range(n)]
        ny = [0] * n
        for a, b, c in abc:
            if c > X:
                g[a - 1].append(b - 1)
                ny[b - 1] += 1
        tps = [-1] * n
        T = 0
        seen = [0] * n
        q = deque()
        for i, x in enumerate(ny):
            if x == 0:
                q.append(i)
                seen[i] = 1
        while q:
            v = q.popleft()
            tps[v] = T
            T += 1
            for u in g[v]:
                if seen[u]:
                    continue
                ny[u] -= 1
                if ny[u] == 0:
                    q.append(u)
                    seen[u] = 1
        return tps

    ok = 10 ** 9 + 10
    ng = -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if sol(mid):
            ok = mid
        else:
            ng = mid

    res = []
    tps = sol2(ok)
    for i, (a, b, c) in enumerate(abc):
        if c <= ok:
            if tps[a - 1] > tps[b - 1]:
                res.append(i + 1)

    print(ok, len(res))
    if res:
        print(*res)
    else:
        print()


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)