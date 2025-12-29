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
    n: 规模，用作模式数量。自动生成测试数据:
    - k 固定为 3
    - m = n
    - 构造 n 个模式 p，和 m 个查询 s
    """
    import random
    random.seed(0)

    # 固定参数
    k = 3            # 每个模式长度
    m = n            # 查询数量

    # 生成模式 p：长度为 k，由 'a'~'c' 和 '_' 组成
    chars = ['a', 'b', 'c', '_']
    p = []
    for _ in range(n):
        pat = ''.join(random.choice(chars) for _ in range(k))
        p.append(pat)

    # 生成查询 s：
    # string: 长度为 k，由 'a'~'c' 组成，不含 '_'
    # idx: 1 ~ n 之间的随机下标
    s = []
    for _ in range(m):
        string = ''.join(random.choice(['a', 'b', 'c']) for _ in range(k))
        idx = random.randint(1, n)
        s.append([string, str(idx)])

    # 以下是原逻辑，无 input()

    memo = {}
    for idx, ptn in enumerate(p):
        val = 0
        for i in range(k):
            if ptn[i] == "_":
                continue
            val += (ord(ptn[i]) - 96) * (27 ** i)
        memo[val] = idx

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
    # 示例：运行规模 n=5
    main(5)