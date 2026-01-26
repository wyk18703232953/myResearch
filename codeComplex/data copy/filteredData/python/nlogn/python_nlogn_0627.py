from collections import deque

def main(n):
    # 构造一个确定性的树，并给出 k
    # 这里构造一棵完全三叉树风格的“多层星形”结构：
    # 0 为根，每层每个节点连到三个新节点，直到用完 n 个节点
    # 这样层数和 n 有一个确定关系，可用于不同 n 做复杂度实验

    if n < 2:
        # 对于 n 太小的情况，构造最小的树并设置 k=0
        k = 0
        graph = [set() for _ in range(1)]

    else:
        graph = [set() for _ in range(n)]
        current = 1
        parent = 0
        layer_nodes = [0]
        next_layer_nodes = []
        # 构造一个“每个节点最多连 3 个子节点”的树
        while current < n and layer_nodes:
            next_layer_nodes = []
            for parent in layer_nodes:
                for _ in range(3):
                    if current >= n:
                        break
                    graph[parent].add(current)
                    graph[current].add(parent)
                    next_layer_nodes.append(current)
                    current += 1
                if current >= n:
                    break
            layer_nodes = next_layer_nodes

        # 估计 k 为树的大致“层数减一”，用来测试不同 n 下的表现
        # 层数近似为按 1,3,9,... 的几何级数累积到 >= n 的层数
        total = 1
        layer = 0
        while total < n:
            layer += 1
            total += 3**layer
        k = layer - 1
        if k < 0:
            k = 0

    # 以下保持原算法逻辑不变
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
            center = next(iter(graph[leaf]))
            graph[leaf].remove(center)

            try:
                centers[center] += 1
            except KeyError:
                centers[center] = 1

            graph[center].remove(leaf)

            if len(graph[center]) == 0:
                valid = False
                break
            elif len(graph[center]) == 1:
                new_leafs.append(center)

        if not valid:
            break

        if any(mult < 3 for mult in centers.values()):
            valid = False
            break

        count = count + 1
        leafs = new_leafs
        new_leafs = []
        centers = {}

    if valid and count == k:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(1000)