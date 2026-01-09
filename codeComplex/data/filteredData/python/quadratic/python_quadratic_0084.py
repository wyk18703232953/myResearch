def get_deterministic_graph(n):
    # Construct a directed graph with n nodes and O(n) edges deterministically.
    # Node indices: 1..n
    # Edges: i -> i+1 for i in 1..n-1 (a path)
    # Additionally, for i multiple of 3, add edge i -> max(1, i-2)
    # This guarantees at least one cycle for n >= 3.
    digraph = [[] for _ in range(n + 1)]
    if n <= 1:
        return digraph

    # Path edges
    for i in range(1, n):
        digraph[i].append(i + 1)

    # Extra edges creating cycles
    for i in range(3, n + 1, 3):
        to_node = i - 2
        if to_node >= 1:
            digraph[i].append(to_node)

    return digraph


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


def main(n):
    digraph = get_deterministic_graph(n)
    cicle = dfs(digraph)
    if cicle is None:
        # print("YES")
        pass

    else:
        cicle.reverse()
        for i in range(len(cicle) - 1):
            c = dfs(digraph, cicle[i], cicle[i + 1])
            if c is None:
                # print("YES")
                pass
                break

        else:
            # print("NO")
            pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different input scales
    main(10)