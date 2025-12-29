from collections import defaultdict
import random
import sys

sys.setrecursionlimit(500000)


def countleaf(tree, n, leafs):
    leafs[n] = 1 if len(tree[n]) == 0 else 0
    for i in tree[n]:
        leafs[n] += countleaf(tree, i, leafs)
    return leafs[n]


def generate_tree_edges(n):
    # 生成一棵以 0 为根、1..n-1 为其他节点的随机树
    # 对应原代码中的 edges: 对于 i from 1..n-1, edges[i-1] = 父节点编号(1-based)
    edges = []
    for child in range(1, n):
        parent = random.randint(0, child - 1)  # 保证无环，形成树
        edges.append(parent + 1)               # 转成 1-based
    return edges


def main(n):
    # 生成测试数据：含 n 个节点的树
    # 节点编号 0..n-1，其中 0 为根
    if n <= 0:
        return

    edges = generate_tree_edges(n)

    tree = [[] for _ in range(n)]
    leafs = [0] * n

    # 使用生成的 edges 构建树（与原程序逻辑一致）
    for i, e in enumerate(edges):
        tree[e - 1].append(i + 1)

    # 自底向上计算叶子数（与原程序逻辑一致）
    for i in range(n - 1, -1, -1):
        if not tree[i]:
            leafs[i] = 1
        else:
            leafs[i] = sum(leafs[j] for j in tree[i])

    # 输出结果
    print(*sorted(leafs))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)