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


def generate_data(n):
    if n <= 0:
        return 0, 0, 0, [], []
    k = min(5, max(1, n // 2))
    p_len = n
    m = n
    letters = [chr(97 + (i % 3)) for i in range(k)]
    p = []
    for i in range(p_len):
        chars = []
        for j in range(k):
            if (i + j) % 5 == 0:
                chars.append("_")
            else:
                chars.append(letters[(i + j) % len(letters)])
        p.append("".join(chars))
    s = []
    for i in range(m):
        chars = []
        for j in range(k):
            chars.append(letters[(i + j) % len(letters)])
        string = "".join(chars)
        idx = (i % p_len) + 1
        s.append([string, str(idx)])
    return p_len, m, k, p, s


def main(n):
    n, m, k, p, s = generate_data(n)

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