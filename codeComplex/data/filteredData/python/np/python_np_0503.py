def main(n):
    from collections import defaultdict as dft

    # Map n to problem scale:
    # Let number of words = n
    # Let word length k = max(1, n // 3)
    # Let number of queries m = n
    if n <= 0:
        return
    k = max(1, n // 3)
    m = n

    # Deterministic generation of words of length k using letters 'a'..'z' and '_'
    # word i is based on i in base-27 over alphabet [a..z,_]
    alphabet = [chr(ord('a') + i) for i in range(26)] + ['_']

    def gen_word(idx):
        x = idx
        chars = []
        for _ in range(k):
            chars.append(alphabet[x % 27])
            x //= 27
        return "".join(chars)

    # Generate n words, ensuring uniqueness may not be necessary for complexity;
    # but we will generate first n base-27 values.
    iput = [gen_word(i) for i in range(n)]
    dct = {w: i + 1 for i, w in enumerate(iput)}

    # Generate m queries:
    # Each query: (word, idx)
    # We create word by taking iput[idx-1] and flipping some positions to '_' deterministically.
    queries = []
    for qi in range(m):
        idx = (qi % n) + 1
        base_word = iput[idx - 1]
        # build query word from base_word using a simple pattern:
        # position x is '_' iff (qi >> (x % 5)) & 1 == 1, else keep base char
        w_list = list(base_word)
        for x in range(k):
            if ((qi >> (x % 5)) & 1) == 1:
                w_list[x] = '_'
        query_word = "".join(w_list)
        queries.append((query_word, idx))

    # Core algorithm logic from original program (without input/exit)

    d = [[] for _ in range(n + 1)]
    size = [0] * (n + 1)

    for word, idx in queries:
        temp = 1
        w = iput[idx - 1]

        for x in range(k):
            if w[x] != '_' and w[x] != word[x]:
                temp = 0
                # In original code: print("NO") and exit immediately.
                # Here we simulate that behavior deterministically by returning.
                print("NO")
                return

        for mask in range(1 << k):
            s = "".join([word[x] if (mask & (1 << x)) == 0 else '_' for x in range(k)])
            if s in dct:
                j = dct[s]
                if j != idx:
                    d[idx].append(j)
                    size[j] += 1

    st = [nd for nd in range(1, n + 1) if size[nd] == 0]

    # Topological processing
    for i in st:
        for j in d[i]:
            size[j] -= 1
            if size[j] == 0:
                st.append(j)

    if len(st) == n:
        print("YES")
        print(*st)
    else:
        print("NO")


if __name__ == "__main__":
    main(6)