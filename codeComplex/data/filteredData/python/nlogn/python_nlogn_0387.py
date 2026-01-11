import sys
import math
import bisect
import heapq
from bisect import bisect_right

def myceil(x, y):
    return (x + y - 1) // y

def Solution(td, n, k):
    mxHeap = []
    td = sorted(td, key=lambda x: x[0])
    prefix = []
    tmp = 0
    for v in td:
        b = v[1]
        tmpAns = tmp + b
        if len(mxHeap) == k:
            if len(mxHeap) and b > mxHeap[0]:
                t = heapq.heappop(mxHeap)
                heapq.heappush(mxHeap, b)
                tmp -= t
                tmp += b
        elif len(mxHeap) < k:
            tmp += b
            heapq.heappush(mxHeap, b)
        prefix.append([tmpAns, v[2]])

    ans = [0 for _ in range(n)]
    for v in prefix:
        ans[v[1]] = v[0]
    # print(*ans)
    pass

def main(n):
    k = max(1, n // 2)
    a = [i + 1 for i in range(n)]
    b = [(i * 2 + 3) % (n + 5) + 1 for i in range(n)]
    td = [[a[i], b[i], i] for i in range(n)]
    Solution(td, n, k)

if __name__ == "__main__":
    main(5)