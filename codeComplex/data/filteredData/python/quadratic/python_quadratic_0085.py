def detect_cycle(n, edges):
    visited = [False] * n
    stack = []
    color = [0] * n
    for v in range(n):
        if not visited[v]:
            if dfs_visit(v, edges, visited, stack, color):
                return stack
    return None

def dfs_visit(v, edges, visited, stack, color):
    visited[v] = True
    stack.append(v)
    color[v] = 1
    for u in edges[v]:
        if not visited[u]:
            if dfs_visit(u, edges, visited, stack, color):
                return True
        elif color[u] == 1:
            stack.append(u)
            return True
    color[v] = 2
    stack.pop(stack.index(v))
    return False

def build_graph(n):
    # Deterministically build a graph with n nodes and O(n) edges.
    # Pattern:
    # - 0->1->2->...->n-1 (a path)
    # - If n >= 3, add one back edge to create a cycle:
    #   (i % (n-1)) -> (i+2) % (n-1) for i from 0 to n-3, then connect (n-2)->(1)
    edges = [[] for _ in range(n)]
    if n <= 1:
        return edges
    # Path edges
    for i in range(n - 1):
        edges[i].append(i + 1)
    # Additional edges creating cycles in a deterministic way
    if n >= 3:
        for i in range(n - 2):
            u = i
            v = (i + 2) % (n - 1)
            if v not in edges[u]:
                edges[u].append(v)
    return edges

def main(n):
    if n < 1:
        # print("YES")
        pass
        return
    edges = build_graph(n)
    inCycle = detect_cycle(n, edges)
    if inCycle:
        possible = False
        index = inCycle.index(inCycle[-1])
        inCycle = inCycle[index:]
        for v in range(len(inCycle) - 1):
            edges[inCycle[v]].remove(inCycle[v + 1])
            if detect_cycle(n, edges) is None:
                possible = True
                break

            else:
                edges[inCycle[v]].append(inCycle[v + 1])

    else:
        possible = True
    # print('YES' if possible else 'NO')
    pass
if __name__ == "__main__":
    main(10)