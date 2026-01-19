import sys
from io import BytesIO, IOBase

alphs = "abcdefghijklmnopqrstuvwxyz"


def run_solve_instance(n, m, k, words, constraints):
    dct = {}
    iput = []
    for i in range(n):
        word = words[i]
        dct[word] = i + 1
        iput.append(word)

    d = [[] for _ in range(n + 1)]
    size = [0] * (n + 1)

    for t in range(m):
        word, idx = constraints[t]
        idx = int(idx)
        temp = 1
        w = iput[idx - 1]

        for x in range(k):
            if w[x] != '_' and w[x] != word[x]:
                print("NO")
                return

        for mask in range(1 << k):
            s = "".join([word[x] if mask & (1 << x) == 0 else '_' for x in range(k)])
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


def main(n):
    if n <= 0:
        return

    # Deterministically map n -> (k, n_words, m_constraints)
    # Choose k so that 2^k not too large; cap k at 10
    k = min(10, max(1, n // 5))
    # Number of words grows roughly linearly with n, but at least k
    n_words = max(k, n)
    # Number of constraints up to n_words, but at least 1
    m_constraints = max(1, n_words // 2)

    # Generate deterministic words of length k
    # Characters are from 'a'..'z', pattern depends only on index and k
    words = []
    for i in range(n_words):
        s = []
        base = i + 1
        for pos in range(k):
            # simple deterministic mapping: alternate letters based on base and pos
            ch_index = (base * (pos + 3) + pos) % 26
            s.append(alphs[ch_index])
        words.append("".join(s))

    # Ensure that every word appears also with some '_' patterns in the dictionary
    # We will add some masked versions of first few words as extra entries
    extra_patterns = []
    for i in range(min(n_words, k)):
        w = words[i]
        # mask position i % k with '_'
        pos = i % k
        pattern = w[:pos] + '_' + w[pos + 1 :]
        extra_patterns.append(pattern)

    # Append extra patterns to the word list to increase connections
    words_extended = words + extra_patterns
    n_total = len(words_extended)

    # Rebuild words and map sizes
    words = words_extended
    n_words = n_total

    # Generate deterministic constraints: (pattern_word, index)
    constraints = []
    for t in range(m_constraints):
        idx = (t * 7 + 3) % n_words + 1  # 1-based index
        base_word = words[idx - 1]
        # create a pattern by masking some positions based on t
        s = list(base_word)
        for pos in range(k):
            if ((t + pos) % 3) == 0:
                s[pos] = '_'
        pattern = "".join(s)
        constraints.append((pattern, str(idx)))

    run_solve_instance(n_words, m_constraints, k, words, constraints)


if __name__ == "__main__":
    # Example deterministic calls for time-complexity experiments
    main(5)
    main(10)
    main(20)