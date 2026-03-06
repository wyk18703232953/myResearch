def main(n):
    # n controls the number of words; we also set m, k deterministically from n
    # k is word length, m is number of constraints
    if n <= 0:
        print("YES")
        print()
        return

    k = max(1, min(10, n // 2))  # bounded word length for determinism and scalability
    m = n  # one constraint per word index

    # Generate a deterministic alphabet and base-26 style words of length k
    alphs = "abcdefghijklmnopqrstuvwxyz"

    def gen_word(idx):
        # deterministic k-length word from idx
        chars = []
        x = idx
        for _ in range(k):
            chars.append(alphs[x % 26])
            x //= 26
        return "".join(chars)

    # construct original input arrays as the interactive program would read
    # First: n, m, k are already chosen
    # Next n words
    dct = {}
    iput = []
    for i in range(n):
        word = gen_word(i + 1)
        dct[word] = i + 1
        iput.append(word)

    # Next m lines: each has (word, idx)
    # We generate them deterministically:
    #   idx cycles through 1..n
    #   word is derived from (constraint index, idx) in a deterministic way,
    #   and may contain underscores.
    constraints = []
    for t in range(1, m + 1):
        idx = (t - 1) % n + 1
        base_word = iput[idx - 1]
        # Create a pattern word with possible underscores:
        # for position x, put '_' if (t + x + idx) is even, else shift character by 1
        pw = []
        for x in range(k):
            if (t + x + idx) % 3 == 0:
                pw.append('_')
            else:
                c = base_word[x]
                pw.append(alphs[(alphs.index(c) + ((t + x + idx) % 5)) % 26])
        pattern_word = "".join(pw)
        constraints.append((pattern_word, idx))

    # Core logic from original solve(), using generated data
    d = [[] for _ in range(n + 1)]
    size = [0] * (n + 1)

    for word, idx in constraints:
        temp = 1
        w = iput[idx - 1]

        for x in range(k):
            if w[x] != '_' and w[x] != word[x]:
                temp = 0
                print("NO")
                return

        for mask in range(1 << k):
            s_chars = []
            for x in range(k):
                if mask & (1 << x) == 0:
                    s_chars.append(word[x])
                else:
                    s_chars.append('_')
            s = "".join(s_chars)
            if s in dct:
                j = dct[s]
                if j != idx:
                    d[idx].append(j)
                    size[j] += 1

    st = [nd for nd in range(1, n + 1) if size[nd] == 0]

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
    # example deterministic call
    main(8)