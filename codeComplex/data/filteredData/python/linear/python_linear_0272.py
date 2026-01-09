def main(n):
    # n represents the number of nodes in the tree
    if n < 2:
        # Original code assumes a tree with at least 2 nodes (nNodes, then nNodes-1 edges)
        # For n < 2, we define a degenerate behavior: no edges, single node or empty.
        # To keep structure similar, handle n == 1 separately.
        if n == 1:
            neighborsOf = {"1": []}
            return decompositionFrom(neighborsOf)

        else:
            return "Yes\n0\n"

    nNodes = n

    # Deterministically generate a tree with nNodes nodes labeled "1" .. str(nNodes)
    # We also deterministically create exactly one node of degree 3 when nNodes >= 5:
    #   - Node "1" connects to "2","3","4" (degree 3)
    #   - Remaining nodes form a chain starting from "4": 4-5-6-...-nNodes
    # This ensures predictable structure and presence of a degree-3 node for n >= 5.
    neighborsOf = {node: [] for node in map(str, range(1, nNodes + 1))}
    threeNeighborNodeExists, threeNeighborNode = False, None

    edges = []
    if nNodes == 2:
        edges.append(("1", "2"))
    elif nNodes == 3:
        edges.append(("1", "2"))
        edges.append(("2", "3"))
    elif nNodes == 4:
        edges.append(("1", "2"))
        edges.append(("2", "3"))
        edges.append(("3", "4"))

    else:
        # nNodes >= 5
        edges.append(("1", "2"))
        edges.append(("1", "3"))
        edges.append(("1", "4"))
        for i in range(4, nNodes):
            edges.append((str(i), str(i + 1)))

    for node1, node2 in edges:
        neighborsOf[node1].append(node2)
        neighborsOf[node2].append(node1)
        if len(neighborsOf[node1]) == 3:
            if threeNeighborNodeExists and threeNeighborNode != node1:
                return "No"
            threeNeighborNodeExists, threeNeighborNode = True, node1
        if len(neighborsOf[node2]) == 3:
            if threeNeighborNodeExists and threeNeighborNode != node2:
                return "No"
            threeNeighborNodeExists, threeNeighborNode = True, node2

    if threeNeighborNodeExists:
        return tnnDecompositionFrom(neighborsOf, threeNeighborNode + " ")

    return decompositionFrom(neighborsOf)


def tnnDecompositionFrom(tree, threeNeighborNode):
    paths = tuple(threeNeighborNode + node for node in tree if len(tree[node]) == 1)
    return f"Yes\n{len(paths)}\n" + "\n".join(paths)


def decompositionFrom(tree):
    return "Yes\n1\n" + " ".join(node for node in tree if len(tree[node]) == 1)


if __name__ == "__main__":
    # Example deterministic call for testing / timing
    # print(main(10))
    pass