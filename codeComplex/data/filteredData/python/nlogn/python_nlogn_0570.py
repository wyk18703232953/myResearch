def countleaf(tree, n, leafs):
    leafs[n] = 1 if len(tree[n]) == 0 else 0
    for i in tree[n]:
        leafs[n] += countleaf(tree, i, leafs)
    return leafs[n]


def main(n):
    if n <= 0:
        return

    # 确定性构造 edges：父节点为 (i // 2) + 1，根的父设为 1（但不会用到）
    edges = [(i // 2) + 1 for i in range(n - 1)]

    tree = [[] for _ in range(n)]
    leafs = [0] * n

    for i, e in enumerate(edges):
        tree[e - 1].append(i + 1)

    for i in range(n - 1, -1, -1):
        if not tree[i]:
            leafs[i] = 1

        else:
            leafs[i] = sum(leafs[j] for j in tree[i])

    # print(*sorted(leafs))
    pass
if __name__ == "__main__":
    main(10)