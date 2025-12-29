import random

def main(n: int):
    # 1. 构造一棵 n 个节点的随机树（1..n）
    graph = [set() for _ in range(n + 2)]
    parents = [0] * (n + 1)
    for v in range(2, n + 1):
        p = random.randint(1, v - 1)
        graph[p].add(v)
        graph[v].add(p)
        parents[v] = p

    # 2. 随机生成一个 BFS 合法序列（可以保证答案为 Yes）
    #    简单做法：从 1 开始，打乱每一层子节点顺序
    bfs_order = []
    q = [1]
    bfs_order.append(1)
    head = 0
    while head < len(q):
        v = q[head]
        head += 1
        children = [u for u in graph[v] if u != parents[v]]
        random.shuffle(children)
        for u in children:
            bfs_order.append(u)
            q.append(u)

    # 3. 根据 bfs_order 模拟原程序逻辑进行判断
    graph_check = [set(nei) for nei in graph]  # 拷贝一份用于检测
    a_iter = iter(bfs_order)

    try:
        assert next(a_iter) == 1  # 序列必须以 1 开头
        q = [1]
        for v in q:
            gv = graph_check[v]
            gv1 = tuple(gv)
            for _ in gv1:
                u = next(a_iter)
                assert u in gv
                gv.remove(u)
                graph_check[u].remove(v)
                q.append(u)
        print("Yes")
    except (AssertionError, StopIteration):
        print("No")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)