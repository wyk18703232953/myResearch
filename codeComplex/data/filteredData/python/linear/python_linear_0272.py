import random

def tnnDecompositionFrom(tree, threeNeighborNode):
    paths = tuple(threeNeighborNode + node for node in tree if len(tree[node]) == 1)
    return f'Yes\n{len(paths)}\n' + '\n'.join(paths)


def decompositionFrom(tree):
    return 'Yes\n1\n' + ' '.join(node for node in tree if len(tree[node]) == 1)


def solve_from_tree(neighborsOf):
    threeNeighborNodeExists, threeNeighborNode = False, None

    for node in neighborsOf:
        if len(neighborsOf[node]) == 3:
            if threeNeighborNodeExists:
                return 'No'
            threeNeighborNodeExists, threeNeighborNode = True, node

    if threeNeighborNodeExists:
        return tnnDecompositionFrom(neighborsOf, threeNeighborNode + ' ')

    return decompositionFrom(neighborsOf)


def generate_random_tree(n):
    """
    生成一个 n 节点的随机树。
    节点为字符串 "1" 到 "n"。
    返回邻接表 neighborsOf: {node: [neighbors]}
    """
    neighborsOf = {str(i): [] for i in range(1, n + 1)}

    # 随机生成一棵树：对每个节点 i(2..n)，随机连接到 [1, i-1] 中某个节点
    for i in range(2, n + 1):
        u = str(i)
        v = str(random.randint(1, i - 1))
        neighborsOf[u].append(v)
        neighborsOf[v].append(u)

    return neighborsOf


def main(n):
    """
    n: 规模（节点数），n >= 1
    根据 n 生成一棵随机树，并运行原逻辑，返回输出字符串。
    """
    if n <= 0:
        return "No"

    neighborsOf = generate_random_tree(n)
    return solve_from_tree(neighborsOf)


if __name__ == '__main__':
    # 示例：规模为 5
    print(main(5))