import sys
input = sys.stdin.readline


def topological_sorted(digraph):
    n = len(digraph)
    indegree = [0] * n
    for v in range(n):
        for nxt_v in digraph[v]:
            indegree[nxt_v] += 1

    tp_order = [i for i in range(n) if indegree[i] == 0]
    stack = tp_order[:]
    while stack:
        v = stack.pop()
        for nxt_v in digraph[v]:
            indegree[nxt_v] -= 1
            if indegree[nxt_v] == 0:
                stack.append(nxt_v)
                tp_order.append(nxt_v)

    return len(tp_order) == n, tp_order


n, m, k = map(int, input().split())
p = [input()[:-1] for i in range(n)]
s = [list(input().split()) for i in range(m)]


memo = {}
for idx, ptn in enumerate(p):
    val = 0
    for i in range(k):
        if ptn[i] == "_":
            continue
        val += (ord(ptn[i]) - 96) * (27 ** i)
    memo[val] = idx

for i, (string, idx) in enumerate(s):
    s[i] = tuple(map(ord, string)), int(idx)

graph = [[] for i in range(n)]
for string, idx in s:
    idxs = []
    idx -= 1
    for bit_state in range(1 << k):
        val = 0
        for i in range(k):
            if (bit_state >> i) & 1:
                continue
            val += (string[i] - 96) * (27 ** i)
        if val in memo:
            idxs.append(memo[val])
    if idx not in idxs:
        print("NO")
        exit()

    for idx_to in idxs:
        if idx == idx_to:
            continue
        graph[idx].append(idx_to)

flag, res = topological_sorted(graph)
if flag:
    print("YES")
    print(*[i + 1 for i in res])
else:
    print("NO")