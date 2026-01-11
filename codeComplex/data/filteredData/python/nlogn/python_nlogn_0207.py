from bisect import bisect_left as bl
from bisect import bisect_right as br
import heapq
import math
from collections import *
from functools import reduce, cmp_to_key

def factors(n):
    return sorted(list(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))))

def main(n):
    # Deterministic data generation
    # Interpret n as number of items; L as a deterministic function of n
    # Each item l[i] is a pair [a, b]
    # a in [1, n], b in [1, 2n], all deterministic
    L = 3 * n
    l = []
    for i in range(n):
        a = (i % max(1, (n // 3) + 1)) + 1
        b = (i * 2 + 1) % (2 * n + 1)
        if b == 0:
            b = 1
        l.append([a, b])

    index = defaultdict(list)
    for ind, item in enumerate(l):
        index[tuple(item)].append(ind + 1)

    l.sort(key=lambda x: x[1])
    d = defaultdict(list)

    ans = 0
    i = 0
    tot = 0
    currpoints = 0
    anspattern = []
    he = []

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

    i = 0
    tot = 0
    currpoints = 0
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
            for key in he:
                for j in d[key]:
                    anspattern.append(index[tuple([key, j])][-1])
                    index[tuple([key, j])].pop()
            # print(ans)
            pass
            # print(len(anspattern))
            pass
            # print(*sorted(anspattern))
            pass
            return

        i += 1

    # Fallback in case the above return doesn't trigger
    # print(ans)
    pass
    # print(0)
    pass
    # print()
    pass
if __name__ == "__main__":
    main(10)