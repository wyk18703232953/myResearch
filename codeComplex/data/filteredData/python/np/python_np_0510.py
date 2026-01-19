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


def generate_input(n):
    # Map n to (n_patterns, n_strings, k)
    # k is bounded to keep 1<<k polynomial in n
    k = max(1, min(10, n // 10 if n > 0 else 1))
    n_patterns = max(1, n)
    n_strings = max(1, n_patterns // 2)

    patterns = []
    pos = {}
    base_chars = [chr(ord('a') + (i % 26)) for i in range(k)]
    for i in range(n_patterns):
        # deterministically generate pattern string of length k
        s = []
        for j in range(k):
            # simple deterministic variation based on i,j
            c_index = (i + j * 7) % 26
            s.append(chr(ord('a') + c_index))
        p = ''.join(s)
        patterns.append(p)
        pos[p] = i

    # deterministically choose strings s and mt
    strings = []
    for i in range(n_strings):
        # pick a pattern index cyclically
        idx = i % n_patterns
        base = patterns[idx]
        s_list = list(base)
        # flip some characters deterministically to create variety
        for j in range(k):
            if (i + j) % 3 == 0:
                # shift character by 1 in alphabet
                c = s_list[j]
                s_list[j] = chr(ord('a') + ((ord(c) - ord('a') + 1) % 26))
        s = ''.join(s_list)
        # choose mt as some deterministic index
        mt = (idx * 3 + i) % n_patterns
        strings.append((s, mt + 1))  # mt is 1-based in original

    return k, patterns, pos, strings, n_patterns


def run_logic(k, patterns, pos, strings, n_patterns):
    patterns_set = set(patterns)
    matches = [[] for _ in range(n_patterns)]

    chk = True
    for i in range(len(strings)):
        s, mt = strings[i]
        mt = mt - 1
        if chk:
            chk = False
            for mask in range(1 << k):
                tmp_chars = []
                for j in range(k):
                    if mask & (1 << j):
                        tmp_chars.append('_')
                    else:
                        tmp_chars.append(s[j])
                tmp = ''.join(tmp_chars)
                if tmp in patterns_set:
                    if mt == pos[tmp]:
                        chk = True
                    else:
                        matches[mt].append(pos[tmp])

    if not chk:
        print("NO")
    else:
        toposort(matches)


def main(n):
    k, patterns, pos, strings, n_patterns = generate_input(n)
    run_logic(k, patterns, pos, strings, n_patterns)


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(10)