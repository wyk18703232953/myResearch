# -*- coding:utf-8 -*-
import collections
import random

def main(n):
    # 生成一棵规模为 n 的随机树，p[i] 表示节点 i+2 的父节点
    # 节点编号为 1..n，根为 1
    p = []
    for i in range(2, n + 1):
        # 对于每个新节点 i，随机选择 [1, i-1] 中的一个父节点
        parent = random.randint(1, i - 1)
        p.append(parent)

    G = collections.defaultdict(list)

    for i, v in enumerate(p):
        u = i + 2
        G[u].append(v)
        G[v].append(u)

    root = 1

    colors = [0] * (n + 1)
    counts = [0] * (n + 1)

    q = [root]
    parents = [0] * (n + 1)
    vis = [0] * (n + 1)
    while q:
        u = q.pop()
        if vis[u]:
            colors[parents[u]] += colors[u]
            continue
        children = [v for v in G[u] if v != parents[u]]
        for v in children:
            parents[v] = u

        if children:
            vis[u] = True
            q.append(u)
            q.extend(children)
        else:
            vis[u] = True
            colors[u] = 1
            colors[parents[u]] += 1

    colors = colors[1:]
    colors.sort()
    print(' '.join(map(str, colors)))


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)