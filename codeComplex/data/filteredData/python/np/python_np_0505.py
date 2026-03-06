def main(n):
    from collections import defaultdict as dft

    # Deterministic data generation based on n
    # Number of words
    num_words = max(1, n)
    # Number of pattern constraints (edges in graph)
    m = max(1, n * 2)
    # Word length
    k = max(1, (n % 5) + 3)

    alphs = "abcdefghijklmnopqrstuvwxyz"

    # Generate words deterministically
    words = []
    for i in range(num_words):
        # Build a word of length k using deterministic pattern
        w = []
        base = i + 1
        for j in range(k):
            # Choose character based on i and j
            ch = alphs[(base * (j + 3) + j) % 26]
            w.append(ch)
        words.append("".join(w))

    # Build a trie of words
    trie = {}
    for i, word in enumerate(words):
        dct = trie
        for w in word:
            if w not in dct:
                dct[w] = {}
            dct = dct[w]
        dct['#'] = i + 1

    # Build m pattern queries deterministically
    # For each query we create a pattern and an index
    queries = []
    for i in range(m):
        idx = (i % num_words) + 1  # ensure idx in [1, num_words]
        w = list(words[idx - 1])
        pos = (i + idx) % k
        if (i + idx) % 3 == 0:
            w[pos] = '_'  # wildcard
        else:
            # deterministically modify one character
            ch_index = (alphs.index(w[pos]) + (i % 5) + 1) % 26
            w[pos] = alphs[ch_index]
        pattern = "".join(w)
        queries.append((pattern, idx))

    d = dft(list)
    case = 0
    res = []

    def chk(word, dct, i_pos):
        if i_pos == k:
            res.append(dct['#'])
        else:
            if word[i_pos] in dct:
                chk(word, dct[word[i_pos]], i_pos + 1)
            if '_' in dct:
                chk(word, dct['_'], i_pos + 1)

    # Process queries, build dependency graph
    for word, idx in queries:
        res.clear()
        chk(word, trie, 0)
        temp = 0
        for num in res:
            if num != idx:
                d[idx].append(num)
            else:
                temp = 1
        if not temp:
            case = 1

    # Topological sort with cycle detection
    order = [0] * (num_words + 1)
    vis = [0] * (num_words + 1)
    seen = set()
    idx_order = num_words

    def seq(nd, i_pos):
        case_local = 0
        vis[nd] = 1
        for lnk in d[nd]:
            if not vis[lnk]:
                i_pos, case_local = seq(lnk, i_pos)
                if case_local:
                    return i_pos, case_local
            else:
                if lnk not in seen:
                    case_local = 1
                    break
        order[i_pos] = nd
        seen.add(nd)
        return i_pos - 1, case_local

    for i in range(1, num_words + 1):
        if not vis[i]:
            idx_order, tp = seq(i, idx_order)
            if tp:
                case = 1
                break

    if case:
        print("NO")
    else:
        print("YES")
        print(*order[1:])


if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(10)