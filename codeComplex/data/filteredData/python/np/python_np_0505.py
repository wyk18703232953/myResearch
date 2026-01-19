import sys
from collections import defaultdict as dft

def solve(n, words, queries):
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

    def chk(word, dct, i):
        if i == k:
            res.append(dct['#'])
        else:
            if word[i] in dct:
                chk(word, dct[word[i]], i + 1)
            if '_' in dct:
                chk(word, dct['_'], i + 1)

    m = len(queries)
    k = len(queries[0][0]) if m > 0 else 0

    trie = {}
    for i in range(n):
        word = words[i]
        dct = trie
        for w in word:
            if w not in dct:
                dct[w] = {}
            dct = dct[w]
        dct['#'] = i + 1

    d = dft(list)
    global case
    case = 0

    for (word, idx) in queries:
        res = []
        chk(word, trie, 0)
        temp = 0
        for num in res:
            if num != idx:
                d[idx].append(num)
            else:
                temp = 1
        if not temp:
            case = 1

    order = [0] * (n + 1)
    vis = [0] * (n + 1)
    seen = set()
    idx = n

    for i in range(1, n + 1):
        if not vis[i]:
            idx, tp = seq(i, idx)
            if tp:
                case = 1
                break

    if case:
        print("NO")
    else:
        print("YES")
        print(*order[1:])

def main(n):
    # n controls the scale:
    # - number of words: n
    # - number of queries: n
    # - word length and pattern length: 5
    word_len = 5
    n = max(1, int(n))

    # Deterministically generate n words of length 5 using letters a-z
    alph = "abcdefghijklmnopqrstuvwxyz"
    words = []
    for i in range(n):
        w = []
        x = i
        for j in range(word_len):
            w.append(alph[x % 26])
            x = x // 26 + 1
        words.append("".join(w))

    # Deterministically generate n queries (pattern, idx)
    # Pattern is word with some positions replaced by '_'
    queries = []
    for i in range(n):
        base_idx = (i % n) + 1  # ensure idx in [1, n]
        base_word = words[(i * 7 + 3) % n]
        chars = list(base_word)
        for pos in range(word_len):
            if (i + pos) % 3 == 0:
                chars[pos] = '_'
        pattern = "".join(chars)
        queries.append((pattern, base_idx))

    solve(n, words, queries)

if __name__ == "__main__":
    main(10)