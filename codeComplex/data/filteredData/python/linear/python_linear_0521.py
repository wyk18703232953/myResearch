from collections import defaultdict
import random


def main(n):
    # 1. 生成一棵 n 个节点的随机树，节点编号为 1..n
    t = defaultdict(list)
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)
        t[u].append(v)
        t[v].append(u)

    # 2. 生成一个 1..n 的随机排列 a
    a = list(range(1, n + 1))
    random.shuffle(a)

    o = {a_: i for i, a_ in enumerate(a)}

    # BFS 计算每个节点的层数 lv 和父亲 par
    i = 0
    q = [1]
    lv = {1: 0}
    par = {1: 1}
    while i < len(q):
        u = q[i]
        i += 1
        for v in t[u]:
            if v not in lv:
                lv[v] = lv[u] + 1
                q.append(v)
                par[v] = u

    # depths[d] 中存储深度为 d 的节点，其父节点在排列 a 中的位置
    depths = defaultdict(list)
    for x in a:
        depths[lv[x]].append(o[par[x]])

    ans = a[0] == 1
    if ans:
        for d in depths.values():
            if not all(d[i] <= d[i + 1] for i in range(len(d) - 1)):
                ans = False
                break

    if ans:
        l = [lv[x] for x in a]
        ans = all(l[i] <= l[i + 1] for i in range(len(l) - 1))

    print(('No', 'Yes')[ans])


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)