from collections import defaultdict as dft
import random
import string

def main(n):
    # n: number of distinct words in the "dictionary" (nodes in graph)
    # We'll generate:
    # - n words (only lowercase letters)
    # - m queries (m chosen as n for simplicity)
    # - each query is a pattern word with '_' as wildcard, plus an index in [1..n]

    # 1. Generate dictionary words
    # ensure uniqueness by sampling from a large space
    words = set()
    max_len = 8
    while len(words) < n:
        L = random.randint(1, max_len)
        w = ''.join(random.choice(string.ascii_lowercase) for _ in range(L))
        words.add(w)
    words = list(words)  # index 0..n-1

    # 2. Build trie
    trie = {}
    for i, word in enumerate(words, start=1):
        dct = trie
        for ch in word:
            if ch not in dct:
                dct[ch] = {}
            dct = dct[ch]
        dct['#'] = i  # store index (1-based) at terminal

    # 3. Generate queries (patterns and indices)
    # We'll set k = length of patterns. To make it compatible with original code,
    # we must fix k, then only use words of length k in queries.
    # Choose k in [1..max_len], then build patterns of that length.
    k = random.randint(1, max_len)

    # helper to collect all indices of words with specific length k
    words_by_len = [i + 1 for i, w in enumerate(words) if len(w) == k]
    if not words_by_len:
        # If no words of length k exist, adjust k to something existing or trivial
        # For simplicity, set k=1 and create one-letter words
        k = 1
        # reset words and trie to guarantee correct shape
        words = []
        trie = {}
        for i in range(1, n + 1):
            w = random.choice(string.ascii_lowercase)
            words.append(w)
            dct = trie
            for ch in w:
                if ch not in dct:
                    dct[ch] = {}
                dct = dct[ch]
            dct['#'] = i
        words_by_len = [i for i in range(1, n + 1)]

    # choose m = n queries
    m = n
    queries = []
    for _ in range(m):
        # pick a base word index that has length k
        idx = random.choice(words_by_len)
        w = words[idx - 1]  # actual word
        # create pattern from w, turning some chars into '_'
        pat = list(w)
        # random number of wildcards (can be zero)
        num_wild = random.randint(0, k)
        pos = random.sample(range(k), num_wild)
        for p in pos:
            pat[p] = '_'
        pattern = ''.join(pat)
        queries.append((pattern, idx))

    # 4. Now replicate original solve() logic using the generated data
    # Rebuild trie just to follow same structure as original (not strictly needed)
    trie = {}
    for i, word in enumerate(words, start=1):
        dct = trie
        for ch in word:
            if ch not in dct:
                dct[ch] = {}
            dct = dct[ch]
        dct['#'] = i

    def chk(word, dct, i, k, res):
        if i == k:
            if '#' in dct:
                res.append(dct['#'])
        else:
            ch = word[i]
            if ch in dct:
                chk(word, dct[ch], i + 1, k, res)
            if '_' in dct:
                chk(word, dct['_'], i + 1, k, res)

    d = dft(list)
    case = 0

    for word, idx in queries:
        res = []
        chk(word, trie, 0, len(word), res)
        temp = 0
        for num in res:
            if num != idx:
                d[idx].append(num)
            else:
                temp = 1
        if not temp:
            case = 1

    # 5. Topological sort with cycle detection as in original code

    order = [0] * (n + 1)
    vis = [0] * (n + 1)
    seen = set()
    idx_pos = n

    def seq(nd, i):
        case_local = 0
        vis[nd] = 1
        for lnk in d[nd]:
            if not vis[lnk]:
                i, case_local = seq(lnk, i)
                if case_local:
                    return i, case_local
            else:
                if lnk not in seen:
                    case_local = 1
                    break
        order[i] = nd
        seen.add(nd)
        return i - 1, case_local

    for node in range(1, n + 1):
        if not vis[node]:
            idx_pos, tp = seq(node, idx_pos)
            if tp:
                case = 1
                break

    if case:
        print("NO")
    else:
        print("YES")
        print(*order[1:])


if __name__ == "__main__":
    # Example: run main with n = 10
    main(10)