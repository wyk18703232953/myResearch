import sys


def prepare(n, m, adj, deg):
    stack = [i for i in range(n) if deg[i] == 0]
    cnt = 0
    while stack:
        v = stack.pop()
        cnt += 1
        for dest in adj[v]:
            deg[dest] -= 1
            if deg[dest] == 0:
                stack.append(dest)
        adj[v].clear()
    return cnt == n


def solve(st, n, m, adj, deg):
    stack = [st]
    visited = [0] * n
    cnt = 0
    while stack:
        v = stack.pop()
        cnt += 1
        for dest in adj[v]:
            if dest == st:
                continue
            visited[dest] += 1
            if deg[dest] == visited[dest]:
                stack.append(dest)
    return cnt == m


def generate_graph(n):
    # Deterministic graph generation for given n
    # We create a directed graph on n nodes with m edges.
    # Pattern:
    # - A path 0 -> 1 -> 2 -> ... -> n-1
    # - Additional edges i -> (i+2) % n for even i to increase in-degree variety
    adj = [[] for _ in range(n)]
    deg = [0] * n

    # Path edges
    for i in range(n - 1):
        adj[i].append(i + 1)
        deg[i + 1] += 1

    # Extra edges
    for i in range(0, n, 2):
        j = (i + 2) % n
        if j != i and j not in adj[i]:
            adj[i].append(j)
            deg[j] += 1

    m = sum(len(row) for row in adj)
    return n, m, adj, deg


def main(n):
    if n <= 0:
        return

    n, m, adj, deg = generate_graph(n)

    ok = prepare(n, m, adj, deg)
    if ok:
        # print("YES")
        pass
        return

    m_pos = len([1 for i in range(n) if deg[i] > 0])
    for i in range(n):
        if deg[i] == 1 and solve(i, n, m_pos, adj, deg):
            # print("YES")
            pass
            return

    # print("NO")
    pass
if __name__ == "__main__":
    main(10)