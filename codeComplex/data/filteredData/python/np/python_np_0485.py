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


def generate_data(n):
    if n <= 0:
        n = 1
    # k: pattern length, grows slowly with n to keep 2^k manageable
    k = max(1, min(6, n // 3 + 1))
    # number of patterns
    num_patterns = n
    # number of strings/queries
    m = n

    # generate patterns p: list of length num_patterns, each string length k
    # characters chosen deterministically from 'a'..'z' or '_' based on indices
    p = []
    for i in range(num_patterns):
        chars = []
        for j in range(k):
            base = (i + 1) * (j + 2)
            if (base % 5) == 0:
                chars.append('_')
            else:
                chars.append(chr(97 + (base % 26)))
        p.append(''.join(chars))

    # generate s: list of m pairs (string, idx) where
    # string is length k, idx between 1 and num_patterns inclusive
    s = []
    for i in range(m):
        chars = []
        for j in range(k):
            base = (i + 2) * (j + 3)
            chars.append(chr(97 + (base % 26)))
        string = ''.join(chars)
        idx = (i % num_patterns) + 1
        s.append([string, str(idx)])

    return num_patterns, m, k, p, s


def run_algorithm(n, m, k, p, s):
    memo = {}
    for idx, ptn in enumerate(p):
        val = 0
        for i in range(k):
            if ptn[i] == "_":
                continue
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
            return False, None

        for idx_to in idxs:
            if idx == idx_to:
                continue
            graph[idx].append(idx_to)

    flag, res = topological_sorted(graph)
    if flag:
        return True, [i + 1 for i in res]
    else:
        return False, None


def main(n):
    n, m, k, p, s = generate_data(n)
    flag, res = run_algorithm(n, m, k, p, s)
    if flag:
        print("YES")
        print(*res)
    else:
        print("NO")


if __name__ == "__main__":
    main(10)