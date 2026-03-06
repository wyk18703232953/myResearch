def main(n):
    from collections import deque

    # Interpret n as number of patterns (original n), and also scale m and k
    # Deterministic scaling: let m = n, k = min(10, max(1, n % 10 + 1))
    orig_n = n
    k = min(10, max(1, n % 10 + 1))
    m = n

    # Generate p: list of orig_n strings of length k over 'a'..'d'
    # Deterministic pattern based on index
    p = []
    for i in range(orig_n):
        s = []
        x = i
        for j in range(k):
            s.append(chr(ord('a') + (x % 4)))
            x //= 4
        p.append(''.join(s))

    idx = {s: i for i, s in enumerate(p)}

    def match(s):
        res = []
        for i in range(2 ** k):
            tmp = []
            for j in range(k):
                if i >> j & 1:
                    tmp.append(s[j])
                else:
                    tmp.append("_")
            res.append("".join(tmp))
        return set(res)

    # Generate m queries (s, mt)
    # We will generate s based on the target pattern p[mt] with deterministic modifications
    queries = []
    for i in range(m):
        # mt in [0, orig_n-1]
        mt = i % orig_n
        base = p[mt]
        # Create s by replacing some positions with another letter deterministically
        s_chars = list(base)
        for pos in range(k):
            if (i + pos) % 3 == 0:
                # change character in a cyclic deterministic way
                s_chars[pos] = chr(ord('a') + ((ord(s_chars[pos]) - ord('a') + 1) % 4))
        s = ''.join(s_chars)
        # Ensure sometimes s equals target pattern to allow matches
        if i % 5 == 0:
            s = base
        queries.append((s, mt + 1))  # mt+1 to mimic original 1-based input

    edge = [[] for _ in range(orig_n)]
    deg = [0] * orig_n

    for i in range(m):
        s, mt = queries[i]
        mt = int(mt) - 1
        t = p[mt]
        M = match(s)
        if t in M:
            for nv in M:
                if nv != t and nv in idx:
                    nv_idx = idx[nv]
                    edge[mt].append(nv_idx)
                    deg[nv_idx] += 1
        else:
            print("NO")
            return

    deq = deque([v for v in range(orig_n) if deg[v] == 0])
    res = []
    while deq:
        v = deq.popleft()
        res.append(v + 1)
        for nv in edge[v]:
            deg[nv] -= 1
            if deg[nv] == 0:
                deq.append(nv)

    if len(res) != orig_n:
        print("NO")
        return

    print("YES")
    print(*res)


if __name__ == "__main__":
    main(5)