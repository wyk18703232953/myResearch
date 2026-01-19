import sys
from collections import deque

def main(n):
    # n: number of patterns and also number of queries (scalable input size)
    # k: length of each pattern string
    k = 5
    if n < 1:
        n = 1

    # Generate patterns P: n distinct strings of length k over 'a'..'z'
    # Deterministic construction by counting in base-26
    def int_to_string(x, length):
        s = []
        for _ in range(length):
            s.append(chr(ord('a') + (x % 26)))
            x //= 26
        s.reverse()
        return ''.join(s)

    P = [int_to_string(i, k) for i in range(n)]

    # Generate queries S: m = n queries
    # For diversity, each query pattern is derived deterministically from its index
    m = n
    S = []
    for i in range(m):
        base = P[i % n]
        # Create a pattern by replacing some positions with '_'
        # Position j is '_' if (i >> j) & 1 == 1, else keep base[j] (wrapped by k)
        pattern_chars = []
        for j in range(k):
            if (i >> j) & 1:
                pattern_chars.append('_')
            else:
                pattern_chars.append(base[j])
        pattern = ''.join(pattern_chars)
        # Choose index as (i % n), shifted to 0-based later
        idx = (i % n) + 1
        S.append([pattern, idx])

    # Begin original logic (without input)
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
    # Example deterministic call; adjust n to change input size
    main(8)