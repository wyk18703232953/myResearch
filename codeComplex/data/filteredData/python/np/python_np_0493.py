import sys

def deterministic_patterns(N, K):
    P = []
    D_P = {}
    for i in range(N):
        s_chars = []
        for j in range(K):
            # Simple deterministic pattern: cycle through 'a'..'z' then 'A'..'Z'
            base = (i + j) % 52
            if base < 26:
                ch = chr(ord('a') + base)
            else:
                ch = chr(ord('A') + (base - 26))
            s_chars.append(ch)
        s = ''.join(s_chars)
        P.append(s)
        D_P[s] = i
    return P, D_P

def deterministic_queries(M, N, K, P):
    queries = []
    for q in range(M):
        mt = q % N
        fp = P[mt]
        s_chars = []
        for i in range(K):
            # Flip case deterministically based on query index and position
            if (q + i) % 3 == 0:
                s_chars.append('_')
            else:
                ch = fp[i]
                if 'a' <= ch <= 'z':
                    s_chars.append(chr(ord('A') + (ord(ch) - ord('a'))))
                elif 'A' <= ch <= 'Z':
                    s_chars.append(chr(ord('a') + (ord(ch) - ord('A'))))
                else:
                    s_chars.append(ch)
        S = ''.join(s_chars)
        queries.append((S, mt))
    return queries

def run_algorithm(N, M, K, P, D_P, queries):
    adj = [[] for _ in range(N)]
    indeg = [0] * N

    for S, mt in queries:
        fp = P[mt]

        if any(fp[i] not in (S[i], '_') for i in range(K)):
            return False, []

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
        return True, Q
    else:
        return False, []

def main(n):
    # Map n to problem dimensions
    if n < 1:
        n = 1
    K = max(1, n // 3)
    N = max(1, n // 2)
    M = max(1, n)

    P, D_P = deterministic_patterns(N, K)
    queries = deterministic_queries(M, N, K, P)
    ok, order = run_algorithm(N, M, K, P, D_P, queries)

    if ok:
        print('YES')
        print(' '.join(str(v + 1) for v in order))
    else:
        print('NO')

if __name__ == "__main__":
    main(10)