def match(p, s):
    for a, b in zip(p, s):
        if a != '_' and a != b:
            return False
    return True

def toposort(graph):
    res, found = [], [0] * len(graph)
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            res.append(~node)
        elif not found[node]:
            found[node] = 1
            stack.append(~node)
            stack += graph[node]
    for node in res:
        if any(found[nei] for nei in graph[node]):
            return None
        found[node] = 0
    return res[::-1]

def main(n):
    from itertools import product

    if n < 1:
        n = 1
    k = 3
    m = n
    # generate patterns P: n patterns, each of length k
    P = []
    for i in range(n):
        chars = []
        for pos in range(k):
            val = (i + pos) % 27
            if val == 26:
                chars.append('_')
            else:
                chars.append(chr(ord('a') + val))
        P.append(''.join(chars))

    # mapping for later index lookup
    index_of = {p: idx for idx, p in enumerate(P)}

    # generate S: m queries (string, index)
    S = []
    for q in range(m):
        idx = q % n
        base = P[idx]
        chars = []
        for pos, c in enumerate(base):
            if c == '_':
                chars.append('a')
            else:
                if (q + pos) % 3 == 0:
                    chars.append(c)
                else:
                    chars.append(c)
        s = ''.join(chars)
        S.append((s, idx))

    G = [[] for _ in range(n)]
    for s, i in S:
        if not match(P[i], s):
            print("NO")
            return
        for mask in product(range(2), repeat=k):
            sp = ['_' if bit else c for bit, c in zip(mask, s)]
            sp = ''.join(sp)
            if sp in index_of:
                j = index_of[sp]
                if i != j:
                    G[i].append(j)

    tp = toposort(G)
    if tp is None:
        print("NO")
    else:
        print("YES")
        print(*[x + 1 for x in tp])

if __name__ == "__main__":
    main(5)