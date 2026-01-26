from collections import defaultdict
import heapq


def generate_tree(n):
    if n <= 1:
        return [[] for _ in range(n)]
    a = [[] for _ in range(n)]
    # Generate a simple chain tree: 1-2-3-...-n
    for i in range(1, n):
        u = i - 1
        v = i
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
    while len(stack) > 0:
        crt = stack[-1]
        if visited[crt]:
            stack.pop(-1)
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


def main(n):
    a = generate_tree(n)

    if n == 0:
        # print("")
        pass
        return
    if n == 1:
        # print("1")
        pass
        return

    leaves = [i for i in range(n) if len(a[i]) == 1]

    first_choice = leaves[0]
    d1, child1 = dfs_from(first_choice, a)

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

    while len(pq) > 0:
        _, best = heapq.heappop(pq)
        if seen[best]:
            continue
        c = best
        s = 0
        while c != -1:
            seen[c] = True
            c = child[c]
            s = s + 1
        s = s + solution[-1]
        solution.append(s)

    for _ in range(n - min(len(solution), n)):
        solution.append(n)

    # print(' '.join(str(s) for s in solution))
    pass
if __name__ == "__main__":
    main(10)