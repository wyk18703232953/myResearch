def parse(s, i):
    i = int(i) - 1
    return s, i

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

def generate_input(n):
    if n < 1:
        n = 1
    k = max(1, n // 3)
    m = max(1, n // 2)
    # generate pattern strings P
    P = []
    for i in range(n):
        s_chars = []
        for j in range(k):
            # deterministic character pattern
            val = (i * (j + 1) + j) % 3
            if val == 0:
                s_chars.append('a')
            elif val == 1:
                s_chars.append('b')
            else:
                s_chars.append('_')
        P.append(''.join(s_chars))
    # build index mapping like original
    index_of = {p: i for i, p in enumerate(P)}
    # generate queries S as list of (string, index+1) for parse compatibility
    S = []
    for q in range(m):
        idx = q % n
        p = P[idx]
        s_chars = []
        for j, ch in enumerate(p):
            if ch == '_':
                base_char = chr(ord('a') + ((idx + j) % 3))
                s_chars.append(base_char)
            else:
                # sometimes keep, sometimes tweak deterministically
                if ((idx + j + q) % 4) == 0:
                    s_chars.append(ch)
                else:
                    s_chars.append(ch)
        s = ''.join(s_chars)
        S.append((s, str(idx + 1)))
    return n, m, k, P, S

def main(n):
    from itertools import product
    n, m, k, P, raw_S = generate_input(n)
    S = [parse(s, i) for s, i in raw_S]
    index_of = dict()
    for i, p in enumerate(P):
        index_of[p] = i
    G = [[] for _ in range(n)]
    for s, i in S:
        if not match(P[i], s):
            print("NO")
            return
        for mask in product(range(2), repeat=k):
            sp = ['_' if bit else c for bit, c in zip(mask, s)]
            sp = ''.join(sp)
            try:
                j = index_of[sp]
                if i != j:
                    G[i].append(j)
            except KeyError:
                pass
    tp = toposort(G)
    if tp is None:
        print("NO")
    else:
        print("YES")
        print(*[x + 1 for x in tp])

if __name__ == "__main__":
    main(6)