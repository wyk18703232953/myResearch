from collections import deque
import random

def main(n):
    # 生成一个包含 0..n 的树：
    # 强制加入边 (0,1)，剩余 2..n 每个随机连接到 [0..i-1] 中某个点
    graph = [set() for _ in range(n + 1)]
    graph[0].add(1)
    graph[1].add(0)
    for v in range(2, n + 1):
        u = random.randint(0, v - 1)
        graph[u].add(v)
        graph[v].add(u)

    # 生成一个 BFS 序列 a，以 0 为根
    # 与原逻辑一致：先把 root=0 放在队列里，从其子节点开始构造 a
    q = deque([0])
    par = [-1] * (n + 1)
    par[0] = 0
    bfs_order = []
    while q:
        v = q.popleft()
        children = [u for u in graph[v] if u != par[v]]
        random.shuffle(children)
        bfs_order.extend(children)
        for ch in children:
            par[ch] = v
            q.append(ch)

    a = bfs_order  # 对应原代码中的输入序列 a

    # 以下为原逻辑的验证部分
    q = deque()
    q.append(0)
    i = 0
    par = [0] * (n + 1)
    while len(q):
        v = q.popleft()
        graph[v].discard(par[v])
        l = len(graph[v])
        if graph[v] != set(a[i:i + l]):
            print("No")
            break
        for j in range(i, i + l):
            q.append(a[j])
            par[a[j]] = v
        i += l
    else:
        print("Yes")


if __name__ == "__main__":
    # 示例运行，可根据需要修改 n
    main(5)