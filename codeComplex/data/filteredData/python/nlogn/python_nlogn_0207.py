from bisect import bisect_left as bl
from bisect import bisect_right as br
import heapq
import math
from collections import defaultdict
from functools import reduce, cmp_to_key
import random


def factors(n):
    return sorted(list(set(reduce(list.__add__,
                                  ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))))


def main(n):
    # 生成测试数据：
    # n 行，每行两个整数 [type, length]
    # L 为长度上限
    #
    # 这里生成方式：
    #   type: 1..n 的随机值（类别）
    #   length: 1..10 的随机值
    #   L: 约为 5 * n，保证有一定可行空间
    random.seed(0)
    L = 5 * n
    l = []
    for _ in range(n):
        t = random.randint(1, max(1, n // 2))
        w = random.randint(1, 10)
        l.append([t, w])

    # 以下为原逻辑，仅删除 input 并使用上述生成的数据
    index = defaultdict(list)
    for ind, i in enumerate(l):
        index[tuple(i)].append(ind + 1)

    l.sort(key=lambda x: x[1])
    d = defaultdict(list)

    ans = i = tot = currpoints = 0
    anspattern = []
    he = []

    # 第一次循环：求最大 currpoints = ans
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

    # 第二次循环：构造达到 ans 的一个方案
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
                for length in d[typ]:
                    anspattern.append(index[tuple([typ, length])][-1])
                    index[tuple([typ, length])].pop()
            print(ans)
            print(len(anspattern))
            print(*sorted(anspattern))
            return
        i += 1


if __name__ == "__main__":
    # 可在此修改规模 n
    main(10)