import random

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

def generate_test_data(n):
    # 生成一个有向图：每个点随机连若干条边
    edges = [[] for _ in range(n)]
    # 边数上限设为 n*(n-1)，但实际生成较少，避免过密
    max_edges = min(n * (n - 1), 3 * n)
    m = random.randint(n, max_edges) if n > 1 else 0
    all_pairs = [(u, v) for u in range(n) for v in range(n) if u != v]
    random.shuffle(all_pairs)
    for i in range(min(m, len(all_pairs))):
        u, v = all_pairs[i]
        edges[u].append(v)
    return edges

def main(n):
    edges = generate_test_data(n)

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

if __name__ == '__main__':
    # 示例：规模 n=10，可按需修改
    main(10)