# -*- coding: utf-8 -*-
from collections import defaultdict, deque
import random

class Graph:
    def __init__(self):
        self.g = defaultdict(list)

    def addedge(self, u, v):
        self.g[u].append(v)

def router(values):
    gr = Graph()
    for i in range(len(values)):
        gr.addedge(values[i], i + 2)
    return gr.g

def isleaf(node, gr):
    return len(gr[node]) == 0

def christmas(gr, start, visited):
    q = deque()
    q.append(start)
    visited[start] = True
    count = 0
    while q:
        count = 0
        value = q.popleft()
        for val in gr[value]:
            if not isleaf(val, gr):
                q.append(val)
                visited[val] = True
            else:
                visited[val] = True
                count += 1
        if count < 3:
            return 'No'
    if count < 3:
        return 'No'
    return 'Yes'

def main(n):
    # 生成测试数据：
    # 构造一棵有 n 个节点的树，节点 2..n 的父亲在 [1, i-1] 中随机选择，
    # 与原程序对 values 的含义（每个 i+2 的父节点）保持一致。
    if n < 2:
        # 原逻辑要求 n-1 个 parent 输入，n=1 时结构退化
        values = []
    else:
        values = [random.randint(1, i + 1) for i in range(n - 1)]
    gr = router(values)
    visited = [False] * (n + 1)
    result = christmas(gr, 1, visited)
    print(result)
    return result

if __name__ == "__main__":
    # 示例：运行规模为 10 的随机测试
    main(10)