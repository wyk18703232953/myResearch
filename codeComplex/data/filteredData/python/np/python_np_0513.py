#   Author: yumtam
#   Converted to main(n) version without input()

from itertools import product
import random
import string


def match(p, s):
    for a, b in zip(p, s):
        if a != '_' and a != b:
            return False
    return True


def toposort(graph):
    res, found = [], [0] * len(graph)
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            res.append(~node)
        elif not found[node]:
            found[node] = 1
            stack.append(~node)
            stack += graph[node]

    # cycle check
    for node in res:
        if any(found[nei] for nei in graph[node]):
            return None
        found[node] = 0

    return res[::-1]


def main(n):
    # n: scale parameter, used as number of patterns
    # We generate:
    #   k = 3 (pattern/string length)
    #   m = n (number of queries)
    #
    # Data generation strategy:
    #   - Generate n distinct full patterns (no '_')
    #   - Build index_of for them
    #   - Generate m strings s by picking one pattern P[i]
    #     and replacing some positions with '_' both in:
    #       * the "mask pattern" P[i] (kept as is here)
    #       * the query string s (kept as original characters so match holds)
    #   - i in queries is 1-based index into P as in original code
    #
    # This keeps the logic close to the original while being self-contained.

    random.seed(0)

    # Fix k (pattern length) and m (number of queries) based on n
    k = 3
    m = n

    # Generate n distinct patterns of length k over lowercase letters
    # Ensure uniqueness by using a set
    P_set = set()
    letters = string.ascii_lowercase
    while len(P_set) < n:
        p = ''.join(random.choice(letters) for _ in range(k))
        P_set.add(p)
    P = list(P_set)

    # Build index map for patterns
    index_of = {p: i for i, p in enumerate(P)}

    # Generate m queries S: list of (s, i)
    S = []
    for _ in range(m):
        i = random.randrange(n)  # zero-based index into P
        base = P[i]
        # s is exactly the base string; P[i] remains a full literal pattern
        s = base
        # store with 0-based index as original parse() did (int(i) - 1)
        S.append((s, i))

    # Now run the original logic (without I/O) on generated P, S
    G = [[] for _ in range(n)]

    for s, i in S:
        if not match(P[i], s):
            print("NO")
            return

        for mask in product(range(2), repeat=k):
            sp = ['_' if bit else c for bit, c in zip(mask, s)]
            sp = ''.join(sp)

            j = index_of.get(sp)
            if j is not None and i != j:
                G[i].append(j)

    tp = toposort(G)
    if tp is None:
        print("NO")
    else:
        print("YES")
        print(*[x + 1 for x in tp])


if __name__ == "__main__":
    # Example: run with n = 5 for a small test
    main(5)