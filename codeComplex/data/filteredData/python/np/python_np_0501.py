def patterns(s):
    if len(s) == 1:
        return [s, '_']
    else:
        tp = patterns(s[1:])
        return [s[0] + t for t in tp] + ['_' + t for t in tp]

def main(n):
    # n: number of patterns, and roughly number of queries (m ≈ n)
    # scale m with n to keep proportional
    m = n
    k = 1  # unused in original code but kept for structure

    # Deterministically generate n base patterns of length L
    # Use alphabet 'a'..'j' and '_' for variety but avoid starting with '_'
    # pattern i is a base-11 representation of i, mapped to chars
    L = 4  # fixed small length; changing this changes pattern space size, not asymptotics
    alphabet = "abcdefghij"
    def encode(i, length=L):
        # base-11 digits 0-9,10 -> a-j, '_'
        s = []
        for _ in range(length):
            d = i % 11
            if d == 10:
                ch = '_'
            else:
                ch = alphabet[d]
            s.append(ch)
            i //= 11
        s.reverse()
        # ensure no leading '_' to avoid accidental collisions with patterns()
        if s[0] == '_':
            s[0] = 'a'
        return ''.join(s)

    patterns_list = [encode(i) for i in range(n)]

    # Build name->index map
    ppm = {p: i for i, p in enumerate(patterns_list)}

    pre = [0] * n
    suc = [[] for _ in range(n)]

    # Deterministically generate m query strings s and indices ml (1-based in original input)
    # For queries, derive from base patterns with simple deterministic modifications
    queries = []
    for q in range(m):
        base_idx = q % n
        base = patterns_list[base_idx]
        # produce a query string by flipping some characters deterministically
        s_chars = list(base)
        pos = q % L
        # change char at pos in a cyclic deterministic way
        c = s_chars[pos]
        if c == '_':
            s_chars[pos] = 'a'
        else:
            # shift within alphabet or to '_'
            if c in alphabet:
                idx = alphabet.index(c)
                idx = (idx + 1) % 11
                if idx == 10:
                    s_chars[pos] = '_'
                else:
                    s_chars[pos] = alphabet[idx]
            else:
                s_chars[pos] = 'b'
        s = ''.join(s_chars)
        # choose target index ml so that some edges are created
        ml = (base_idx + (q % 3)) % n  # 0-based
        queries.append((s, ml))

    # Simulate original core logic using generated data
    for s, ml in queries:
        ps = patterns(s)
        found = False
        for p in ps:
            if p in ppm:
                if ppm[p] == ml:
                    found = True
                else:
                    pre[ppm[p]] += 1
                    suc[ml].append(ppm[p])
        if not found:
            print("NO")
            return

    # Topological sort
    znodes = [i for i in range(n) if pre[i] == 0]
    res = []
    while znodes:
        i = znodes.pop()
        res.append(i + 1)
        for j in suc[i]:
            pre[j] -= 1
            if pre[j] == 0:
                znodes.append(j)
    if len(res) == n:
        print("YES")
        print(' '.join(map(str, res)))
    else:
        print("NO")

if __name__ == "__main__":
    # Example scale; adjust n for experiments
    main(10)