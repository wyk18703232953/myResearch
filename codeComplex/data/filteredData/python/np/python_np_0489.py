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
    # 这里的 n 作为模式串个数（原代码中的 n）
    # 为使逻辑完整，需要同时生成：
    #   m: 查询个数
    #   k: 字符串长度
    # 并生成 p (模式串列表) 和 s (查询列表)
    #
    # 生成策略（可根据需求修改）：
    #   - 固定 k = 3
    #   - p 为 n 个由小写字母和下划线组成的长度为 k 的模式串
    #   - m = n（每个模式串对应一个查询）
    #   - 每个查询字符串与对应模式串兼容（保证至少有一个匹配）
    import random
    import string

    random.seed(0)

    k = 3
    m = n

    # 生成模式串 p：长度为 k，字符在 'a'~'c' 和 '_' 中选
    alphabet = "abc_"
    p = []
    for _ in range(n):
        s = "".join(random.choice(alphabet) for _ in range(k))
        p.append(s)

    # 生成查询 s：
    # 对于每个模式串 p[i]，生成一个具体字符串 str_i（无下划线），
    # 使得 str_i 能匹配 p[i]，并让查询索引为 i+1。
    # 匹配规则（延续原题意）：模式串有 '_' 为通配符，其余字符需与查询对应位置相同。
    s = []
    for i, pat in enumerate(p):
        chars = []
        for ch in pat:
            if ch == "_":
                # 通配符位置随机选 'a'~'c'
                chars.append(random.choice("abc"))
            else:
                chars.append(ch)
        query_str = "".join(chars)
        s.append((tuple(map(ord, query_str)), i + 1))

    # 以下是原逻辑，不再依赖 input()
    memo = {}
    graph = [[] for _ in range(n)]

    # 预处理模式串，建立哈希到索引的映射
    for idx, ptn in enumerate(p):
        val = 0
        for i in range(k):
            if ptn[i] != "_":
                val += (ord(ptn[i]) - 96) * (27 ** i)
        memo[val] = idx

    # 主过程
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

        graph[idx] += [idx_to for idx_to in idxs if idx != idx_to]

    flag, res = topological_sorted(graph)
    if flag:
        print("YES")
        print(*[i + 1 for i in res])
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)