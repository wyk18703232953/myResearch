from collections import deque

def main(n):
    # Ensure n >= 2 because original code uses nodes 0 and 1 and reads n-1 edges
    if n < 2:
        n = 2

    # Deterministically build a tree-like graph with n+1 nodes: 0..n
    # Make 0-1 edge as in original, then chain 1-2-3-...-n
    graph = [set() for _ in range(n + 1)]
    graph[0].add(1)
    graph[1].add(0)
    for i in range(1, n):
        x = i
        y = i + 1
        graph[x].add(y)
        graph[y].add(x)

    # Deterministically build a sequence 'a' that should be accepted by the algorithm:
    # It performs a BFS-like traversal: starting from node 0, neighbors in increasing order.
    # So we generate BFS order from node 0 with neighbors sorted.
    tmp_graph = [neighbors.copy() for neighbors in graph]
    q = deque([0])
    par = [-1] * (n + 1)
    bfs_order = []
    while q:
        v = q.popleft()
        bfs_order.append(v)
        # remove parent to simulate the same behavior
        if par[v] != -1:
            tmp_graph[v].discard(par[v])
        children = sorted(tmp_graph[v])
        for u in children:
            if par[u] == -1 and u != 0:
                par[u] = v
                q.append(u)

    # In the original code, 'a' is the list read from input.
    # To keep the logic, we set a to the bfs_order excluding the initial 0
    # because the algorithm starts with q=[0] and then expects neighbors in 'a'.
    a = bfs_order[1:]

    # Now run the original algorithm logic with this deterministic graph and a
    q = deque()
    q.append(0)
    i = 0
    par = [0] * (n + 1)
    result = None
    while len(q):
        v = q.popleft()
        graph[v].discard(par[v])
        l = len(graph[v])
        if graph[v] != set(a[i:i + l]):
            result = "No"
            break
        for j in range(i, i + l):
            q.append(a[j])
            par[a[j]] = v
        i += l

    else:
        result = "Yes"

    # print(result)
    pass
if __name__ == "__main__":
    main(10)