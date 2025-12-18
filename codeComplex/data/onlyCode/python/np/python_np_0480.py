import sys

input = sys.stdin.readline

from collections import deque

n,m,k = map(int,input().split())
p = [input().rstrip() for i in range(n)]
idx = {s:i for i,s in enumerate(p)}

def match(s):
    res = []
    for i in range(2**k):
        tmp = []
        for j in range(k):
            if i>>j & 1:
                tmp.append(s[j])
            else:
                tmp.append("_")
        res.append("".join(tmp))
    return set(res)

edge = [[] for i in range(n)]
deg = [0]*n
for i in range(m):
    s,mt = input().rstrip().split()
    mt = int(mt)-1
    t = p[mt]
    M = match(s)
    if t in M:
        for nv in M:
            if nv!=t and nv in idx:
                nv = idx[nv]
                edge[mt].append(nv)
                deg[nv] += 1
    else:
        exit(print("NO"))

deq = deque([v for v in range(n) if deg[v]==0])
res = []
while deq:
    v = deq.popleft()
    res.append(v+1)
    for nv in edge[v]:
        deg[nv] -= 1
        if deg[nv]==0:
            deq.append(nv)

if len(res)!=n:
    exit(print("NO"))

print("YES")
print(*res)
