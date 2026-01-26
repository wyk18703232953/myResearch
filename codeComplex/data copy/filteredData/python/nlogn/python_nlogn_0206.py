from bisect import bisect_left as bl
from bisect import bisect_right as br
import heapq
import math
from collections import *
from functools import reduce, cmp_to_key

def factors(n):
    return sorted(list(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))))

def generate_data(n):
    # Interpret n as number of pairs
    # Generate L and list l of size n deterministically
    # Each element: [x, t]
    # x ranges in [1, max(1, n//3)], t in [1, max(1, n//2)] via simple arithmetic
    L = max(1, n * 3)
    l = []
    max_x = max(1, n // 3)
    max_t = max(1, n // 2)
    for i in range(n):
        x = 1 + (i % max_x)
        t = 1 + (i % max_t)
        l.append([x, t])
    return n, L, l

def main(n):
    n, L, l = generate_data(n)

    index = defaultdict(list)
    for ind, i in enumerate(l):
        index[tuple(i)].append(ind + 1)

    l.sort(key=lambda x: x[1])
    d = defaultdict(list)

    ans = i = tot = currpoints = 0
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

if __name__ == "__main__":
    main(10)