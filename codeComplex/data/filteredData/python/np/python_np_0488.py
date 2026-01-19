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

def main(n):
    if n <= 0:
        return

    k = 3
    num_chars = 3
    chars = ['a', 'b', 'c']
    total_patterns = num_chars ** k
    p_size = min(n, total_patterns)

    p_strings = []
    for i in range(p_size):
        x = i
        s = []
        for _ in range(k):
            s.append(chars[x % num_chars])
            x //= num_chars
        p_strings.append(''.join(s))

    def string_to_ord_tuple(s):
        return tuple(ord(c) for c in s)

    s_data = []
    for i in range(p_size):
        s_data.append((string_to_ord_tuple(p_strings[i]), i + 1))

    n_val = p_size
    m_val = len(s_data)
    k_val = k

    p = p_strings
    s = s_data

    memo = {}
    graph = [[] for _ in range(n_val)]

    for idx, ptn in enumerate(p):
        val = 0
        for i in range(k_val):
            if ptn[i] != "_":
                val += (ord(ptn[i]) - 96) * (27 ** i)
        memo[val] = idx

    for i, (string, idx) in enumerate(s):
        s[i] = (string, int(idx))

    for string, idx in s:
        idxs = []
        idx -= 1
        for bit_state in range(1 << k_val):
            val = 0
            for i in range(k_val):
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