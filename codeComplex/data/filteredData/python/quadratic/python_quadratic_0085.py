import random

def detect_cycle(n, edges):
    visited = [False] * n
    stack = []
    color = [0] * n  # 0: unvisited, 1: visiting, 2: visited
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

def generate_test_graph(n):
    """
    根据规模 n 生成测试数据：
    - 顶点数 = n
    - 随机生成有向边，数量约为 n 到 2n 之间
    - 顶点编号为 0..n-1
    """
    edges = [[] for _ in range(n)]
    if n <= 1:
        return edges

    # 控制边数在 [n, 2n] 范围内（若可能）
    max_possible_edges = n * (n - 1)  # 有向图不允许自环时的最大边数
    m = random.randint(min(n, max_possible_edges), min(2 * n, max_possible_edges))

    all_pairs = [(u, v) for u in range(n) for v in range(n) if u != v]
    random.shuffle(all_pairs)

    for i in range(m):
        u, v = all_pairs[i]
        edges[u].append(v)

    return edges

def main(n):
    # 生成测试图
    edges = generate_test_graph(n)

    inCycle = detect_cycle(n, edges)
    if inCycle:
        possible = False
        index = inCycle.index(inCycle[-1])
        inCycle = inCycle[index:]
        for v in range(len(inCycle) - 1):
            # 尝试删除环上的一条边，看能否变为无环图
            if inCycle[v + 1] in edges[inCycle[v]]:
                edges[inCycle[v]].remove(inCycle[v + 1])
            if detect_cycle(n, edges) is None:
                possible = True
                break
            else:
                # 恢复边
                edges[inCycle[v]].append(inCycle[v + 1])
    else:
        possible = True

    print('YES' if possible else 'NO')

if __name__ == "__main__":
    # 示例运行：可根据需要修改规模
    main(5)