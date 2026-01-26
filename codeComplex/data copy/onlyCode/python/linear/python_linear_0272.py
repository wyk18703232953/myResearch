# _
#####################################################################################################################

def main():
    nNodes = int(input())
    neighborsOf = {node: [] for node in map(str, range(1, nNodes+1))}
    threeNeighborNodeExists, threeNeighborNode = False, None
    for i in range(1, nNodes):
        node1, node2 = input().split()
        neighborsOf[node1].append(node2), neighborsOf[node2].append(node1)
        if len(neighborsOf[node1]) == 3:
            if threeNeighborNodeExists:
                return 'No'
            threeNeighborNodeExists, threeNeighborNode = True, node1
        elif len(neighborsOf[node2]) == 3:
            if threeNeighborNodeExists:
                return 'No'
            threeNeighborNodeExists, threeNeighborNode = True, node2

    if threeNeighborNodeExists:
        return tnnDecompositionFrom(neighborsOf, threeNeighborNode+' ')

    return decompositionFrom(neighborsOf)


def tnnDecompositionFrom(tree, threeNeighborNode):
    paths = tuple(threeNeighborNode + node for node in tree if len(tree[node]) == 1)
    return f'Yes\n{len(paths)}\n' + '\n'.join(paths)


def decompositionFrom(tree):
    return 'Yes\n1\n' + ' '.join(node for node in tree if len(tree[node]) == 1)


if __name__ == '__main__':
    print(main())
    # main()
