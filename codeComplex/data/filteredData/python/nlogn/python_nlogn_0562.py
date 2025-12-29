from collections import deque
import random

def main(n: int):
    # 1. 生成一棵含 n 个节点的随机树（节点编号 1..n）
    # 使用随机生成的父数组再打乱边顺序
    edges = []
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)
        edges.append((u, v))

    # 2. 构建邻接表
    l = [[] for _ in range(n + 1)]
    for a, b in edges:
        l[a].append(b)
        l[b].append(a)

    # 3. 生成一个 BFS 顺序作为 b（保证是合法的访问顺序）
    visited = [False] * (n + 1)
    order = []
    q = deque([1])
    visited[1] = True
    while q:
        x = q.popleft()
        order.append(x)
        for y in l[x]:
            if not visited[y]:
                visited[y] = True
                q.append(y)
    b = order[:]  # b 是要验证的序列

    # 4. 以下为原逻辑，只是把 input 替换为使用上面生成的数据
    visited = [False for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]

    s = [1]
    visited[1] = True
    c = 1
    c1 = 0
    t = True
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
                t = False
                break
        else:
            c += aux
            c1 += 1
            continue
        break
    if t:
        print("Yes")


# 示例调用
if __name__ == "__main__":
    main(10)