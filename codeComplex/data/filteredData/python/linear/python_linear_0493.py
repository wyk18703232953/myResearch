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


def main(n):
    if n < 2:
        graph = [[] for _ in range(max(n, 1))]
        result = get_new_edges(graph)
        # print(result)
        pass
        return

    # Deterministic tree generation with n vertices (0 to n-1)
    # Parent of i (i >= 1) is i // 2
    graph = [[] for _ in range(n)]
    for i in range(1, n):
        p = i // 2
        graph[p].append(i)
        graph[i].append(p)

    result = get_new_edges(graph)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)