from collections import deque
import random

def main(n):
    # n: number of "item" nodes (original variable n)
    # We will generate:
    #   m = n edges in the first layer (original variable m)
    #   a: length-n list of capacities from item nodes to T
    #
    # Graph structure follows the original code:
    #   Nodes: 0 ... m+n+1
    #   S = 0
    #   Edge nodes: 1..m
    #   Item nodes: m+1..m+n
    #   T = m+n+1

    global e, lvl, S, T, inf

    # parameters for random test generation
    m = n
    max_w = 10**6
    max_a = 10**6

    # generate random a[0..n-1]
    a = [random.randint(1, max_a) for _ in range(n)]

    # generate m edges (u, v, w)
    # u, v are item indices in [1, n], w is weight
    edges = []
    for _ in range(m):
        u = random.randint(1, n)
        v = random.randint(1, n)
        w = random.randint(1, max_w)
        edges.append((u, v, w))

    inf = 2 * (10 ** 12)
    ans = 0
    e = [[] for _ in range(n + m + 2)]
    S, T = 0, m + n + 1

    def addedge(u, v, value):
        global e
        a1 = [v, value, None]
        b1 = [u, 0, a1]
        a1[2] = b1
        e[u].append(a1)
        e[v].append(b1)

    # build graph as in original program
    for i in range(1, m + 1):
        u, v, w = edges[i - 1]
        ans += w
        addedge(i, u + m, inf)
        addedge(i, v + m, inf)
        addedge(S, i, w)
    for i in range(m + 1, T):
        addedge(i, T, a[i - m - 1])

    lvl = None

    def bfs():
        nonlocal lvl
        lvl = [0] * (n + m + 2)
        q = deque([S])
        while q:
            node = q.popleft()
            for edge in e[node]:
                if edge[0] != S and lvl[edge[0]] == 0 and edge[1]:
                    lvl[edge[0]] = lvl[node] + 1
                    q.append(edge[0])

    def dfs(node, maxdelta):
        if node == T:
            return maxdelta
        delta = 0
        for edge in e[node]:
            if lvl[edge[0]] == lvl[node] + 1 and edge[1]:
                tmp = dfs(edge[0], min(maxdelta, edge[1]))
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
        bfs()
        tmp = dfs(S, inf)
        if tmp == 0:
            break
        flow += tmp
    ans -= flow
    print(ans)


if __name__ == "__main__":
    # example: run with n=5
    main(5)