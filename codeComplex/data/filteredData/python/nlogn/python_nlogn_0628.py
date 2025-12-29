from collections import deque
import random

def bfs(graph, s, k):
    n = len(graph)
    Q = deque()
    Q.append(s)

    infinite = 10 ** 6
    d = [infinite] * n
    parent = [-1] * n
    valid = True

    d[s] = 0

    while Q:
        u = Q.popleft()
        not_visited_count = 0

        for v in graph[u]:
            if d[v] == infinite:
                d[v] = d[u] + 1
                parent[v] = u
                Q.append(v)
                not_visited_count += 1

        if not_visited_count < 3 and d[u] != k:
            valid = False

    return d, parent, valid


def generate_tree(n):
    """
    生成一棵随机树（n >= 1），返回邻接表 graph 和一个随机的 k。
    k 的选择保证直径大致可用：取 1..(n//2) 中的随机值。
    """
    if n == 1:
        return [[]], 0

    graph = [[] for _ in range(n)]
    # 随机生成一棵树：逐点与前面任意一个点连边
    for v in range(1, n):
        u = random.randint(0, v - 1)
        graph[u].append(v)
        graph[v].append(u)

    # k 取 1..(n//2)，避免过大
    k = random.randint(1, max(1, n // 2))
    return graph, k


def main(n):
    # 1. 生成测试数据
    graph, k = generate_tree(n)

    # 2. 找一个叶子
    leaf = -1
    for i, v in enumerate(graph):
        if len(v) == 1 or n == 1:  # n==1 时唯一点算作“叶子”
            leaf = i
            break

    if leaf == -1:
        print("NO")
        return

    # 3. 从 leaf 做 BFS
    d, parent, _ = bfs(graph, leaf, k)
    center = -1
    farthest_leaf = -1
    diameter = 2 * k

    for i, level in enumerate(d):
        if level == diameter:
            farthest_leaf = i
            break

    if farthest_leaf == -1 or len(graph[farthest_leaf]) != 1:
        print("NO")
        return

    # 4. 沿着 parent 走 k 步找到 center
    for _ in range(k):
        center = parent[farthest_leaf]
        farthest_leaf = center

    if center == -1:
        print("NO")
        return

    # 5. 以 center 再次 BFS 验证
    _, _, valid = bfs(graph, center, k)

    if valid:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main，n 为规模
    main(10)