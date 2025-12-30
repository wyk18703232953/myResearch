from collections import deque
import random

def bfs(G, s, k, n):
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

        for v in G[u]:
            if d[v] == infinite:
                d[v] = d[u] + 1
                parent[v] = u
                Q.append(v)
                not_visited_count += 1

        if not_visited_count < 3 and d[u] != k:
            valid = False

    return d, parent, valid


def generate_tree(n):
    """生成一棵随机树，点编号 0..n-1"""
    if n == 1:
        return [[]]
    graph = [[] for _ in range(n)]
    # 随机生成一棵树：每个新节点连到前面某个节点
    for i in range(1, n):
        p = random.randrange(0, i)
        graph[p].append(i)
        graph[i].append(p)
    return graph


def main(n):
    # 为了保持与原逻辑相近，生成一个 k，并生成一棵树
    # 这里简单设定 k 为 1 到 n//2 之间的一个合法值
    if n <= 2:
        k = 1
    else:
        k = random.randint(1, max(1, n // 2))

    graph = generate_tree(n)

    # 找一个叶子
    leaf = -1
    for i, v in enumerate(graph):
        if len(v) == 1:
            leaf = i
            break

    if leaf == -1:
        print("NO")
        return

    d, parent, _ = bfs(graph, leaf, k, n)
    center = -1
    farthest_leaf = -1
    path = 2 * k

    for i, level in enumerate(d):
        if level == path:
            farthest_leaf = i
            break

    if farthest_leaf == -1 or len(graph[farthest_leaf]) != 1:
        print("NO")
        return

    for _ in range(k):
        center = parent[farthest_leaf]
        farthest_leaf = center

    _, _, valid = bfs(graph, center, k, n)

    if valid:
        print("YES")
    else:
        print("NO")


# 示例：直接运行时给一个默认规模
if __name__ == "__main__":
    main(10)