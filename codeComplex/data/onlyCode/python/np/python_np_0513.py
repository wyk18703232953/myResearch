#   Author: yumtam
#   Created at: 2021-03-06 23:41

def parse():
    s, i = input().split()
    i = int(i) - 1
    return s, i

def match(p, s):
    for a, b in zip(p, s):
        if a != '_' and a != b:
            return False
    return True

def main():
    from itertools import product

    n, m, k = [int(t) for t in input().split()]
    P = [input() for _ in range(n)]
    S = [parse() for _ in range(m)]

    index_of = dict()
    for i, p in enumerate(P):
        index_of[p] = i

    G = [[] for _ in range(n)]
    for s, i in S:
        if not match(P[i], s):
            print("NO")
            return

        for mask in product(range(2), repeat=k):
            sp = ['_' if bit else c for bit, c in zip(mask, s)]
            sp = ''.join(sp)

            try:
                j = index_of[sp]
                if i != j:
                    G[i].append(j)
            except:
                pass

    tp = toposort(G)
    if tp is None:
        print("NO")
    else:
        print("YES")
        print(*[x+1 for x in tp])


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

import sys, os, io
input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))

main()

os.write(1, stdout.getvalue())
