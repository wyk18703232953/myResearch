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
    k = 5
    if n < 2:
        n = 2
    m = n

    p = []
    for i in range(n):
        chars = []
        for j in range(k):
            if j == (i % k):
                chars.append("_")
            else:
                chars.append(chr(97 + (i + j) % 3))
        p.append("".join(chars))

    s = []
    for i in range(m):
        base = i % n
        string_chars = []
        for j in range(k):
            string_chars.append(chr(97 + (base + j) % 3))
        string = "".join(string_chars)
        idx = (base % n) + 1
        s.append((string, str(idx)))

    memo = {}
    for idx, ptn in enumerate(p):
        val = 0
        for i in range(k):
            if ptn[i] == "_":
                continue
            val += (ord(ptn[i]) - 96) * (27 ** i)
        memo[val] = idx

    s_conv = []
    for string, idx in s:
        s_conv.append((tuple(map(ord, string)), int(idx)))
    s = s_conv

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