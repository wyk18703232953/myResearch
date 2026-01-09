def main(n):
    # n: number of vertices
    # Map input size n to a graph with n vertices and m edges deterministically.
    # Here we construct a directed graph:
    # - A main cycle 0 -> 1 -> ... -> n-1 -> 0  (n edges)
    # - Plus extra edges forming a forward chain to create more in-degrees:
    #   for i in 0..n-2: i -> i+1 (already in cycle except last one), and an extra wrap
    # Total edges m ~ 2n (but exact value determined by construction).
    if n <= 0:
        return

    # Build edges deterministically
    edges = []
    # Main cycle
    for i in range(n):
        u = i
        v = (i + 1) % n
        edges.append((u, v))
    # Extra forward edges (avoid duplicating exact cycle edges by shifting)
    for i in range(n):
        u = i
        v = (i + 2) % n
        edges.append((u, v))

    m = len(edges)

    # Initialize global-like structures as in original code
    adj = [[] for _ in range(n)]
    rev = [[] for _ in range(n)]
    deg = [0] * n

    for u, v in edges:
        adj[u].append(v)
        rev[v].append(u)
        deg[v] += 1

    def prepare():
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

    def solve(st):
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

    ok = prepare()
    if ok:
        # print('YES')
        pass
        return

    m_eff = len([1 for i in range(n) if deg[i] > 0])
    for i in range(n):
        if deg[i] == 1 and solve(i):
            # print('YES')
            pass
            return

    # print('NO')
    pass
if __name__ == "__main__":
    # Example deterministic calls for time complexity experiments
    for size in (10, 100, 1000):
        main(size)