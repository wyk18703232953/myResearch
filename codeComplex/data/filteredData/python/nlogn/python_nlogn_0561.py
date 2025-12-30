import sys
from collections import deque
import random

def main(n: int):
    # 1. 生成一棵 n 个节点的随机树
    # 使用随机 Prüfer 序列生成树，然后转换为边集
    if n <= 0:
        return

    if n == 1:
        # 只有一个节点时，任意 BFS 序列都是 [1]
        print("Yes")
        return

    # 生成 Prüfer 序列
    prufer = [random.randint(1, n) for _ in range(n - 2)]
    degree = [1] * (n + 1)
    for x in prufer:
        degree[x] += 1

    # 利用 Prüfer 序列生成边
    l = [[] for _ in range(n + 1)]
    import heapq
    heap = []
    for i in range(1, n + 1):
        if degree[i] == 1:
            heapq.heappush(heap, i)

    for x in prufer:
        u = heapq.heappop(heap)
        v = x
        l[u].append(v)
        l[v].append(u)
        degree[u] -= 1
        degree[v] -= 1
        if degree[v] == 1:
            heapq.heappush(heap, v)

    # 剩余两个点连接
    u = heapq.heappop(heap)
    v = heapq.heappop(heap)
    l[u].append(v)
    l[v].append(u)

    # 2. 生成一个合法的 BFS 序列 b（原代码的 b）
    # 从节点 1 做 BFS，并将每层节点随机打乱
    visited_gen = [False] * (n + 1)
    b = []
    q = deque([1])
    visited_gen[1] = True

    while q:
        layer = []
        for _ in range(len(q)):
            node = q.popleft()
            layer.append(node)
        random.shuffle(layer)
        for node in layer:
            b.append(node)
            for nei in l[node]:
                if not visited_gen[nei]:
                    visited_gen[nei] = True
                    q.append(nei)

    # 3. 使用原始逻辑对生成的树和 BFS 序列进行检验
    visited = [False for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]
    s = [1]
    visited[1] = True
    c = 1
    c1 = 0

    # b[0] 必须是 1，否则原程序会越界或直接判 "No"
    if b[0] != 1:
        print("No")
        return

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
                print("No")
                return
        c += aux
        c1 += 1

    print("Yes")


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)