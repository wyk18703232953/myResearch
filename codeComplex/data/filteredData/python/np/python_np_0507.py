mod = 1000000007
eps = 10**-9


def main(n):
    # n controls N, M, K
    # Ensure reasonable lower bounds
    if n < 1:
        n = 1

    # Define K as a small constant so 2^K is manageable and depends weakly on n
    K = 5
    # Number of patterns
    N = n
    # Number of edges (constraints)
    M = n

    # Deterministic generation of pattern strings P[1..N], each of length K over 'a'..'z'
    P = [""]
    for i in range(1, N + 1):
        s = []
        x = i
        for j in range(K):
            c = chr(ord('a') + (x + j) % 26)
            s.append(c)
        P.append("".join(s))

    p2i = {p: i for i, p in enumerate(P)}
    adj = [set() for _ in range(N + 1)]

    # Deterministic generation of M constraints (s, mt)
    # For repeatability, choose mt cycling through 1..N
    for i in range(M):
        mt = (i % N) + 1
        # Base string s derived from P[mt] but modified deterministically
        base = list(P[mt])
        # Flip characters at positions depending on i to create variety
        for j in range(K):
            if (i >> j) & 1:
                base[j] = chr(ord('a') + (ord(base[j]) - ord('a') + 1) % 26)
        s = "".join(base)

        ok = 0
        for k in range(1 << K):
            s_new = ["_"] * K
            for j in range(K):
                if k >> j & 1:
                    s_new[j] = s[j]
            s_new = "".join(s_new)
            if s_new != P[mt]:
                if s_new in p2i:
                    adj[mt].add(p2i[s_new])
            else:
                ok = 1
        if not ok:
            print("NO")
            return

    in_num = [0] * (N + 1)
    for v in range(1, N + 1):
        for u in adj[v]:
            in_num[u] += 1
    st = []
    for v in range(1, N + 1):
        if in_num[v] == 0:
            st.append(v)
    ans = []
    while st:
        v = st.pop()
        ans.append(v)
        for u in adj[v]:
            in_num[u] -= 1
            if in_num[u] == 0:
                st.append(u)
    if len(ans) == N:
        print("YES")
        print(*ans)
    else:
        print("NO")


if __name__ == "__main__":
    main(10)