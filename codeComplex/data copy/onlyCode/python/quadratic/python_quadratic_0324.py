import heapq
import sys
input = sys.stdin.readline

n, d, k = map(int, input().split())
if n == 1 or n <= d:
    ans = "NO"
elif k == 1:
    ans = "YES" if n == 2 and d == 1 else "NO"
    e = [(1, 2)]
else:
    e = [(i + 1, i + 2) for i in range(d)]
    h = []
    l, r = 1, d + 1
    if k > 2:
        for i in range(2, d + 1):
            heapq.heappush(h, (i, 2, min(i - l, r - i)))
    ans = "YES"
    for i in range(d + 2, n + 1):
        if not h:
            ans = "NO"
            break
        j, k0, d0 = heapq.heappop(h)
        e.append((j, i))
        if k0 + 1 < k:
            heapq.heappush(h, (j, k0 + 1, d0))
        if d0 - 1 > 0:
            heapq.heappush(h, (i, 1, d0 - 1))
print(ans)
if ans == "YES":
    for u, v in e:
        print(u, v)