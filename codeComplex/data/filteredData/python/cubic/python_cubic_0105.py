class edge(object):
    def __init__(self, ne, to, fl):
        self.ne = ne
        self.to = to
        self.fl = fl

def add(x, y, z):
    global tot, e, he
    tot += 1
    e.append(edge(he[x], y, z))
    he[x] = tot

def addedge(x, y, z):
    add(x, y, z)
    add(y, x, 0)

def bfs():
    global deep, T, S, he, e
    deep = [0 for _ in range(T + 1)]
    q = [S]
    deep[S] = 1
    lp = 0
    while len(q) > lp:
        x = q[lp]
        lp += 1
        i = he[x]
        while i:
            y = e[i].to
            if deep[y] == 0 and e[i].fl != 0:
                deep[y] = deep[x] + 1
                q.append(y)
            i = e[i].ne
    return deep[T] != 0

def dfs(x, flow):
    global deep, T, he, e
    if x == T or flow == 0:
        return flow
    used = 0
    i = he[x]
    while i:
        y = e[i].to
        if deep[y] == deep[x] + 1 and e[i].fl != 0:
            now = dfs(y, min(flow - used, e[i].fl))
            used += now
            e[i].fl -= now
            e[i ^ 1].fl += now
            if flow == used:
                break
        i = e[i].ne
    if used == 0:
        deep[x] = -1
    return used

def dinic():
    global S, INF
    res = 0
    while bfs():
        res += dfs(S, INF)
    return res

def main(n):
    global e, tot, S, T, he, INF, deep

    # Scale: treat n as number of original nodes.
    # Define number of extra nodes m as n (same order of magnitude).
    if n <= 0:
        return 0

    m = n

    # Deterministic weight generation for n nodes: weight[i] = (i % 10) + 1
    weight = [0] + [ (i % 10) + 1 for i in range(1, n + 1) ]

    e = [0, 0]
    tot = 1
    S = n + m + 1
    T = S + 1
    he = [0 for _ in range(T + 1)]
    INF = 1000000007

    ans = 0

    # Edges from S to original nodes with capacity = weight[i]
    for i in range(1, n + 1):
        addedge(S, i, weight[i])

    # Deterministic construction of m "item" nodes:
    # For each i in 1..m:
    #   x = (i % n) + 1
    #   y = ((i * 2) % n) + 1
    #   w = (i % 7) + 1
    #   edges: (n+i -> T, cap=w), (x -> n+i, INF), (y -> n+i, INF)
    for i in range(1, m + 1):
        x = (i % n) + 1
        y = ((i * 2) % n) + 1
        w = (i % 7) + 1
        addedge(n + i, T, w)
        addedge(x, n + i, INF)
        addedge(y, n + i, INF)
        ans += w

    ans -= dinic()
    # print(ans)
    pass
    return ans

if __name__ == "__main__":
    main(10)