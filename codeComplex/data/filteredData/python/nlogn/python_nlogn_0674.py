def topological_sort(E, D):
    D = D[:]
    n = len(E)
    Q = [i for i in range(n) if D[i] == 0]
    L = []
    while Q:
        p = Q.pop()
        L.append(p)
        for vf in E[p]:
            D[vf] -= 1
            if not D[vf]:
                Q.append(vf)
    if len(L) != n:
        return False
    return L

def main(n):
    # Deterministic generation of N, M and edges based on n
    if n <= 0:
        print(0, 0)
        print()
        return

    N = n
    M = n * 2

    Edge = [None] * M
    for m in range(M):
        # generate a, b in [0, N-1], avoid self-loop by construction
        a = m % N
        b = (m * 2 + 1) % N
        c = (m * 3 + 7) % (n + 5)
        Edge[m] = (c, m + 1, a, b)

    from operator import itemgetter
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
    main(10)