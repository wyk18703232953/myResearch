import random
from collections import deque

def get_new_edges(graph):
    n = len(graph)
    far_vertex = []
    pi = [None] * n
    visit = [False] * n
    queue = deque()
    queue.append((0, 0))  # (vertex, depth)

    while queue:
        current, d = queue.popleft()
        if visit[current]:
            continue
        visit[current] = True
        for v in graph[current]:
            if not visit[v]:
                pi[v] = current
                queue.append((v, d + 1))
                if d + 1 > 2:
                    far_vertex.append([v, d + 1])

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
        if father is not None and pos[father] is not None:
            far_vertex[pos[father]] = None
        for u in (graph[father] if father is not None else []):
            if pos[u] is not None:
                far_vertex[pos[u]] = None

    return count


def generate_tree(n, seed=0):
    """生成一个包含 n 个节点的随机树（无向连通无环图）"""
    random.seed(seed)
    graph = [[] for _ in range(n)]
    # 逐个节点连接到前面任一节点，保证连通且无环
    for v in range(1, n):
        u = random.randint(0, v - 1)
        graph[u].append(v)
        graph[v].append(u)
    return graph


def main(n):
    """
    n: 图的顶点数（规模）
    功能：生成一个规模为 n 的随机树，调用 get_new_edges，并打印结果。
    """
    if n <= 0:
        return
    graph = generate_tree(n)
    ans = get_new_edges(graph)
    print(ans)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)