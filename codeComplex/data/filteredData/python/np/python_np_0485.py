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

    # 参数设计：
    # n: 模式串数量
    # m: 查询数量
    # k: 每个字符串长度
    k = max(1, n // 3)
    m = max(1, n * 2)

    # 生成 n 个模式串 p，长度为 k，由 'a'~'z' 和 '_' 构成
    p = []
    for i in range(n):
        chars = []
        for j in range(k):
            # 决定是否为 '_'：按 (i + j) 的奇偶性
            if (i + j) % 5 == 0:
                chars.append('_')
            else:
                # 字母选择：根据 (i + j) 映射到 1..26
                c = chr(96 + ((i + j) % 26) + 1 if (i + j) % 26 != 25 else 26)
                chars.append(c)
        p.append(''.join(chars))

    # 生成 m 条查询 (string, idx)
    # string: 长度为 k 的小写字母串
    # idx: 1..n 之间的索引，确定性循环
    s = []
    for q in range(m):
        chars = []
        for j in range(k):
            # 字母选择：按 (q + j) 构造
            c = chr(96 + ((q + 2 * j) % 26) + 1 if (q + 2 * j) % 26 != 25 else 26)
            chars.append(c)
        string = ''.join(chars)
        idx = (q % n) + 1
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