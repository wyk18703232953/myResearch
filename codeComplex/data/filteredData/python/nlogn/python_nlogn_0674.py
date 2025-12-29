import random
from operator import itemgetter


def topological_sort(E, D):
    D = D[:]  # copy
    n = len(E)
    Q = [i for i in range(n) if D[i] == 0]
    L = []
    while Q:
        p = Q.pop()
        L.append(p)
        for vf in E[p]:
            D[vf] -= 1
            if D[vf] == 0:
                Q.append(vf)

    if len(L) != n:
        return False
    return L


def main(n):
    """
    n: number of vertices (scale of the problem)
    The function generates a random directed graph with M edges
    and then runs the original algorithm logic on it.
    """

    N = n
    # Generate a reasonably dense graph but avoid too large M
    # M in [N-1, min(N*(N-1)/2, N^2)]
    max_possible = N * (N - 1) // 2
    if max_possible == 0:
        # Degenerate case: N <= 1
        print(0, 0)
        print()
        return

    # Choose M proportional to N, but not exceeding the maximum simple DAG edges
    # We'll generate a random DAG by using a topological order
    M = min(max_possible, max(N - 1, 2 * N))

    # Generate a random topological order for vertices 0..N-1
    topo = list(range(N))
    random.shuffle(topo)
    pos = [0] * N
    for i, v in enumerate(topo):
        pos[v] = i

    edges = set()
    # Ensure at least a spanning structure (N-1 edges)
    for i in range(N - 1):
        u = topo[i]
        v = topo[i + 1]
        edges.add((u, v))

    # Add remaining edges randomly, keeping DAG property (u before v in topo)
    while len(edges) < M:
        u_idx = random.randint(0, N - 2)
        v_idx = random.randint(u_idx + 1, N - 1)
        u = topo[u_idx]
        v = topo[v_idx]
        edges.add((u, v))

    # Assign random weights c to edges (1..10^9)
    Edge = []
    m_id = 1
    for (a, b) in edges:
        c = random.randint(1, 10**9)
        Edge.append((c, m_id, a, b))
        m_id += 1

    M = len(Edge)  # in case set deduped some

    # Original logic starts here
    Edge.sort(key=itemgetter(0), reverse=True)

    ok = 0
    ng = M + 1
    while abs(ok - ng) > 1:
        med = (ok + ng) // 2
        Edge2 = [[] for _ in range(N)]
        Dim2 = [0] * N
        for i in range(med):
            _, _, a, b = Edge[i]
            Edge2[a].append(b)
            Dim2[b] += 1
        if topological_sort(Edge2, Dim2):
            ok = med
        else:
            ng = med

    Edge2 = [[] for _ in range(N)]
    Dim = [0] * N
    for i in range(ok):
        _, _, a, b = Edge[i]
        Edge2[a].append(b)
        Dim[b] += 1

    L = topological_sort(Edge2, Dim)
    Linv = [None] * N
    for i in range(N):
        Linv[L[i]] = i

    Ans = []
    ans = 0
    if ok < M:
        ans = Edge[ok][0]
        for i in range(ok, M):
            c, m, a, b = Edge[i]
            if Linv[a] > Linv[b]:
                Ans.append(m)

    print(ans, len(Ans))
    if Ans:
        print(*Ans)
    else:
        print()


if __name__ == "__main__":
    # Example: run with n = 10
    main(10)