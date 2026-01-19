import io
import os
from collections import Counter, defaultdict, deque
from pprint import pprint

def toposort(graph):
    res = []
    found = [0] * len(graph)
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            res.append(~node)
        elif not found[node]:
            found[node] = 1
            stack.append(~node)
            stack += graph[node]
    for node in res:
        if any(found[nei] for nei in graph[node]):
            return None
        found[node] = 0
    return res[::-1]


def solve(N, M, K, P, S, MT):
    graph = [[] for i in range(N)]

    def isMatch(s, pattern):
        for a, b in zip(s, pattern):
            if b != "_" and a != b:
                return False
        return True

    ordA = ord("a") - 1

    def hashStr(s):
        hsh = 0
        for i, c in enumerate(s):
            val = 27 if c == "_" else ord(c) - ordA
            hsh = 32 * hsh + val
        return hsh

    patternToId = {}
    for i, p in enumerate(P):
        patternToId[hashStr(p)] = i

    for s, mt in zip(S, MT):
        if not isMatch(s, P[mt]):
            return "NO"
        vals = [ord(c) - ordA for c in s]
        for mask in range(1 << K):
            hsh = 0
            for pos in range(K):
                val = 27 if (1 << pos) & mask else vals[pos]
                hsh = 32 * hsh + val
            if hsh in patternToId:
                mt2 = patternToId[hsh]
                if mt2 != mt:
                    graph[mt].append(mt2)

    ans = toposort(graph)
    if ans is None:
        return "NO"
    return "YES\n" + " ".join(str(i + 1) for i in ans)


def main(n):
    if n < 1:
        n = 1
    K = 3
    N = min(n, 1 << K)
    M = n
    base_patterns = []
    for mask in range(1 << K):
        chars = []
        for pos in range(K):
            if (mask >> pos) & 1:
                chars.append("_")
            else:
                chars.append(chr(ord("a") + pos))
        base_patterns.append("".join(chars))
    P = [base_patterns[i % len(base_patterns)] for i in range(N)]
    S = []
    MT = []
    for i in range(M):
        pat_idx = i % N
        pattern = P[pat_idx]
        s_chars = []
        for j in range(K):
            c = pattern[j]
            if c == "_":
                c = chr(ord("a") + ((pat_idx + j) % K))
            s_chars.append(c)
        s = "".join(s_chars)
        S.append(s)
        MT.append(pat_idx)
    ans = solve(N, M, K, P, S, MT)
    print(ans)


if __name__ == "__main__":
    main(10)