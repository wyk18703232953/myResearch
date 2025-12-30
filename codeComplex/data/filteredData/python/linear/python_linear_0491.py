import random
from collections import deque
import heapq


def solve(N, EDGE):
    EDGELIST = [[] for _ in range(N + 1)]

    for i, j in EDGE:
        EDGELIST[i].append(j)
        EDGELIST[j].append(i)

    REDG = [None for _ in range(N + 1)]
    QUE = deque([1])
    check = [0] * (N + 1)
    DEPTH = [None] * (N + 1)
    depth_val = 0

    while QUE:
        NQUE = deque()
        depth_val += 1

        while QUE:
            x = QUE.pop()
            DEPTH[x] = depth_val
            check[x] = 1
            for to in EDGELIST[x]:
                if check[to] == 1:
                    continue
                else:
                    REDG[to] = x
                    NQUE.append(to)
        QUE = NQUE

    check = [0] * (N + 1)
    check[1] = 1

    LEAF = []
    for i in range(2, N + 1):
        if len(EDGELIST[i]) == 1:
            LEAF.append((-DEPTH[i], i))

    QUE = LEAF
    heapq.heapify(QUE)
    ANS = 0

    while QUE:
        dep, x = heapq.heappop(QUE)
        if check[x] != 0 or dep >= -3:
            continue

        if check[REDG[x]] == 2:
            continue

        if check[x] == 0:
            check[x] = 1
        if check[REDG[REDG[x]]] == 0:
            check[REDG[REDG[x]]] = 1
        check[REDG[x]] = 2
        heapq.heappush(
            QUE,
            (-DEPTH[REDG[REDG[REDG[x]]]], REDG[REDG[REDG[x]]])
        )
        ANS += 1

    return ANS


def generate_tree_edges(n):
    """生成一棵随机树的边列表，节点编号为 1..n。"""
    edges = []
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)
        edges.append((u, v))
    return edges


def main(n):
    # 生成规模为 n 的测试数据（随机树）
    N = n
    EDGE = generate_tree_edges(N)

    ans = solve(N, EDGE)
    print(ans)


if __name__ == "__main__":
    # 示例：运行 main(10)。实际使用时可修改 n。
    main(10)