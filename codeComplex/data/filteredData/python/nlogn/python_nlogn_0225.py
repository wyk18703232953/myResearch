from collections import defaultdict
import heapq
import random


def build_tree(n):
    """
    生成一棵随机树：
    - 节点编号 0..n-1
    - 返回邻接表 a
    """
    if n == 1:
        return [[]]

    a = [[] for _ in range(n)]
    # 随机生成一棵树：每个新节点连到一个已有节点
    for v in range(1, n):
        u = random.randint(0, v - 1)
        a[u].append(v)
        a[v].append(u)
    return a


def dfs_from(root, a):
    n = len(a)
    depth = defaultdict(int)
    child = {}
    parent = defaultdict(lambda: -1)
    stack = [root]
    visited = [False for _ in range(n)]
    while stack:
        crt = stack[-1]
        if visited[crt]:
            stack.pop()
            if len(a[crt]) > 1:  # not a leaf
                child[crt], depth[crt] = max(
                    [(c, depth[c] + 1) for c in a[crt] if c != parent[crt]],
                    key=lambda x: x[1]
                )
            else:
                child[crt] = -1
                depth[crt] = 0
            continue

        visited[crt] = True
        for nxt in a[crt]:
            if nxt != parent[crt]:
                stack.append(nxt)
                parent[nxt] = crt

    return depth, child


def main(n: int):
    # 1. 生成测试树
    a = build_tree(n)

    # 2. 原逻辑
    leaves = [i for i in range(n) if len(a[i]) == 1] if n > 1 else [0]

    first_choice = leaves[0]
    d1, child1 = dfs_from(first_choice, a)

    if n == 1:
        root = 0
    else:
        root = max(
            [(a[leaf][0], d1[a[leaf][0]]) for leaf in leaves],
            key=lambda leaf_depth: leaf_depth[1]
        )[0]
        while child1[root] != -1:
            root = child1[root]

    depth, child = dfs_from(root, a)

    solution = [1]
    pq = []
    for k, v in depth.items():
        heapq.heappush(pq, (-v, k))

    seen = [False for _ in range(n)]
    seen[root] = True

    while pq:
        _, best = heapq.heappop(pq)
        if seen[best]:
            continue
        c = best
        s = 0
        while c != -1:
            seen[c] = True
            c = child[c]
            s += 1
        s = s + solution[-1]
        solution.append(s)

    for _ in range(n - min(len(solution), n)):
        solution.append(n)

    print(' '.join(str(s) for s in solution))


if __name__ == "__main__":
    # 示例运行，可按需修改 n
    main(10)