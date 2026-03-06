def toposort(graph):
    res = []
    found = [0] * len(graph)
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            res.append(1 + (~node))
        elif not found[node]:
            found[node] = 1
            stack.append(~node)
            stack.extend(graph[node])

    for node in res:
        node -= 1
        if any(found[nei] for nei in graph[node]):
            print("NO")
            return
        found[node] = 0

    print("YES")
    print(*res[::-1])


def main(n):
    # Deterministically construct n, m, k
    if n < 2:
        n_eff = 2
    else:
        n_eff = n
    k = 3
    m = 2 * n_eff

    # Generate patterns: k-length strings over 'a'..'d'
    # Make n_eff distinct patterns
    def int_to_pattern(x, k):
        chars = ['a', 'b', 'c', 'd']
        res = []
        for _ in range(k):
            res.append(chars[x % 4])
            x //= 4
        return ''.join(res[::-1])

    patterns_list = [int_to_pattern(i, k) for i in range(n_eff)]
    patterns = set(patterns_list)
    pos = {p: i for i, p in enumerate(patterns_list)}

    matches = [[] for _ in range(n_eff)]

    # Generate m queries (s, mt)
    # s is some pattern (possibly modified), mt in [0, n_eff-1]
    queries = []
    for i in range(m):
        base_idx = i % n_eff
        base_pattern = patterns_list[base_idx]
        s_list = list(base_pattern)
        if i % 3 == 0:
            # change one character deterministically
            ch = s_list[0]
            s_list[0] = 'b' if ch != 'b' else 'c'
        s = ''.join(s_list)
        mt = (base_idx + 1)  # original code uses 1-based, then mt-1
        queries.append((s, mt))

    chk = True
    for s, mt in queries:
        mt = mt - 1
        if chk:
            chk = False
            for mask in range(1 << k):
                tmp = []
                for j in range(k):
                    if mask & (1 << j):
                        tmp.append('_')
                    else:
                        tmp.append(s[j] if j < len(s) else 'a')
                tmp = ''.join(tmp)
                if tmp in patterns:
                    if mt == pos[tmp]:
                        chk = True
                    else:
                        matches[mt].append(pos[tmp])

    if not chk:
        print("NO")
    else:
        toposort(matches)


if __name__ == "__main__":
    main(10)