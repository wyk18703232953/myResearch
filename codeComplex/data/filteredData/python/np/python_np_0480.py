import sys
from collections import deque

def match(s, k):
    res = []
    for i in range(2**k):
        tmp = []
        for j in range(k):
            if (i >> j) & 1:
                tmp.append(s[j])
            else:
                tmp.append("_")
        res.append("".join(tmp))
    return set(res)

def main(n):
    # Deterministic data generation based on n
    # Interpret n as number of patterns and queries
    k = 4  # fixed pattern length
    m = n  # number of queries
    p = []
    for i in range(n):
        # generate deterministic k-length strings over 'a', 'b'
        s = []
        x = i
        for j in range(k):
            s.append(chr(ord('a') + (x & 1)))
            x >>= 1
        p.append("".join(s))
    idx = {s: i for i, s in enumerate(p)}

    # build queries (s, mt)
    queries = []
    for i in range(m):
        mt = (i * 7 + 3) % n  # deterministic index in [0, n-1]
        base = p[mt]
        # deterministically create a mask string s from base
        # use '_' for some positions, base char for others
        chars = []
        for j in range(k):
            if ((i + j) % 3) == 0:
                chars.append("_")
            else:
                chars.append(base[j])
        s = "".join(chars)
        queries.append((s, mt))

    edge = [[] for _ in range(n)]
    deg = [0] * n

    for s, mt in queries:
        t = p[mt]
        M = match(s, k)
        if t in M:
            for nv in M:
                if nv != t and nv in idx:
                    nv_idx = idx[nv]
                    edge[mt].append(nv_idx)
                    deg[nv_idx] += 1
        else:
            print("NO")
            return

    deq = deque([v for v in range(n) if deg[v] == 0])
    res = []
    while deq:
        v = deq.popleft()
        res.append(v + 1)
        for nv in edge[v]:
            deg[nv] -= 1
            if deg[nv] == 0:
                deq.append(nv)

    if len(res) != n:
        print("NO")
        return

    print("YES")
    print(*res)

if __name__ == "__main__":
    main(5)