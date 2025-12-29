import random

def main(n):
    # 1. 生成一棵规模为 n 的随机树（1 为根）
    # parent[i] 为结点 i 的父亲（i >= 2）
    parents = [0] * (n + 1)
    for i in range(2, n + 1):
        parents[i] = random.randint(1, i - 1)

    if n == 1:
        print(1)
        return

    # 2. 用与原代码相同的方式构建邻接表
    adj = [[] for _ in range(n + 10)]
    for i in range(2, n + 1):
        pi = parents[i]
        adj[i].append(pi)
        adj[pi].append(i)

    # 3. 原逻辑：BFS 生成 disco 序列
    num = 1
    curr = [1]
    nextcurr = []
    disco = [1]
    visited = {1: True}
    while num < n:
        for v in curr:
            for w in adj[v]:
                if w not in visited:
                    nextcurr.append(w)
                    visited[w] = True
                    disco.append(w)
                    num += 1
        curr = nextcurr
        nextcurr = []

    # 4. 原逻辑：自底向上的 nl 与 nlvals 计算
    nl = {}
    nlvals = {}
    for v in disco[::-1]:
        nl[v] = max(sum(nl.get(w, 0) for w in adj[v]), 1)
        nlvals[nl[v]] = nlvals.get(nl[v], 0) + 1

    # 5. 原逻辑：colors 前缀和
    colors = {}
    leaves = nlvals[1]
    colors[1] = leaves
    for c in range(2, leaves + 1):
        colors[c] = colors[c - 1] + nlvals.get(c, 0)

    # 6. 原逻辑：生成答案
    ans = []
    j = 1
    for i in range(1, n + 1):
        while colors[j] < i:
            j += 1
        ans.append(str(j))
    print(' '.join(ans))


# 示例调用（提交时可去掉或保留）
if __name__ == "__main__":
    main(10)