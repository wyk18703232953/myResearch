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
    head = 0
    while head < len(q):
        x = q[head]
        head += 1
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


def generate_input(n):
    # n controls the total number of vertices in original bipartite set + number of edges
    # We map: number of original vertices = n//2 + 1, number of edges = n//2
    # Ensure at least 1 vertex and 1 edge when n is small
    if n < 2:
        n_vertices = 1
        m_edges = 1

    else:
        n_vertices = n // 2 + 1
        m_edges = n // 2
    # weights of size n_vertices, deterministic using simple formula
    weight = [0] + [(i % 7) + 1 for i in range(1, n_vertices + 1)]
    edges = []
    for i in range(1, m_edges + 1):
        # connect vertices in a deterministic structured way
        x = (i % n_vertices) + 1
        y = ((i * 2) % n_vertices) + 1
        if x == y:
            y = (y % n_vertices) + 1
        w = (i % 10) + 1
        edges.append((x, y, w))
    return n_vertices, m_edges, weight, edges


def main(n):
    global e, tot, S, T, he, INF, deep
    n_vertices, m_edges, weight, edges = generate_input(n)

    INF = 1000000007
    ans = 0

    e = [0, 0]
    tot = 1
    S = n_vertices + m_edges + 1
    T = S + 1
    he = [0 for _ in range(T + 1)]

    for i in range(1, n_vertices + 1):
        addedge(S, i, weight[i])
    for i in range(1, m_edges + 1):
        x, y, w = edges[i - 1]
        addedge(n_vertices + i, T, w)
        addedge(x, n_vertices + i, INF)
        addedge(y, n_vertices + i, INF)
        ans += w
    ans -= dinic()
    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)