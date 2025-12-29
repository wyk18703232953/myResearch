from collections import defaultdict
import random


def solve(n, k, edges):
    graph = [set() for _ in range(n)]

    for a, b in edges:
        a -= 1
        b -= 1
        graph[a].add(b)
        graph[b].add(a)

    leafs = [i for i, v in enumerate(graph) if len(v) == 1]
    new_leafs = []
    valid = True
    centers = dict()
    count = 0

    while len(leafs) > 1 and valid:
        for leaf in leafs:
            if not graph[leaf]:
                valid = False
                break
            center = graph[leaf].pop()

            centers[center] = centers.get(center, 0) + 1

            if leaf in graph[center]:
                graph[center].remove(leaf)

            if len(graph[center]) == 0:
                break
            elif len(graph[center]) == 1:
                new_leafs.append(center)

        if not valid:
            break

        if any(mult < 3 for mult in centers.values()):
            valid = False
            break

        count += 1
        leafs = new_leafs
        new_leafs = []
        centers = {}

    return "YES" if valid and count == k else "NO"


def generate_tree_edges(n):
    # 生成一棵随机树：将每个节点(2..n)随机连接到前面的某个节点
    edges = []
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)
        edges.append((u, v))
    return edges


def main(n):
    random.seed(0)
    # 生成测试参数 k，可根据需要调整策略
    # 这里简单设定为 1 到 n//2 之间的随机值（至少为 1）
    k = random.randint(1, max(1, n // 2))

    edges = generate_tree_edges(n)
    result = solve(n, k, edges)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)