MOD = 10**9 + 7
from collections import defaultdict as dd

def check_bfs(n, edges, l):
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

def generate_tree_edges(n):
    edges = []
    for i in range(2, n + 1):
        parent = i // 2
        edges.append((parent, i))
    return edges

def generate_l(n):
    # BFS order of the deterministic tree rooted at 1
    edges = generate_tree_edges(n)
    g = [[] for _ in range(n + 1)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    for i in range(1, n + 1):
        g[i].sort()
    from collections import deque
    q = deque([1])
    vis = [0] * (n + 1)
    vis[1] = 1
    order = []
    while q:
        x = q.popleft()
        order.append(x)
        for y in g[x]:
            if not vis[y]:
                vis[y] = 1
                q.append(y)
    return order

def main(n):
    if n < 1:
        return
    edges = generate_tree_edges(n)
    l = generate_l(n)
    res = check_bfs(n, edges, l)
    print(res)

if __name__ == "__main__":
    main(10)