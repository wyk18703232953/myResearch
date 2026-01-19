def main(n):
    # Interpret n as N (number of patterns), with M=N and K up to 10 for complexity
    if n <= 0:
        return
    K = 5 if n < 20 else 10
    N = n
    M = n

    # Deterministic generation of S (N strings of length K over 'a','b','_')
    # Pattern: cycle through alphabet with '_' inserted every 3rd position
    chars = ['a', 'b', '_']
    S = []
    for i in range(N):
        s = []
        base = i
        for j in range(K):
            idx = (base + j * 2) % len(chars)
            s.append(chars[idx])
        S.append(''.join(s))

    # Build dictionary from patterns to index
    D = {}
    for i in range(N):
        D[S[i]] = i

    # Deterministic generation of queries T: each is [pattern, index]
    # We generate patterns based on S with some controlled modifications so that
    # they are often compatible with S[index].
    T = []
    for i in range(M):
        idx = i % N
        base_pattern = S[idx]
        t_chars = []
        for j in range(K):
            c = base_pattern[j]
            if c == '_':
                # Deterministically choose a or b based on i,j
                t_chars.append('a' if (i + j) % 2 == 0 else 'b')
            else:
                # Keep original char
                t_chars.append(c)
        T.append([''.join(t_chars), idx + 1])

    G = [[] for _ in range(N)]
    C = [0] * N

    # Original algorithm logic
    for i in range(M):
        T[i][1] = int(T[i][1]) - 1
    for i in range(M):
        # Check compatibility
        ok = True
        s_idx = T[i][1]
        for j in range(K):
            if S[s_idx][j] != '_' and S[s_idx][j] != T[i][0][j]:
                ok = False
                break
        if not ok:
            print('NO')
            return
        # Build edges
        for j in range(1 << K):
            t = ''.join(['_' if j & (1 << k) else T[i][0][k] for k in range(K)])
            x = D.get(t, -1)
            if x != -1 and x != s_idx:
                G[s_idx].append(x)
                C[x] += 1

    P = []
    Q = []
    F = [1] * N
    for i in range(N):
        if C[i] == 0 and F[i]:
            Q.append(i)
        while len(Q):
            v = Q.pop()
            if not F[v]:
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
    # Example deterministic call; adjust n as needed for experiments
    main(10)