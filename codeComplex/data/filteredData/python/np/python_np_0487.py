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
    """
    n: number of patterns
    The size parameter n controls:
      - number of patterns = n
      - number of strings m = n
      - pattern/string length k is fixed to 3 for test generation
    """
    k = 3  # fixed small length for generated test data
    m = n  # generate m == n queries

    # ---------- generate test data ----------
    # generate patterns p: list of strings of length k over 'a'..'c' and '_'
    # we ensure a simple consistent setting: exact matches only, no '_'
    # p[i] is just a repeated character pattern to keep it simple
    alphabet = ['a', 'b', 'c']
    p = []
    for i in range(n):
        ch = alphabet[i % len(alphabet)]
        p.append(ch * k)

    # generate m queries s: each is (string, index)
    # we let each string exactly match its designated pattern index (1-based)
    s = []
    for i in range(m):
        string = p[i]
        idx = i + 1  # 1-based index pointing to matching pattern
        s.append([string, str(idx)])

    # ---------- original core logic (without input) ----------
    memo = {}
    for idx, ptn in enumerate(p):
        val = 0
        for i in range(k):
            if ptn[i] != "_":
                val += (ord(ptn[i]) - 96) * (27 ** i)
        memo[val] = idx

    for i, (string, idx) in enumerate(s):
        s[i] = (tuple(ord(c) for c in string), int(idx))

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
            # print("NO")
            pass
            return

        for idx_to in idxs:
            if idx == idx_to:
                continue
            graph[idx].append(idx_to)

    flag, res = topological_sorted(graph)
    if flag:
        # print("YES")
        pass
        # print(*[i + 1 for i in res])
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # example: run with n = 5
    main(5)