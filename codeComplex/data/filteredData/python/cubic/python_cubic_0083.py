def matching(n, m, path):
    match1 = [-1] * n
    match2 = [-1] * m
    for node in range(n):
        for nei in path[node]:
            if match2[nei] == -1:
                match1[node] = nei
                match2[nei] = node
                break
    while 1:
        bfs = [node for node in range(n) if match1[node] == -1]
        depth = [-1] * n
        for node in bfs:
            depth[node] = 0

        for node in bfs:
            for nei in path[node]:
                next_node = match2[nei]
                if next_node == -1:
                    break
                if depth[next_node] == -1:
                    depth[next_node] = depth[node] + 1
                    bfs.append(next_node)

            else:
                continue
            break

        else:
            break
        pointer = [len(c) for c in path]
        dfs = [node for node in range(n) if depth[node] == 0]
        while dfs:
            node = dfs[-1]
            while pointer[node]:
                pointer[node] -= 1
                nei = path[node][pointer[node]]
                next_node = match2[nei]
                if next_node == -1:
                    while nei != -1:
                        node = dfs.pop()
                        match2[nei], match1[node], nei = node, nei, match1[node]
                    break
                elif depth[node] + 1 == depth[next_node]:
                    dfs.append(next_node)
                    break

            else:
                dfs.pop()
    return n - match1.count(-1)


def experiment(n, m, edges):
    ans = float("inf")
    for centre in range(n):
        path = [[] for _ in range(n)]
        cost = 2 * n - 1
        extra = m
        for u, v in edges:
            if u == centre or v == centre:
                cost -= 1
                extra -= 1

            else:
                path[u].append(v)
        maxMatch = matching(n, n, path)
        extra -= maxMatch
        cost += n - 1 - maxMatch + extra
        ans = min(ans, cost)
    return ans


def generate_data(n):
    if n <= 1:
        n_nodes = 1
        edges = []
        return n_nodes, len(edges), edges

    n_nodes = n
    edges = []
    # deterministic edge generation: layered structure with some wrap-arounds
    for u in range(n_nodes):
        v1 = (u + 1) % n_nodes
        v2 = (u * 2 + 1) % n_nodes
        if u != v1:
            edges.append((u, v1))
        if u != v2 and v2 != v1:
            edges.append((u, v2))
    # clip to reasonable multiple to keep density bounded
    max_m = 3 * n_nodes
    edges = edges[:max_m]
    return n_nodes, len(edges), edges


def main(n):
    n_nodes, m, edges = generate_data(n)
    result = experiment(n_nodes, m, edges)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)