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
    根据规模 n 生成测试数据:
    - n: 模式数量
    - k: 模式长度
    返回 (patterns_list, queries)
    其中：
      patterns_list: 长度为 n 的模式字符串列表
      queries: 长度为 m 的 (s, mt) 列表，模拟原始的 m 行输入
    """
    # 为简单起见，令 m = n
    m = n

    # 生成 n 个长度为 k 的模式串（小写字母）
    patterns = []
    used = set()
    while len(patterns) < n:
        p = ''.join(random.choice(string.ascii_lowercase[:3]) for _ in range(k))
        if p not in used:
            used.add(p)
            patterns.append(p)

    # 生成 m 条查询，每条 (s, mt)
    # 保证 s 与某个模式有关系，mt 为 [1, n] 之间
    queries = []
    for _ in range(m):
        # 随机选一个模式作为基础
        base = random.choice(patterns)
        s_list = list(base)
        # 随机改动若干位置，制造多样性
        for i in range(k):
            if random.random() < 0.3:
                s_list[i] = random.choice(string.ascii_lowercase[:3])
        s = ''.join(s_list)
        mt = random.randint(1, n)
        queries.append((s, mt))

    return patterns, queries


def main(n):
    # 这里可以固定 k，或根据 n 设定
    k = 3

    # 1. 生成测试数据
    patterns_list, queries = generate_test_data(n, k)

    # 2. 按原逻辑构造数据结构
    patterns = set(patterns_list)
    pos = {p: i for i, p in enumerate(patterns_list)}

    matches = [[] for _ in range(n)]

    chk = True
    for s, mt in queries:
        mt -= 1
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
    # 示例: 规模 n = 5
    main(5)