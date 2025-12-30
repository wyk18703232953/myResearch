from collections import deque
import random

def main(n):
    # 1. 生成测试数据：一棵 n 个节点的树 + 一个 BFS 序列（此处生成根为 1 的 BFS 序）
    # 生成随机树
    edges = []
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)
        edges.append((u, v))

    # 构建邻接表
    l = [[] for _ in range(n + 2)]
    for a, b in edges:
        l[a].append(b)
        l[b].append(a)

    # 生成从 1 开始的 BFS 序列，保证原算法答案为 "Yes"
    visited_gen = [False] * (n + 2)
    q = deque([1])
    visited_gen[1] = True
    bfs_seq = []
    while q:
        u = q.popleft()
        bfs_seq.append(u)
        for v in l[u]:
            if not visited_gen[v]:
                visited_gen[v] = True
                q.append(v)

    # 2. 使用原逻辑对生成的树和 BFS 序列进行验证
    visited = [False for _ in range(n + 2)]
    dp = [-1 for _ in range(n + 2)]

    # 重新构造邻接表（与生成时一致，实际可直接复用 l）
    # 这里直接使用已构造好的 l

    b = deque(bfs_seq)
    b.popleft()  # 去掉第一个 1
    s = deque([1])
    ans = "Yes"
    visited[1] = True

    while len(b) > 0 and len(s) > 0:
        aux = 0
        for i in l[s[0]]:
            if not visited[i]:
                visited[i] = True
                dp[i] = 1
                aux += 1
        for _ in range(aux):
            if not b:
                ans = "No"
                break
            x = b.popleft()
            if dp[x] == 1:
                s.append(x)
                dp[x] = -1
            else:
                ans = "No"
                b = []
                break
        s.popleft()

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)