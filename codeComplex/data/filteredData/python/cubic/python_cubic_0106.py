from collections import deque

inf = 2 * (10 ** 12)

def addedge(e, u, v, value):
    a = [v, value, None]
    b = [u, 0, a]
    a[2] = b
    e[u].append(a)
    e[v].append(b)

def dinic(n, m, a, edges):
    S, T = 0, m + n + 1
    size = n + m + 2
    e = [[] for _ in range(size)]
    ans = 0
    for i, (u, v, w) in enumerate(edges, start=1):
        ans += w
        addedge(e, i, u + m, inf)
        addedge(e, i, v + m, inf)
        addedge(e, S, i, w)
    for i in range(m + 1, T):
        addedge(e, i, T, a[i - m - 1])

    def bfs():
        lvl = [0] * size
        q = deque([S])
        lvl[S] = 1
        while q:
            node = q.popleft()
            for edge in e[node]:
                if edge[0] != S and lvl[edge[0]] == 0 and edge[1]:
                    lvl[edge[0]] = lvl[node] + 1
                    q.append(edge[0])
        return lvl

    def dfs(node, maxdelta, lvl, T):
        if node == T:
            return maxdelta
        delta = 0
        for edge in e[node]:
            if lvl[edge[0]] == lvl[node] + 1 and edge[1]:
                tmp = dfs(edge[0], min(maxdelta, edge[1]), lvl, T)
                if tmp > 0:
                    edge[1] -= tmp
                    edge[2][1] += tmp
                    maxdelta -= tmp
                    delta += tmp
                if maxdelta == 0:
                    break
        return delta

    flow = 0
    while True:
        lvl = bfs()
        tmp = dfs(S, inf, lvl, T)
        if tmp == 0:
            break
        flow += tmp
    ans -= flow
    return ans

def generate_input(n):
    # Map n to graph parameters
    if n < 2:
        n_nodes = 1
        m_edges = 1

    else:
        n_nodes = n
        m_edges = n  # one hyper-edge per index

    # a: capacities for n nodes
    a = [i + 1 for i in range(n_nodes)]

    edges = []
    for i in range(1, m_edges + 1):
        u = (i % n_nodes) + 1
        v = ((i * 2) % n_nodes) + 1
        w = (i * 3) % (10 ** 6) + 1
        edges.append((u, v, w))

    return n_nodes, m_edges, tuple(a), edges

def main(n):
    n_nodes, m_edges, a, edges = generate_input(n)
    result = dinic(n_nodes, m_edges, a, edges)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)