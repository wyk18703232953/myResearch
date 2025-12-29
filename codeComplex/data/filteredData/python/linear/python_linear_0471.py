def main(n: int):
    """
    根据规模 n 自动生成测试数据并执行原逻辑：
    - c: 每个节点的成本，取值范围 [1, 10^9]
    - a: 每个节点指向的下一个节点（0~n-1），保证每个点出度为 1
    """
    import random

    # 固定随机种子便于复现，如需不同数据可注释下一行
    random.seed(0)

    # 生成测试数据
    # 成本数组 c
    c = [random.randint(1, 10**9) for _ in range(n)]

    # 生成一个随机函数图（每个点恰有一个出边）
    # 先构造若干随机环，再把剩余点随便指向已有点，保证有环结构
    a = [None] * n
    nodes = list(range(n))
    random.shuffle(nodes)

    idx = 0
    # 随机分组形成环
    while idx < n:
        # 环的大小至少为1
        cycle_size = random.randint(1, min(5, n - idx))  # 控制环不会太大以增加多样性
        cycle_nodes = nodes[idx:idx + cycle_size]
        idx += cycle_size
        for i in range(len(cycle_nodes)):
            a[cycle_nodes[i]] = cycle_nodes[(i + 1) % len(cycle_nodes)]

    # 若仍有 None（理论上不会有，但以防万一）
    for i in range(n):
        if a[i] is None:
            a[i] = random.randrange(n)

    # ---- 原逻辑开始 ----
    vis = [-1] * n
    ans = 0
    for i in range(n):
        ind = i
        while vis[ind] == -1:
            vis[ind] = i
            ind = a[ind]
        if vis[ind] == i:
            start = ind
            ind = a[ind]
            cost = c[start]
            while ind != start:
                cost = min(cost, c[ind])
                ind = a[ind]
            ans += cost
    print(ans)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)