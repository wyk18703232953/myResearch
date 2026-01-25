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

def main(n):
    if n < 2:
        n = 2
    m = n
    edges = [[] for _ in range(n)]
    for i in range(m):
        u = i % n
        v = (i + 1) % n
        edges[u].append(v)
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
    print('YES' if possible else 'NO')

if __name__ == "__main__":
    main(10)