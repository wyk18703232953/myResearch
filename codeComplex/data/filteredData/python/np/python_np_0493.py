def main(n):
    # n controls the pattern length K and number of patterns/queries
    # Define sizes deterministically from n
    K = max(1, n // 4)          # pattern length
    N = max(1, n // 2)          # number of patterns
    M = max(1, n)               # number of queries

    # Generate N distinct patterns of length K over alphabet {'a','b','c','_'}
    # Ensure determinism via simple arithmetic
    alphabet = ['a', 'b', 'c', '_']
    P = []
    D_P = {}
    for i in range(N):
        # deterministic pattern based on i and K
        s = []
        x = i
        for pos in range(K):
            ch = alphabet[(x + pos) % 4]
            s.append(ch)
            x //= 2
        pat = ''.join(s)
        # ensure uniqueness by appending index if collision happens
        if pat in D_P:
            pat = pat[:-1] + alphabet[(i + 1) % 4]
        P.append(pat)
        D_P[pat] = i

    # Generate M queries (S, mtIndex) deterministically
    # Try to often create valid queries: S that matches P[mt] with extra '_'
    queries = []
    for q in range(M):
        mt = q % N
        base = P[mt]
        s_list = []
        # Construct S by combining base with a deterministic pattern of '_'
        for i in range(K):
            if (q + i) % 5 == 0:
                s_list.append('_')
            else:
                s_list.append(base[i])
        S = ''.join(s_list)
        queries.append((S, mt + 1))  # mt is 1-based in original input

    # Core algorithm (unchanged logic, but without I/O)
    adj = [[] for _ in range(N)]
    indeg = [0] * N

    for S, mt in queries:
        mt = mt - 1
        fp = P[mt]

        if any(fp[i] not in (S[i], '_') for i in range(K)):
            print('NO')
            return

        for bs in range(1 << K):
            pat_chars = []
            for i in range(K):
                if bs & (1 << i) == 0:
                    pat_chars.append(S[i])
                else:
                    pat_chars.append('_')
            pat = ''.join(pat_chars)
            if pat == fp:
                continue
            if pat in D_P:
                j = D_P[pat]
                indeg[j] += 1
                adj[mt].append(j)

    Q = [i for i in range(N) if indeg[i] == 0]
    for i in Q:
        for j in adj[i]:
            indeg[j] -= 1
            if indeg[j] == 0:
                Q.append(j)

    if len(Q) == N:
        print('YES')
        print(' '.join(str(v + 1) for v in Q))
    else:
        print('NO')


if __name__ == "__main__":
    main(16)