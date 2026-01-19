import sys

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

def run_once(n, m, k, p, s):
    memo = {}
    graph = [[] for _ in range(n)]
    for idx, ptn in enumerate(p):
        val = 0
        for i in range(k):
            if ptn[i] != "_":
                val += (ord(ptn[i]) - 96) * (27 ** i)
        memo[val] = idx

    s_processed = []
    for string, idx in s:
        s_processed.append((tuple(ord(c) for c in string), idx))
    s = s_processed

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
            return "NO", []

        for idx_to in idxs:
            if idx != idx_to:
                graph[idx].append(idx_to)

    flag, res = topological_sorted(graph)
    if flag:
        return "YES", [i + 1 for i in res]
    else:
        return "NO", []

def generate_input(n):
    if n <= 0:
        n = 1
    k = 3
    m = n
    p = []
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in range(n):
        s = []
        for j in range(k):
            base = (i + j * 7) % 28
            if base == 0:
                s.append("_")
            else:
                s.append(letters[(base - 1) % 26])
        p.append("".join(s))

    s = []
    for i in range(m):
        idx = (i % n) + 1
        base_string = list(p[idx - 1])
        pos = i % k
        base_string[pos] = letters[(ord(base_string[pos]) - 96 + 1) % 26]
        s.append(("".join(base_string), idx))
    return n, m, k, p, s

def main(n):
    n, m, k, p, s = generate_input(n)
    res_flag, order = run_once(n, m, k, p, s)
    if res_flag == "NO":
        print("NO")
    else:
        print("YES")
        print(*order)

if __name__ == "__main__":
    main(5)