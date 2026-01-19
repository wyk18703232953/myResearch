import io
import os

from collections import Counter, defaultdict, deque
from pprint import pprint

# toposort from pajenegod, AC server: https://discordapp.com/channels/555883512952258563/578670185007808512/708046996207829093
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

    # cycle check
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
    #print(patternToId)

    for s, mt in zip(S, MT):
        if not isMatch(s, P[mt]):
            return "NO"
        vals = [ord(c) - ordA for c in s]
        hsh = 0
        for mask in range(1 << K):
            hsh = 0
            for pos in range(K):
                val = 27 if (1 << pos) & mask else vals[pos]
                hsh = 32 * hsh + val
            if hsh in patternToId:
                mt2 = patternToId[hsh]

                #print(s, bin(mask), hsh, P[mt2])
                if mt2 != mt:
                    graph[mt].append(mt2)

    ans = toposort(graph)
    if ans is None:
        return "NO"

    return "YES\n" + " ".join(str(i + 1) for i in ans)


if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    TC = 1
    for tc in range(1, TC + 1):
        N, M, K = [int(x) for x in input().split()]
        P = [input().decode().rstrip() for i in range(N)]
        S = []
        MT = []
        for i in range(M):
            s, mt = input().split()
            s = s.decode()
            mt = int(mt) - 1  # 0 indexed
            S.append(s)
            MT.append(mt)
        ans = solve(N, M, K, P, S, MT)
        print(ans)

