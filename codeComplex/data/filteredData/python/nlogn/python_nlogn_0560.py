import sys
from collections import deque
import random

def main(n):
    # 1. 生成一棵包含 n 个节点的随机树
    # 用简单的随机生成：对每个 2..n 随机连到 [1, i-1] 之间的某个点
    l = [[] for _ in range(n + 1)]
    edges = []
    for i in range(2, n + 1):
        p = random.randint(1, i - 1)
        l[p].append(i)
        l[i].append(p)
        edges.append((p, i))

    # 2. 生成一个序列 b：要成为 BFS 顺序
    # 我们先实际做一次 BFS，得到一个合法的 BFS 序列，然后也可以选择打乱同层顺序
    def bfs_order(start=1):
        visited = [False] * (n + 1)
        q = deque([start])
        visited[start] = True
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            # 同层子结点顺序可随机打乱
            neighbors = l[u][:]
            random.shuffle(neighbors)
            for v in neighbors:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        return order

    # 得到一个 BFS 顺序 b
    b = bfs_order(1)

    # 3. 按原逻辑验证序列 b 是否是该树的一种 BFS 顺序
    visited = [False for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]

    s = [1]
    visited[1] = True
    c = 1
    c1 = 0

    ok = True
    while len(s) != n:
        aux = 0
        for i in l[s[c1]]:
            if not visited[i]:
                visited[i] = True
                dp[i] = 1
                aux += 1
        for i in range(c, c + aux):
            if dp[b[i]] == 1:
                s.append(b[i])
                dp[b[i]] = 0
            else:
                ok = False
                break
        if not ok:
            break
        c += aux
        c1 += 1

    if ok:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)