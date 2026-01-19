import sys
input = sys.stdin.readline
from collections import defaultdict, Counter, deque

n, m, k = map(int, input().split())
P = [input()[:-1] for _ in range(n)]
S = [list(input().split()) for _ in range(m)]
idx = {p: i for i, p in enumerate(P, 1)}
G = defaultdict(list)
deg = Counter()
for s, i in S:
    i = int(i)
    cand = set()
    for mask in range(1 << k):
        cur = ['_'] * k
        for j in range(k):
            if mask >> j & 1: cur[j] = s[j]
        cur = "".join(cur)
        if cur in idx:
            cand.add(idx[cur])
    if i not in cand:
        print("NO")
        break
    for c in cand:
        if c == i: continue
        G[i].append(c)
        deg[c] += 1
else:
    ans = []
    q = deque([i for i in range(1, n + 1) if not deg[i]])
    while q:
        i = q.popleft()
        ans.append(i)
        for j in G[i]:
            deg[j] -= 1
            if not deg[j]:
                q.append(j)
    if len(ans) < n:
        print("NO")
    else:
        print("YES")
        print(*ans)