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
    n: number of patterns; we also set m = n, k = 3 for test data generation.
    """
    import random

    # parameters for test generation
    k = 3                # pattern length
    m = n                # number of strings
    letters = [chr(ord('a') + i) for i in range(3)]  # use a small alphabet: a,b,c

    # generate patterns p: strings over letters + '_' as wildcard
    p = []
    for _ in range(n):
        s = []
        for _ in range(k):
            # randomly choose a letter or underscore
            if random.random() < 0.3:
                s.append('_')
            else:
                s.append(random.choice(letters))
        p.append(''.join(s))

    # generate m queries s: (string, idx)
    # string is concrete (no '_'), idx in [1..n]
    queries = []
    for _ in range(m):
        s_str = ''.join(random.choice(letters) for _ in range(k))
        idx = random.randint(1, n)
        queries.append([s_str, str(idx)])

    # ----- original logic below, with generated p, queries -----
    memo = {}
    for idx, ptn in enumerate(p):
        val = 0
        for i in range(k):
            if ptn[i] == "_":
                continue
            val += (ord(ptn[i]) - 96) * (27 ** i)
        memo[val] = idx

    s = queries
    for i, (string, idx) in enumerate(s):
        s[i] = (tuple(map(ord, string)), int(idx))

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
    # example: run with n = 5
    main(5)