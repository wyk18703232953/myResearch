from collections import defaultdict
import random


def solve_tree(graph, k):
    n = len(graph)
    leafs = [i for i, v in enumerate(graph) if len(v) == 1]
    new_leafs = []
    valid = True
    centers = dict()
    count = 0

    while len(leafs) > 1 and valid:
        for leaf in leafs:
            if not graph[leaf]:
                continue
            center = graph[leaf].pop()

            try:
                centers[center] += 1
            except KeyError:
                centers[center] = 1

            graph[center].remove(leaf)

            if len(graph[center]) == 0:
                break
            elif len(graph[center]) == 1:
                new_leafs.append(center)

        if any(mult < 3 for mult in centers.values()):
            valid = False
            break

        count += 1
        leafs = new_leafs
        new_leafs = []
        centers = {}

    return "YES" if valid and count == k else "NO"


def generate_tree_edges(n, rng):
    # 生成一棵随机树：从 2..n 每个点连到前面任意一点
    edges = []
    for v in range(2, n + 1):
        u = rng.randint(1, v - 1)
        edges.append((u, v))
    return edges


def main(n):
    """
    n: 问题规模，用于控制生成的树节点数和参数 k
    行为：
      - 生成一棵规模为 n 的随机树
      - 随机生成 0 <= k <= n
      - 按原算法逻辑输出 YES 或 NO
    """
    if n < 2:
        # 原算法要求 n >= 2 才有 n-1 条边，这里做个简单处理
        print("NO")
        return

    rng = random.Random(0)  # 固定种子保证复现性

    # 生成随机 k，范围可按需要调整
    k = rng.randint(0, n)

    # 生成随机树边
    edges = generate_tree_edges(n, rng)

    # 构建图（0-based）
    graph = [set() for _ in range(n)]
    for a, b in edges:
        a -= 1
        b -= 1
        graph[a].add(b)
        graph[b].add(a)

    # 调用核心逻辑
    result = solve_tree(graph, k)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)