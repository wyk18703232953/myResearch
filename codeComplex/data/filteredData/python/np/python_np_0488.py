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


def solve_instance(n, m, k, p, s):
    memo = {}
    graph = [[] for _ in range(n)]
    for idx, ptn in enumerate(p):
        val = 0
        for i in range(k):
            if ptn[i] != "_":
                val += (ord(ptn[i]) - 96) * (27 ** i)
        memo[val] = idx

    s_conv = []
    for string, idx in s:
        s_conv.append((tuple(ord(c) for c in string), idx))
    s = s_conv

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
            return False, []

        for idx_to in idxs:
            if idx == idx_to:
                continue
            graph[idx].append(idx_to)

    flag, res = topological_sorted(graph)
    if not flag:
        return False, []
    return True, [i + 1 for i in res]


def main(n):
    # Map n to parameters:
    # k: pattern length (small, controls 2^k)
    # m: number of strings
    # we choose:
    # k = 5 (constant)
    # number of patterns = n
    # number of strings = n
    k = 5
    num_patterns = n
    num_strings = n

    # Deterministically generate patterns p of length k over 'a'..'c' and '_'
    chars = ['a', 'b', 'c', '_']
    p = []
    for i in range(num_patterns):
        x = i
        s = []
        for j in range(k):
            s.append(chars[x % 4])
            x //= 4
        p.append(''.join(s))

    # Deterministically generate strings s (string, idx)
    # strings of length k over 'a'..'c'
    s_list = []
    for i in range(num_strings):
        x = i
        s = []
        for j in range(k):
            s.append(chr(97 + (x % 3)))  # 'a','b','c'
            x //= 3
        string = ''.join(s)
        idx = (i % num_patterns) + 1
        s_list.append((string, idx))

    ok, order = solve_instance(num_patterns, num_strings, k, p, s_list)
    if ok:
        print("YES")
        print(*order)
    else:
        print("NO")


if __name__ == "__main__":
    main(1000)