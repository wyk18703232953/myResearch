from collections import deque
import random

def main(n: int):
    # 1. 生成一棵以 1 为根的随机树，并生成其 BFS 序列 b
    # 生成树（无向、连通、n 个节点）
    adj = [[] for _ in range(n + 1)]
    parents = [0] * (n + 1)
    parents[1] = -1
    for v in range(2, n + 1):
        # 随机选择一个已有节点作为父节点
        p = random.randint(1, v - 1)
        parents[v] = p
        adj[p].append(v)
        adj[v].append(p)

    # 根据这棵树生成一个合法的 BFS 序列
    b = []
    q = deque([1])
    visited_gen = [False] * (n + 1)
    visited_gen[1] = True
    while q:
        u = q.popleft()
        b.append(u)
        # 随机打乱子节点的访问顺序以生成任一合法 BFS 序
        children = [v for v in adj[u] if not visited_gen[v]]
        random.shuffle(children)
        for v in children:
            visited_gen[v] = True
            q.append(v)

    # 2. 使用原逻辑判断 b 是否是图 adj 的 BFS 序列

    visited = [False for _ in range(n + 2)]
    dp = [-1 for _ in range(n + 2)]
    l = adj  # 保持原变量名

    b_deque = deque(b)
    b_deque.popleft()  # 原代码中将第一个元素(应为1)弹出
    s = deque([1])
    visited[1] = True

    ok = True
    while len(b_deque) > 0 and len(s) > 0:
        aux = 0
        for i in l[s[0]]:
            if not visited[i]:
                visited[i] = True
                dp[i] = 1
                aux += 1
        for _ in range(aux):
            if not b_deque:  # 理论上不会发生，防御性判断
                ok = False
                break
            x = b_deque.popleft()
            if dp[x] == 1:
                s.append(x)
                dp[x] = -1
            else:
                ok = False
                break
        if not ok:
            break
        s.popleft()

    if ok:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # 示例：可自行修改 n 的大小进行测试
    main(10)