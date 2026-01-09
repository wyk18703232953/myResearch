import sys
from collections import deque

mod = 10**9+7
INF = float('inf')

def solve(edges):
    n = len(edges)
    dist = [-1] * n
    dist[0] = 0
    pa = [-1] * n
    se = set()
    pq = []
    q = deque()
    q.append(0)
    while q:
        now = q.popleft()
        for nx in edges[now]:
            if dist[nx] != -1:
                continue
            pa[nx] = now
            dist[nx] = dist[now] + 1
            if dist[nx] > 2:
                se.add(nx)
                pq.append((dist[nx], nx))
            q.append(nx)
    pq = pq[::-1]
    res = 0
    ind = 0
    while se:
        d, v = pq[ind]
        ind += 1
        if v not in se:
            continue
        res += 1
        pv = pa[v]
        se.discard(pv)
        for nv in edges[pv]:
            se.discard(nv)
    return res

def generate_tree(n):
    if n <= 1:
        return [[] for _ in range(max(n, 1))]
    edges = [[] for _ in range(n)]
    # deterministic tree: connect i to i//2 for i >= 1 (like a heap tree)
    for i in range(1, n):
        p = i // 2
        edges[p].append(i)
        edges[i].append(p)
    return edges

def main(n):
    n = int(n)
    if n <= 0:
        n = 1
    edges = generate_tree(n)
    res = solve(edges)
    # print(res)
    pass
if __name__ == "__main__":
    main(10)