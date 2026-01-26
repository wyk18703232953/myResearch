import math,itertools
from collections import Counter,deque,defaultdict
from bisect import bisect_left,bisect_right 
from heapq import heappop,heappush,heapify, nlargest
from copy import deepcopy

mod = 10**9+7
INF = float('inf')

def main(n):
    # Interpret n as number of nodes; edges m = n*(n-1)//2 (complete DAG)
    # Nodes are 1..n, and edges are from i to j for i<j to keep acyclic
    m = n * (n - 1) // 2
    abc = []
    w = 1
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            # Deterministic weight based on (a,b)
            c = a * n + b
            abc.append([a, b, c])
            w += 1

    def sol(X): 
        g = [[] for _ in range(n)]
        ny = [0]*n
        for a,b,c in abc:
            if c > X:
                g[a-1].append(b-1)
                ny[b-1] += 1
        seen = [0]*n
        q = deque()
        for i,x in enumerate(ny):
            if x==0:
                q.append(i)
                seen[i] = 1
        while q:
            v = q.popleft()
            for u in g[v]:
                if seen[u]:
                    continue
                ny[u] -= 1
                if ny[u] == 0:
                    q.append(u)
                    seen[u]= 1
        return all(seen)

    def sol2(X): 
        g = [[] for _ in range(n)]
        ny = [0]*n
        for a,b,c in abc:
            if c > X:
                g[a-1].append(b-1)
                ny[b-1] += 1
        tps = [-1]*n
        T = 0
        seen = [0]*n
        q = deque()
        for i,x in enumerate(ny):
            if x==0:
                q.append(i)
                seen[i] = 1
        while q:
            v = q.popleft()
            tps[v] = T
            T += 1
            for u in g[v]:
                if seen[u]:
                    continue
                ny[u] -= 1
                if ny[u] == 0:
                    q.append(u)
                    seen[u]= 1
        return tps

    ok = 10**9+10
    ng = -1
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if sol(mid):
            ok = mid

        else:
            ng = mid

    res = []
    tps = sol2(ok)
    for i,(a,b,c) in enumerate(abc):
        if c <= ok:
            if tps[a-1] > tps[b-1]:
                res.append(i+1)
    # print(ok,len(res))
    pass

    if res:
        # print(*res)
        pass

    else:
        # print()
        pass
if __name__ == "__main__":
    main(200)