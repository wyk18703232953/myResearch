import random

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
    global deep, S, T, he, e
    deep = [0 for _ in range(T + 1)]
    q = [S]
    deep[S] = 1
    while q:
        x = q.pop(0)
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
    """
    n: number of left-side nodes
    We generate:
      - m = n random hyper edges
      - random weights for n nodes and m hyper edges
    """
    global e, tot, S, T, he, INF, deep

    # Parameterization: choose m as a function of n
    m = n  # can be adjusted as needed

    # Generate node weights: 1..10
    weight = [0] + [random.randint(1, 10) for _ in range(n)]

    # Initialize graph
    e = [0, 0]
    tot = 1
    S = n + m + 1
    T = S + 1
    he = [0 for _ in range(T + 1)]
    INF = 10**9 + 7
    deep = []

    ans = 0

    # Edges from S to left nodes
    for i in range(1, n + 1):
        addedge(S, i, weight[i])

    # Generate m hyper edges, each connects two distinct left nodes x,y
    # and has capacity w from hyper node to T
    for i in range(1, m + 1):
        x = random.randint(1, n)
        y = random.randint(1, n)
        while y == x:
            y = random.randint(1, n)
        w = random.randint(1, 10)
        addedge(n + i, T, w)
        addedge(x, n + i, INF)
        addedge(y, n + i, INF)
        ans += w

    ans -= dinic()
    print(ans)


if __name__ == "__main__":
    # Example call; adjust n as needed
    main(5)