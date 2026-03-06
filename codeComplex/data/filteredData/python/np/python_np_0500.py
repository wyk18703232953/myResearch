def main(n):
    # Interpret n as:
    # K: pattern length
    # N: number of strings
    # M: number of queries
    # For scalability and determinism:
    K = max(1, n % 7 + 1)          # pattern length between 1 and 8
    N = max(1, n * 3)              # number of strings
    M = max(1, n * 2)              # number of queries

    # Generate N distinct pattern strings of length K over 'a'..'d' and '_'
    # Deterministic generation by counting in base 5 (4 letters + '_')
    alphabet = ['a', 'b', 'c', 'd', '_']

    def idx_to_pattern(idx, length):
        s = []
        for _ in range(length):
            s.append(alphabet[idx % 5])
            idx //= 5
        return ''.join(s)

    # Ensure we have at least N unique patterns by deterministic mapping
    S = [idx_to_pattern(i, K) for i in range(N)]
    # Make sure there is at least some '_' in patterns for edges
    if K > 1:
        for i in range(N):
            if all(ch != '_' for ch in S[i]):
                # deterministically place an '_' at position depending on i
                pos = i % K
                S[i] = S[i][:pos] + '_' + S[i][pos + 1:]

    # Build dictionary from pattern to index
    D = {S[i]: i for i in range(N)]

    # Generate M queries T: each is (query_pattern, index)
    # We try to generate patterns that are close to S[index] so constraints are not immediately violated
    T = []
    for i in range(M):
        idx = i % N
        base = S[idx]
        # Create a query string by modifying characters deterministically
        q_chars = []
        for j in range(K):
            c = base[j]
            if c == '_':
                # map '_' to a letter based on (i + j)
                q_chars.append(alphabet[(i + j) % 4])
            else:
                # sometimes keep same, sometimes shift
                if (i + j) % 3 == 0:
                    q_chars.append(c)
                else:
                    q_chars.append(alphabet[(ord(c) - ord('a') + 1) % 4])
        q = ''.join(q_chars)
        T.append([q, idx])

    # Core logic from original program
    G = [[] for _ in range(N)]
    C = [0] * N
    for i in range(M):
        # feasibility check
        si = S[T[i][1]]
        qi = T[i][0]
        for j in range(K):
            if si[j] != '_' and si[j] != qi[j]:
                print('NO')
                return
        # generate all masks
        for mask in range(1 << K):
            t_chars = []
            for k in range(K):
                if mask & (1 << k):
                    t_chars.append('_')
                else:
                    t_chars.append(qi[k])
            t = ''.join(t_chars)
            x = D.get(t, -1)
            if x != -1 and x != T[i][1]:
                G[T[i][1]].append(x)
                C[x] += 1

    P = []
    Q = []
    F = [1] * N
    for i in range(N):
        if C[i] == 0 and F[i]:
            Q.append(i)
        while Q:
            v = Q.pop()
            if F[v] == 0:
                continue
            F[v] = 0
            P.append(v + 1)
            for to in G[v]:
                C[to] -= 1
                if C[to] == 0:
                    Q.append(to)

    if len(P) == N:
        print('YES')
        print(*P)
    else:
        print('NO')


if __name__ == "__main__":
    main(10)