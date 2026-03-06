def main(n):
    # Scale meaning:
    #   k = 3 (pattern length)
    #   number of patterns = n
    #   number of queries m = n
    k = 3
    m = n

    # Generate deterministic patterns P of length k over 'a','b','c'
    # e.g. for k=3: aaa, aab, aac, aba, ...
    alphabet = ['a', 'b', 'c']
    P = []
    total_patterns = len(alphabet) ** k
    for idx in range(n):
        x = idx % total_patterns
        s = []
        for pos in range(k):
            s.append(alphabet[(x // (len(alphabet) ** (k - pos - 1))) % len(alphabet)])
        P.append(''.join(s))

    # Generate deterministic queries S:
    # For i < n:
    #   x is P[i] with one character possibly changed (deterministic)
    #   index is i (1-based in original code)
    S = []
    for i in range(m):
        base_pattern = P[i % n]
        # deterministically modify one position based on i
        s_list = list(base_pattern)
        pos = (i + 1) % k
        # change character deterministically but keep in alphabet
        current = s_list[pos]
        s_list[pos] = alphabet[(alphabet.index(current) + 1) % len(alphabet)]
        x = ''.join(s_list)
        # to ensure feasibility, sometimes keep it equal to P[i]
        if i % 3 == 0:
            x = base_pattern
        S.append([x, str((i % n) + 1)])  # keep as strings initially

    # Original logic starts here, but with generated P, S, and given n, m, k
    for i in range(m):
        S[i][1] = int(S[i][1]) - 1

    PDICT = dict()
    for i in range(n):
        PDICT[P[i]] = i

    E = []

    for i in range(m):
        x = S[i][0]
        LIST = []

        for j in range(1 << k):
            t = ""
            for l in range(k):
                if (1 << l) & j != 0:
                    t += "_"
                else:
                    t += x[l]

            if t in PDICT:
                LIST.append(PDICT[t])

        if not (S[i][1] in LIST):
            print("NO")
            return
        else:
            s = S[i][1]
            for l in LIST:
                if l == s:
                    continue
                else:
                    E.append((s, l))

    EDGEIN = [0] * n
    EDGEOUTLIST = [[] for _ in range(n)]
    for x, y in E:
        EDGEIN[y] += 1
        EDGEOUTLIST[x].append(y)

    from collections import deque
    QUE = deque()

    for i in range(n):
        if EDGEIN[i] == 0:
            QUE.append(i)

    TOP_SORT = []
    while QUE:
        x = QUE.pop()
        TOP_SORT.append(x)
        for to in EDGEOUTLIST[x]:
            EDGEIN[to] -= 1
            if EDGEIN[to] == 0:
                QUE.appendleft(to)

    if len(TOP_SORT) == n:
        print("YES")
        print(*[i + 1 for i in TOP_SORT])
    else:
        print("NO")


if __name__ == "__main__":
    main(10)