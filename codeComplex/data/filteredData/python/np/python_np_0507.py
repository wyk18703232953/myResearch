mod = 1000000007
eps = 10**-9


def generate_input(n):
    if n <= 0:
        N = 1
    else:
        N = n
    K = max(1, (N % 5) + 1)
    # Generate N distinct patterns of length K using letters 'a'..'z'
    P = [""]
    for i in range(1, N + 1):
        x = i
        s = []
        for j in range(K):
            s.append(chr(ord('a') + (x + j) % 26))
        P.append("".join(s))
    # Build deterministic edges
    M = 0
    edges = []
    for mt in range(1, N + 1):
        s = P[mt]
        mask = (mt % (1 << K))
        s_list = list(s)
        for j in range(K):
            if (mask >> j) & 1:
                s_list[j] = '_'
        s_new = "".join(s_list)
        edges.append((s, mt))
        M += 1
    return N, M, K, P, edges


def main(n):
    N, M, K, P, edges = generate_input(n)
    p2i = {p: i for i, p in enumerate(P)}
    adj = [set() for _ in range(N + 1)]
    for s, mt in edges:
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
    main(5)