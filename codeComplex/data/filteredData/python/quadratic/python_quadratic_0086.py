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
    # 构造一个确定性的有向图：
    # 顶点数 = n
    # 边数约为 n（每个点指向 (i+1) mod n，形成一个大环）
    # 当 n >= 2 时，图中一定有环
    if n <= 0:
        # print("YES")
        pass
        return

    m = n  # 边数
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
    # print('YES' if possible else 'NO')
    pass
if __name__ == "__main__":
    main(10)