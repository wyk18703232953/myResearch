import random
from collections import deque

def main(n: int):
    # 1. 生成一棵 n 个节点的随机树（节点编号 1..n）
    # 使用随机父节点方式生成树
    edges = []
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)
        edges.append((u, v))

    # 建立邻接表
    l = [[] for _ in range(n + 1)]
    for a, b in edges:
        l[a].append(b)
        l[b].append(a)

    # 2. 生成 b 序列（一个 1..n 的排列）
    # 为了更经常得到 "Yes"，我们可以从 BFS 序列随机打乱同层节点顺序
    def generate_bfs_like_sequence():
        visited = [False] * (n + 1)
        order = []
        q = deque([1])
        visited[1] = True
        while q:
            size = len(q)
            layer = []
            for _ in range(size):
                node = q.popleft()
                order.append(node)
                for nei in l[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        layer.append(nei)
            random.shuffle(layer)
            q.extend(layer)
        return order

    b = generate_bfs_like_sequence()

    # 3. 按原始逻辑进行判断
    visited = [False for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]

    s = [1]
    visited[1] = True
    c = 1
    c1 = 0
    t = True

    while len(s) != n:
        aux = 0
        # 将当前节点 s[c1] 的未访问邻居标记
        for i in l[s[c1]]:
            if not visited[i]:
                visited[i] = True
                dp[i] = 1
                aux += 1

        # 从 b 的当前位置开始，取 aux 个节点
        for i in range(c, c + aux):
            if dp[b[i]] == 1:
                s.append(b[i])
                dp[b[i]] = 0
            else:
                print("No")
                t = False
                break
        else:
            c += aux
            c1 += 1
            continue
        break

    if t:
        print("Yes")

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)