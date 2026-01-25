import heapq
from collections import deque

def generate_tree_edges(N):
    edges = []
    for i in range(2, N + 1):
        p = i // 2
        if p < 1:
            p = 1
        edges.append([p, i])
    return edges

def solve(N, EDGE):
    EDGELIST = [[] for _ in range(N + 1)]
    for i, j in EDGE:
        EDGELIST[i].append(j)
        EDGELIST[j].append(i)

    REDG = [None for _ in range(N + 1)]
    QUE = deque([1])
    check = [0] * (N + 1)
    DEPTH = [None] * (N + 1)
    depth_level = 0

    while QUE:
        NQUE = deque()
        depth_level += 1
        while QUE:
            x = QUE.pop()
            DEPTH[x] = depth_level
            check[x] = 1
            for to in EDGELIST[x]:
                if check[to] == 1:
                    continue
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
        if REDG[REDG[x]] is not None and check[REDG[REDG[x]]] == 0:
            check[REDG[REDG[x]]] = 1
        check[REDG[x]] = 2
        r3 = REDG[REDG[REDG[x]]] if REDG[x] is not None and REDG[REDG[x]] is not None else 1
        heapq.heappush(QUE, (-DEPTH[r3], r3))
        ANS += 1

    return ANS

def main(n):
    if n < 2:
        N = 2
    else:
        N = n
    EDGE = generate_tree_edges(N)
    ans = solve(N, EDGE)
    print(ans)

if __name__ == "__main__":
    main(10)