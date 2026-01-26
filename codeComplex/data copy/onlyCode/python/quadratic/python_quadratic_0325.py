from collections import deque
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
    q = deque()
    l, r = 1, d + 1
    if k > 2:
        for i in range(2, d + 1):
            q.append((i, 2, min(i - l, r - i)))
    ans = "YES"
    for i in range(d + 2, n + 1):
        if not q:
            ans = "NO"
            break
        j, k0, d0 = q.popleft()
        e.append((j, i))
        if k0 + 1 < k:
            q.append((j, k0 + 1, d0))
        if d0 - 1 > 0:
            q.append((i, 1, d0 - 1))
print(ans)
if ans == "YES":
    for u, v in e:
        print(u, v)