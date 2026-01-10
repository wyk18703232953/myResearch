def main(n):
    from collections import deque

    # Ensure n is at least 3 to form a non-trivial tree and k >= 1
    if n < 3:
        n = 3

    # Deterministically choose k based on n
    # Make sure 2*k <= n-1 so the diameter we want is feasible
    k = max(1, min((n - 1) // 2, n // 3))
    diameter = 2 * k

    # Build a deterministic tree of size n
    # We'll build a "path + branches" tree:
    # - First create a main path of length = diameter
    # - Attach remaining nodes as extra leaves to the center to satisfy branching
    graph = [[] for _ in range(n)]

    # Create main path 0 - 1 - 2 - ... - diameter
    path_len = min(diameter, n - 1)
    for i in range(path_len):
        u = i
        v = i + 1
        graph[u].append(v)
        graph[v].append(u)

    # Ensure diameter path uses nodes [0..diameter], if n is enough
    # Remaining nodes attach to the center of path (node k)
    center_candidate = k if k <= path_len else path_len // 2
    next_node = path_len + 1
    while next_node < n:
        u = center_candidate
        v = next_node
        graph[u].append(v)
        graph[v].append(u)
        next_node += 1

    def bfs(G, s, n_local, k_local):
        Q = deque()
        Q.append(s)
        infinite = 10 ** 6
        d = [infinite] * n_local
        parent = [-1] * n_local
        valid = True
        d[s] = 0

        while Q:
            u = Q.popleft()
            not_visited_count = 0
            for v in G[u]:
                if d[v] == infinite:
                    d[v] = d[u] + 1
                    parent[v] = u
                    Q.append(v)
                    not_visited_count += 1
            if not_visited_count < 3 and d[u] != k_local:
                valid = False

        return d, parent, valid

    # Find a leaf deterministically: smallest index with degree 1
    leaf = -1
    for i, v in enumerate(graph):
        if len(v) == 1:
            leaf = i
            break

    if leaf == -1:
        print("NO")
        return

    d, parent, _ = bfs(graph, leaf, n, k)
    farthest_leaf = -1
    for i, level in enumerate(d):
        if level == diameter:
            farthest_leaf = i
            break

    if farthest_leaf == -1 or len(graph[farthest_leaf]) != 1:
        print("NO")
        return

    center = -1
    for _ in range(k):
        center = parent[farthest_leaf]
        farthest_leaf = center

    if center == -1:
        print("NO")
        return

    _, _, valid = bfs(graph, center, n, k)

    if valid:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)