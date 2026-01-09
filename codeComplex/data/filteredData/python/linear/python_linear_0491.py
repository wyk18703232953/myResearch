import sys
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
        if REDG[REDG[x]] is not None and check[REDG[REDG[x]]] == 0:
            check[REDG[REDG[x]]] = 1
        check[REDG[x]] = 2

        grand = REDG[REDG[REDG[x]]] if REDG[x] is not None and REDG[REDG[x]] is not None else None
        if grand is not None:
            heapq.heappush(QUE, (-DEPTH[grand], grand))
        ANS += 1

    return ANS

def generate_tree_edges(N):
    # Deterministic tree generation: a simple chain 1-2-3-...-N
    # This gives N-1 edges as required
    return [[i, i + 1] for i in range(1, N)]

def main(n):
    # Map n to tree size N
    # Ensure N >= 2 for the original logic (which expects N-1 edges)
    N = max(2, n)
    EDGE = generate_tree_edges(N)
    ans = solve(N, EDGE)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)