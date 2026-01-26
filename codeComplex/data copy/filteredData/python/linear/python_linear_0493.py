def get_new_edges(graph):
    n = len(graph)
    far_vertex = []
    pi = [None] * n
    visit = [False] * n
    queue = [[0, 0]]
    i = 0
    while True:
        if i >= len(queue):
            break
        current, d = queue[i]
        i += 1
        visit[current] = True
        for v in graph[current]:
            if not visit[v]:
                u = [v, d + 1]
                pi[v] = current
                queue.append(u)
                if d + 1 > 2:
                    far_vertex.append(u)

    far_vertex.sort(key=lambda x: -x[1])

    pos = [None] * n
    for i, e in enumerate(far_vertex):
        pos[e[0]] = i

    count = 0
    for i in range(len(far_vertex)):
        if not far_vertex[i]:
            continue
        vertex, depth = far_vertex[i]
        father = pi[vertex]
        count += 1
        if pos[father]:
            far_vertex[pos[father]] = None
        for u in graph[father]:
            if pos[u]:
                far_vertex[pos[u]] = None

    return count


def build_graph(n):
    # Build a deterministic tree with n vertices.
    # Edges: connect i with i//2 for i from 2 to n (1-based),
    # then convert to 0-based indices.
    if n <= 0:
        return []
    graph = [[] for _ in range(n)]
    for i in range(2, n + 1):
        parent = i // 2
        v1 = i - 1      # child (0-based)
        v2 = parent - 1 # parent (0-based)
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph


def main(n):
    # n is the number of vertices in the tree
    graph = build_graph(n)
    result = get_new_edges(graph)
    # print(result)
    pass
if __name__ == "__main__":
    # Example: run main with a chosen input scale
    main(10)