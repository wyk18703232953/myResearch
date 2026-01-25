def main(n):
    # Interpret n as the number of vertices; edges are deterministically generated.
    # We generate a directed graph with vertices 1..n and edges:
    #   for i in 1..n:
    #       j = (i * 2) % n + 1
    #       if i != j: add edge i -> j
    # This ensures a non-trivial but deterministic structure.
    if n < 1:
        return

    digraph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        j = (i * 2) % n + 1
        if i != j:
            digraph[i].append(j)

    cicle = dfs(digraph)
    if cicle is None:
        print("YES")
    else:
        cicle.reverse()
        for i in range(len(cicle) - 1):
            c = dfs(digraph, cicle[i], cicle[i + 1])
            if c is None:
                print("YES")
                break
        else:
            print("NO")


def dfs(graph, u=-1, v=-1):
    n = len(graph)
    pi = [None] * n
    color = ['white'] * n
    for node in range(1, n):
        if color[node] == 'white':
            cicle = dfs_visit(graph, node, color, pi, u, v)
            if cicle is not None:
                return cicle
    return None


def dfs_visit(graph, root, color, pi, u, v):
    stack = [root]

    while stack:
        current_node = stack[-1]

        if color[current_node] != 'white':
            stack.pop()
            color[current_node] = 'black'
            continue

        color[current_node] = 'grey'
        for adj in graph[current_node]:
            if (current_node, adj) == (u, v):
                continue

            if color[adj] == 'white':
                pi[adj] = current_node
                stack.append(adj)
            elif color[adj] == 'grey':
                cicle = [adj]
                while current_node != adj:
                    cicle.append(current_node)
                    current_node = pi[current_node]
                cicle.append(adj)
                return cicle
    return None


if __name__ == "__main__":
    main(10)