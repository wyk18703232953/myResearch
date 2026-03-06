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


def run_instance(n, m, k):
    # deterministic generation of patterns p and queries s
    # alphabet: 'a'..'z'
    # pattern length = k
    # number of patterns = n
    # number of queries = m

    # generate patterns p: k-length strings over 'a'..'z' and '_' deterministically
    # to keep many matches, we introduce '_' in a regular pattern
    p = []
    for i in range(n):
        chars = []
        for j in range(k):
            if (i + j) % (k + 1) == 0:
                chars.append("_")
            else:
                # deterministic letter based on i, j
                letter = chr(97 + ((i * (j + 1)) % 26))
                chars.append(letter)
        p.append("".join(chars))

    # generate m queries s: each is (string, idx)
    # string is k-length over 'a'..'z'
    # idx in [1, n] deterministic
    s = []
    for q in range(m):
        chars = []
        for j in range(k):
            letter = chr(97 + ((q + j * 3) % 26))
            chars.append(letter)
        string = "".join(chars)
        idx = (q * 7) % n + 1
        s.append([string, str(idx)])

    memo = {}
    for idx, ptn in enumerate(p):
        val = 0
        for i in range(k):
            if ptn[i] == "_":
                continue
            val += (ord(ptn[i]) - 96) * (27 ** i)
        memo[val] = idx

    for i, (string, idx) in enumerate(s):
        s[i] = tuple(ord(c) for c in string), int(idx)

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
            return False, []

        for idx_to in idxs:
            if idx == idx_to:
                continue
            graph[idx].append(idx_to)

    flag, res = topological_sorted(graph)
    return flag, res


def main(n):
    # map single parameter n to (n, m, k)
    # choose k small to keep 2^k manageable
    # let k = 5 (32 subsets), m ~ n, all deterministic
    if n <= 0:
        return
    k = 5
    m = n
    flag, res = run_instance(n, m, k)
    if flag:
        print("YES")
        print(*[i + 1 for i in res])
    else:
        print("NO")


if __name__ == "__main__":
    main(1000)