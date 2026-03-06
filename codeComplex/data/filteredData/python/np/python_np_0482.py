def toposort(graph):
    res = []
    found = [0] * len(graph)
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


def solve(N, M, K, P, S, MT):
    graph = [[] for _ in range(N)]

    def isMatch(s, pattern):
        for a, b in zip(s, pattern):
            if b != "_" and a != b:
                return False
        return True

    ordA = ord("a") - 1

    def hashStr(s):
        hsh = 0
        for c in s:
            val = 27 if c == "_" else ord(c) - ordA
            hsh = 32 * hsh + val
        return hsh

    patternToId = {}
    for i, p in enumerate(P):
        patternToId[hashStr(p)] = i

    for s, mt in zip(S, MT):
        if not isMatch(s, P[mt]):
            return "NO"
        vals = [ord(c) - ordA for c in s]
        for mask in range(1 << K):
            hsh = 0
            for pos in range(K):
                val = 27 if (1 << pos) & mask else vals[pos]
                hsh = 32 * hsh + val
            if hsh in patternToId:
                mt2 = patternToId[hsh]
                if mt2 != mt:
                    graph[mt].append(mt2)

    ans = toposort(graph)
    if ans is None:
        return "NO"
    return "YES\n" + " ".join(str(i + 1) for i in ans)


def main(n):
    # Map n to problem size:
    # Let N = n (number of patterns)
    # Let K = max(1, n % 6 + 1) (pattern length between 2 and 7)
    # Let M = n (number of strings)
    N = max(1, n)
    K = max(1, n % 6 + 1)
    M = N

    # Deterministic generation of patterns P (length K each)
    # Characters cycle through 'a'..'z' and '_' based on indices
    alphabet = [chr(ord('a') + i) for i in range(26)] + ['_']
    P = []
    for i in range(N):
        s_chars = []
        base = i
        for j in range(K):
            idx = (base + j * 7) % len(alphabet)
            s_chars.append(alphabet[idx])
        P.append("".join(s_chars))

    # Deterministic generation of S and MT (each S[i] matches P[MT[i]])
    S = []
    MT = []
    for i in range(M):
        mt = i % N
        pattern = P[mt]
        s_chars = []
        for j, c in enumerate(pattern):
            if c == "_":
                # replace wildcard deterministically with a letter
                s_chars.append(alphabet[(i + j * 3) % 26])
            else:
                # sometimes keep, sometimes shift deterministically but keep match
                shift = (i + j) % 2
                if shift == 0:
                    s_chars.append(c)
                else:
                    # still must match pattern; so keep c
                    s_chars.append(c)
        S.append("".join(s_chars))
        MT.append(mt)

    result = solve(N, M, K, P, S, MT)
    print(result)


if __name__ == "__main__":
    main(10)