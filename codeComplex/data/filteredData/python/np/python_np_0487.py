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


def main(n):
    if n < 1:
        n = 1
    k = max(1, min(5, n // 3))
    m = n
    p = []
    for i in range(n):
        pattern = []
        for j in range(k):
            if (i + j) % 4 == 0:
                pattern.append("_")
            else:
                pattern.append(chr(97 + (i + j) % 3))
        p.append("".join(pattern))
    s = []
    for i in range(m):
        base_chars = []
        qi = i % n
        for j in range(k):
            ch = p[qi][j]
            if ch == "_":
                base_chars.append(chr(97 + (qi + j) % 3))
            else:
                base_chars.append(ch)
        string = "".join(base_chars)
        idx = (qi % n) + 1
        s.append([string, str(idx)])
    memo = {}
    for idx, ptn in enumerate(p):
        val = 0
        for i in range(k):
            if ptn[i] != "_":
                val += (ord(ptn[i]) - 96) * (27 ** i)
        memo[val] = idx
    for i, (string, idx) in enumerate(s):
        s[i] = tuple(map(ord, string)), int(idx)
    graph = [[] for _ in range(n)]
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
            return
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


if __name__ == "__main__":
    main(10)