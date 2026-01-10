MOD = 10**9 + 7
from collections import defaultdict as dd

def check_sequence(n, edges, l):
    d = dd(list)
    for u, v in edges:
        d[u].append(v)
        d[v].append(u)
    v = [0] * (n + 1)
    s = 1
    what = 0
    v[1] = 1
    while what < s:
        a = set()
        i = l[what]
        for j in d[i]:
            if not v[j]:
                a.add(j)
        b = set()
        for j in range(s, s + len(a)):
            b.add(l[j])
        if a != b:
            return 'No'
        kkk = 0
        for k in a:
            kkk += 1
            v[k] = 1
        s += kkk
        what += 1
    if s != n:
        return 'No'
    return 'Yes'

def main(n):
    if n < 2:
        n = 2
    edges = []
    for i in range(2, n + 1):
        p = i // 2
        if p < 1:
            p = 1
        edges.append((p, i))
    # BFS order for the above tree
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    for i in range(1, n + 1):
        adj[i].sort()
    from collections import deque
    q = deque([1])
    visited = [False] * (n + 1)
    visited[1] = True
    l = []
    while q:
        x = q.popleft()
        l.append(x)
        for y in adj[x]:
            if not visited[y]:
                visited[y] = True
                q.append(y)
    res = check_sequence(n, edges, l)
    print(res)

if __name__ == "__main__":
    main(10)