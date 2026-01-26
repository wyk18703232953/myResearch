from collections import deque

def bfs(G, s, k, n):
    Q = deque()
    Q.append(s)

    infinite = 10 ** 6
    d = [infinite] * n
    parent = [-1] * n
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

        if not_visited_count < 3 and d[u] != k:
            valid = False

    return d, parent, valid


def generate_tree(n):
    # Generate a deterministic tree with n nodes (0..n-1)
    # Pattern: for i >= 1, parent is i//2
    graph = [[] for _ in range(n)]
    for i in range(1, n):
        p = i // 2
        graph[p].append(i)
        graph[i].append(p)
    return graph


def main(n):
    if n < 2:
        # For n < 2, behavior is trivial; just print NO to keep it defined
        # print("NO")
        pass
        return

    # Define k as a function of n; ensure 2*k is within a reasonable diameter
    k = max(1, n // 4)

    graph = generate_tree(n)

    leaf = -1
    for i, v in enumerate(graph):
        if len(v) == 1:
            leaf = i
            break

    if leaf == -1:
        # print("NO")
        pass
        return

    d, parent, _ = bfs(graph, leaf, k, n)
    center = -1
    farthest_leaf = -1
    path = 2 * k

    for i, level in enumerate(d):
        if level == path:
            farthest_leaf = i
            break

    if farthest_leaf == -1 or len(graph[farthest_leaf]) != 1:
        # print("NO")
        pass
        return

    for _ in range(k):
        center = parent[farthest_leaf]
        farthest_leaf = center

    _, _, valid = bfs(graph, center, k, n)

    if valid:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(1000)