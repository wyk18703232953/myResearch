from bisect import bisect_left as bl
from bisect import bisect_right as br
import heapq
import math
from collections import *
from functools import reduce, cmp_to_key
import random


def factors(n):
    return sorted(list(set(reduce(list.__add__,
                                  ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))))


def main(n):
    # 1. 生成测试数据
    # 生成一个容量 L 和 n 个项目 (type, cost)
    # type 在 [1, max_type]，cost 在 [1, max_cost]
    max_type = max(1, n // 3)
    max_cost = 10 ** 3
    # 让总容量大概是所有花费的 1/2 左右，保证有可行解
    l = []
    total_cost = 0
    for _ in range(n):
        t = random.randint(1, max_type)
        c = random.randint(1, max_cost)
        l.append([t, c])
        total_cost += c
    L = max(1, total_cost // 2)

    # 2. 原逻辑开始（用生成的 n, L, l）

    index = defaultdict(list)
    for ind, item in enumerate(l):
        index[tuple(item)].append(ind + 1)

    l.sort(key=lambda x: x[1])
    d = defaultdict(list)

    ans = i = tot = currpoints = 0
    anspattern = []
    he = []

    # 第一次遍历：求最大 ans
    while i < n:
        if l[i][1] + tot <= L:
            tot += l[i][1]
            heapq.heappush(d[l[i][0]], l[i][1])
            currpoints += 1

            if len(d[l[i][0]]) == 1:
                heapq.heappush(he, l[i][0])

        while len(he) and currpoints > he[0]:
            temp = heapq.heappop(he)
            tot -= heapq.heappop(d[temp])
            currpoints -= 1
            if len(d[temp]):
                heapq.heappush(he, temp)

        if currpoints > ans:
            ans = currpoints

        i += 1

    # 第二次遍历：构造达到 ans 的模式
    i = tot = currpoints = 0
    he = []
    d = defaultdict(list)

    while i < n:
        if l[i][1] + tot <= L:
            tot += l[i][1]
            heapq.heappush(d[l[i][0]], l[i][1])
            currpoints += 1

            if len(d[l[i][0]]) == 1:
                heapq.heappush(he, l[i][0])

        while len(he) and currpoints > he[0]:
            temp = heapq.heappop(he)
            tot -= heapq.heappop(d[temp])
            currpoints -= 1
            if len(d[temp]):
                heapq.heappush(he, temp)

        if currpoints == ans:
            anspattern = []
            for typ in he:
                for cost in d[typ]:
                    key = tuple([typ, cost])
                    anspattern.append(index[key][-1])
                    index[key].pop()
            print(ans)
            print(len(anspattern))
            print(*sorted(anspattern))
            return

        i += 1


if __name__ == "__main__":
    # 示例：使用规模 n = 10 运行
    main(10)