import random
import string


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
    # 规模 n：模式个数
    # 生成测试数据：k 固定或随 n 变化，这里简单设为 min(5, n) 保证非空
    k = max(1, min(5, n))
    # m 为查询数，这里设为 n 的 2 倍
    m = max(1, 2 * n)

    # 生成 n 个长度为 k 的模式串，使用小写字母和 '_'，保证可重复
    alphabet = string.ascii_lowercase
    patterns = []
    for _ in range(n):
        s = []
        for _ in range(k):
            if random.random() < 0.2:
                s.append('_')
            else:
                s.append(random.choice(alphabet))
        patterns.append(''.join(s))

    # 生成 m 个查询 (string, idx)
    # string: 长度为 k 的纯字母串
    # idx: 1..n
    queries = []
    for _ in range(m):
        s = ''.join(random.choice(alphabet) for _ in range(k))
        idx = random.randint(1, n)
        queries.append((s, idx))

    # 以下是原始逻辑

    p = patterns
    s = queries
    memo = {}
    graph = [[] for _ in range(n)]

    for idx, ptn in enumerate(p):
        val = sum(
            (ord(ptn[i]) - 96) * (27 ** i)
            for i in range(k) if ptn[i] != "_"
        )
        memo[val] = idx

    s = [(tuple(map(ord, string)), int(idx)) for (string, idx) in s]

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