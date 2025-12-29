from collections import defaultdict
import random
import string

def toposort(graph):
    res = []
    found = [0] * len(graph)
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            res.append(1 + (~node))
        elif not found[node]:
            found[node] = 1
            stack.append(~node)
            stack.extend(graph[node])

    # cycle check
    for node in res:
        node -= 1
        if any(found[nei] for nei in graph[node]):
            print("NO")
            return
        found[node] = 0

    print("YES")
    print(*res[::-1])


def generate_test_data(n, k):
    """
    生成：
    - n 个长度为 k 的 pattern（互不相同）
    - m 条查询，其中每条是 (s, mt)：
        s: 与某个 pattern 相同或只在若干位上替换为 '_'
        mt: 1-based 索引
    保证至少存在一个有效匹配，从而 chk == True。
    """
    # 生成 n 个不同的 pattern
    patterns = set()
    alphabet = string.ascii_lowercase
    while len(patterns) < n:
        p = ''.join(random.choice(alphabet) for _ in range(k))
        patterns.add(p)
    patterns = list(patterns)

    # 构造 m：这里让 m = n，且每个 s 对应第 i 个 pattern
    m = n
    queries = []
    for i in range(n):
        base = patterns[i]
        # 随机把若干位置替换为 '_' 以模拟通配
        s_list = list(base)
        for pos in range(k):
            if random.random() < 0.3:  # 30% 概率变成 '_'
                s_list[pos] = '_'
        s = ''.join(s_list)
        mt = i + 1  # 1-based
        queries.append((s, mt))

    return patterns, queries, m, k


def main(n):
    # 设定模式长度 k，可以根据需要调整或作为额外参数
    k = 3
    patterns_list, queries, m, k = generate_test_data(n, k)

    patterns = set(patterns_list)
    pos = {p: i for i, p in enumerate(patterns_list)}

    matches = [[] for _ in range(n)]

    chk = True

    for s, mt in queries:
        mt -= 1  # 转为 0-based
        if chk:
            chk = False
            for mask in range(1 << k):
                tmp = []
                for j in range(k):
                    if mask & (1 << j):
                        tmp.append('_')
                    else:
                        tmp.append(s[j])
                tmp = ''.join(tmp)
                if tmp in patterns:
                    if mt == pos[tmp]:
                        chk = True
                    else:
                        matches[mt].append(pos[tmp])

    if not chk:
        print("NO")
    else:
        toposort(matches)


if __name__ == "__main__":
    # 示例：n = 5
    main(5)