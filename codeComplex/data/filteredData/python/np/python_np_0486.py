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
    # 生成一组规模为 n 的测试数据
    # 约定：k = 3，m = n
    k = 3
    m = n

    # 生成 n 个模式串，每个长度为 k，由 'a'~'c' 和 '_' 构成
    chars = ['a', 'b', 'c', '_']
    p = []
    for i in range(n):
        s = []
        for j in range(k):
            # 简单构造，让模式有一定多样性且可重复
            s.append(chars[(i + j) % len(chars)])
        p.append(''.join(s))

    # 生成 m 条查询 (string, idx)，string 长度为 k，由 'a'~'c' 构成
    # 尽量保证每个查询至少与自己的模式匹配
    s = []
    for i in range(m):
        # 将模式 p[i] 中的 '_' 替换成 'a'
        base = list(p[i])
        for j in range(k):
            if base[j] == '_':
                base[j] = 'a'
        string = ''.join(base)
        idx = (i % n) + 1  # 1-based
        s.append((string, idx))

    # ---------------- 以下为原始逻辑 ----------------
    memo = {}
    for idx, ptn in enumerate(p):
        val = 0
        for i in range(k):
            if ptn[i] == "_":
                continue
            val += (ord(ptn[i]) - 96) * (27 ** i)
        memo[val] = idx

    s_conv = []
    for string, idx in s:
        s_conv.append((tuple(map(ord, string)), int(idx)))
    s = s_conv

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
    # 示例：调用 main(5)
    main(5)