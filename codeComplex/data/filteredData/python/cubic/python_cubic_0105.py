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
    global deep, T, S, he, e
    deep = [0 for _ in range(T + 1)]
    q = [S]
    deep[S] = 1
    lp = 0
    while lp < len(q):
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
    """
    n: problem size, we will generate:
       - n vertices on the left
       - m = n vertices on the right (hyper-edges)
    The graph structure follows the original program:
       S -> i (capacity = weight[i])
       n + j -> T (capacity = w_j)
       x_j -> n + j (capacity = INF)
       y_j -> n + j (capacity = INF)
    """
    global e, tot, S, T, he, INF, deep

    random.seed(0)

    m = n  # choose m proportional to n

    # Generate weights for left side vertices: 1..n
    weight = [0] + [random.randint(1, 10) for _ in range(n)]

    # Generate m triples (x, y, w) with 1 <= x, y <= n, x != y
    edges_data = []
    for _ in range(m):
        x = random.randint(1, n)
        y = random.randint(1, n)
        while y == x:
            y = random.randint(1, n)
        w = random.randint(1, 10)
        edges_data.append((x, y, w))

    # Initialize global structures
    e = [0, 0]
    tot = 1
    S = n + m + 1
    T = S + 1
    he = [0 for _ in range(T + 1)]
    INF = 1000000007

    ans = 0

    # S -> i
    for i in range(1, n + 1):
        addedge(S, i, weight[i])

    # hyper edges
    for i in range(1, m + 1):
        x, y, w = edges_data[i - 1]
        addedge(n + i, T, w)
        addedge(x, n + i, INF)
        addedge(y, n + i, INF)
        ans += w

    ans -= dinic()
    print(ans)

if __name__ == "__main__":
    # example: run with n = 5
    main(5)