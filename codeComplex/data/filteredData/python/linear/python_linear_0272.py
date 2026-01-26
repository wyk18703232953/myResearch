def tnnDecompositionFrom(tree, threeNeighborNode):
    paths = tuple(threeNeighborNode + node for node in tree if len(tree[node]) == 1)
    return f'Yes\n{len(paths)}\n' + '\n'.join(paths)


def decompositionFrom(tree):
    return 'Yes\n1\n' + ' '.join(node for node in tree if len(tree[node]) == 1)


def main(n):
    # Generate a deterministic tree with n nodes.
    # Node labels are "1".."n" as in the original program.
    if n <= 0:
        return "Yes\n0\n"

    # neighborsOf: adjacency list using string node labels
    neighborsOf = {str(node): [] for node in range(1, n + 1)}

    # Construct a deterministic tree structure.
    # For n < 4: use a simple path (no degree-3 node).
    # For n >= 4: build a tree where node "1" has degree 3:
    #   edges (1,2), (1,3), (1,4) form the 3 neighbors;
    #   remaining nodes (5..n) are attached in a chain starting from 2.
    edges = []
    if n == 1:
        edges = []
    elif n == 2:
        edges = [(1, 2)]
    elif n == 3:
        edges = [(1, 2), (2, 3)]

    else:
        # base star at node 1
        edges = [(1, 2), (1, 3), (1, 4)]
        # attach remaining nodes as a path from node 2
        current = 2
        for node in range(5, n + 1):
            edges.append((current, node))
            current = node

    # Fill adjacency lists
    threeNeighborNodeExists, threeNeighborNode = False, None
    for u, v in edges:
        node1, node2 = str(u), str(v)
        neighborsOf[node1].append(node2)
        neighborsOf[node2].append(node1)
        if len(neighborsOf[node1]) == 3:
            if threeNeighborNodeExists:
                return 'No'
            threeNeighborNodeExists, threeNeighborNode = True, node1
        elif len(neighborsOf[node2]) == 3:
            if threeNeighborNodeExists:
                return 'No'
            threeNeighborNodeExists, threeNeighborNode = True, node2

    if threeNeighborNodeExists:
        return tnnDecompositionFrom(neighborsOf, threeNeighborNode + ' ')

    return decompositionFrom(neighborsOf)


if __name__ == "__main__":
    # Example deterministic call
    # print(main(10))
    pass