MOD = 10**9 + 7
from collections import defaultdict as dd
import random

def main(n):
    # ---------- 1. 生成测试数据：一棵 n 个节点的树 ----------
    # 生成一棵随机树：对于每个 i(2..n)，连边 (i, parent) 其中 parent 在 [1, i-1]
    d = dd(list)
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        d[parent].append(i)
        d[i].append(parent)

    # 生成一个 BFS 序列 l，随机打乱同层顺序
    # 计算真实的 BFS 顺序（用于生成 l）
    q = [1]
    vis = [0] * (n + 1)
    vis[1] = 1
    bfs_layers = []  # 每一层是一个列表
    while q:
        layer = q[:]
        bfs_layers.append(layer)
        nq = []
        for u in q:
            for v in d[u]:
                if not vis[v]:
                    vis[v] = 1
                    nq.append(v)
        q = nq

    # 对每一层打乱顺序，合成 l
    l = []
    for layer in bfs_layers:
        random.shuffle(layer)
        l.extend(layer)

    # ---------- 2. 原逻辑：检查给定的树和序列 l 是否满足条件 ----------
    v = [0] * (n + 1)
    s = 1
    what = 0
    v[1] = 1

    # 确保 l 长度为 n，若不是则直接失败（正常情况下这里应为 n）
    if len(l) != n:
        print('No')
        return

    while what < s:
        a = set()
        i = l[what]
        for j in d[i]:
            if not v[j]:
                a.add(j)
        b = set()
        # 注意：原代码假定 s + len(a) 不会越界
        for j in range(s, s + len(a)):
            if j >= len(l):  # 防御性判断
                print('No')
                return
            b.add(l[j])
        if a != b:
            print('No')
            return
        kkk = 0
        for k in a:
            kkk += 1
            v[k] = 1
        s += kkk
        what += 1

    if s != n:
        print('No')
        return
    print('Yes')


# 示例：当直接运行本文件时，运行 main(10)
if __name__ == "__main__":
    main(10)