from collections import deque
import random

def bfs(s, n, G):
    q = deque()
    q.append(s)
    dist = [-1] * (n + 1)
    dist[s] = 0
    p = []
    parent = [1] * (n + 1)
    ok = [0] * (n + 1)
    while q:
        i = q.popleft()
        d = dist[i]
        if d < 3:
            ok[i] = 1
        p.append(i)
        for j in G[i]:
            if dist[j] == -1:
                q.append(j)
                dist[j] = d + 1
                parent[j] = i
    ans = 0
    while p:
        i = p.pop()
        j = parent[i]
        if not ok[i]:
            ok[j] = 1
            ans += 1
            for k in G[j]:
                ok[k] = 1
    return ans

def generate_tree(n):
    """
    生成一个随机树：
    对于每个节点 i (2..n)，随机连接到 [1..i-1] 中的一个节点。
    """
    G = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        G[parent].append(i)
        G[i].append(parent)
    return G

def main(n):
    # 生成规模为 n 的测试数据（树）
    G = generate_tree(n)
    # 以 1 为根运行 bfs 逻辑
    ans = bfs(1, n, G)
    print(ans)

if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)