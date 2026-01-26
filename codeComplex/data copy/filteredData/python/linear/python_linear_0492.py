import sys
from collections import deque
mod = 10**9+7
INF = float('inf')

def build_tree(n):
    edges = [[] for _ in range(n)]
    if n <= 1:
        return edges
    for i in range(1, n):
        a = i
        b = (i // 2)
        edges[a].append(b)
        edges[b].append(a)
    return edges

def solve_with_edges(edges):
    n = len(edges)
    if n == 0:
        return 0
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
    while se and ind < len(pq):
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

def main(n):
    if n <= 0:
        # print(0)
        pass
        return
    edges = build_tree(n)
    res = solve_with_edges(edges)
    # print(res)
    pass
if __name__ == "__main__":
    main(10)