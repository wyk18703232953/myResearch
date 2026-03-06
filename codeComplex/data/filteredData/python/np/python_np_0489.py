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

def run_algorithm(n, m, k, p, s):
    memo = {}
    graph = [[] for _ in range(n)]
    for idx, ptn in enumerate(p):
        val = 0
        for i in range(k):
            if ptn[i] == "_":
                continue
            val += (ord(ptn[i]) - 96) * (27 ** i)
        memo[val] = idx

    s_conv = []
    for string, idx in s:
        s_conv.append((tuple(ord(ch) for ch in string), idx))
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
        graph[idx] += [idx_to for idx_to in idxs if idx != idx_to]

    flag, res = topological_sorted(graph)
    if flag:
        return True, [i + 1 for i in res]
    else:
        return False, []

def generate_data(n):
    # Scale parameters deterministically from n
    # k: pattern/string length (bounded to keep 2^k reasonable)
    k = 6 if n >= 6 else max(1, n)
    # number of patterns
    num_patterns = max(1, n)
    # number of strings
    num_strings = max(1, n)

    # Generate patterns p: list of strings of length k over 'a'..'c' and '_'
    # pattern i: for position j, choose deterministically based on (i+j)
    alphabet = ['a', 'b', 'c', '_']
    p = []
    for i in range(num_patterns):
        chars = []
        for j in range(k):
            ch = alphabet[(i + j) % len(alphabet)]
            chars.append(ch)
        p.append(''.join(chars))

    # Generate strings s: list of (string, idx) pairs
    # strings over 'a'..'c', and idx cycles through 1..num_patterns
    s = []
    alpha2 = ['a', 'b', 'c']
    for i in range(num_strings):
        chars = []
        for j in range(k):
            ch = alpha2[(i + 2 * j) % len(alpha2)]
            chars.append(ch)
        string = ''.join(chars)
        idx = (i % num_patterns) + 1
        s.append((string, idx))

    return num_patterns, num_strings, k, p, s

def main(n):
    n_nodes, m_edges, k, p, s = generate_data(n)
    ok, order = run_algorithm(n_nodes, m_edges, k, p, s)
    if ok:
        print("YES")
        print(*order)
    else:
        print("NO")

if __name__ == "__main__":
    main(10)