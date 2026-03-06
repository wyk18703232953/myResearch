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
    # Map n to:
    # k: pattern length
    # n: number of patterns
    # m: number of queries
    if n < 1:
        n = 1
    k = 3
    num_patterns = n
    m = n

    # Generate deterministic patterns of length k
    # pattern i is based on base-3 representation over 'a','b','c'
    chars = ['a', 'b', 'c']
    patterns_list = []
    for i in range(num_patterns):
        x = i
        s = []
        for _ in range(k):
            s.append(chars[x % 3])
            x //= 3
        patterns_list.append(''.join(s))
    patterns = set(patterns_list)
    pos = {p: i for i, p in enumerate(patterns_list)}

    matches = [[] for _ in range(num_patterns)]

    # Generate deterministic queries (s, mt)
    # s is chosen similarly; mt cycles through valid indices
    queries = []
    for i in range(m):
        x = i + num_patterns  # shift to differ from patterns somewhat
        s = []
        for _ in range(k):
            s.append(chars[x % 3])
            x //= 3
        s = ''.join(s)
        mt = i % num_patterns  # 0-based
        queries.append((s, mt))

    chk = True
    first = True
    for s, mt in queries:
        if first:
            first = False
            for mask in range(1 << k):
                tmp = []
                for j in range(k):
                    if mask & (1 << j):
                        tmp.append('_')
                    else:
                        tmp.append(s[j])
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