def main(n):
    # 解释输入规模到 (n_nodes, d, k) 的映射：
    # 保持完全确定性，给出一组在规模上随 n 变化的参数。
    #
    # n_nodes: 节点数（原程序里的 n）
    # d: 要求的直径
    # k: 最大度数
    #
    # 这里选取一种简单且确定性的构造：
    # - n_nodes = max(1, n)
    # - d = min(max(1, n_nodes // 4), n_nodes - 1)  （保证 1 <= d <= n_nodes-1）
    # - k = max(2, min(5, n_nodes))  （度数不小于 2，让算法更有机会成功）
    #
    # 这样随 n 增大，图规模增大，d 和 k 也在可控范围内变化，适合做时间复杂度实验。
    n_nodes = max(1, n)
    if n_nodes == 1:
        # 特殊情况：只有 1 个点时，原始程序要求 d+1 <= n，否则 NO。
        # 对 n_nodes=1，必然 NO，这里直接输出。
        print("NO")
        return

    d = n_nodes // 4
    if d < 1:
        d = 1
    if d >= n_nodes:
        d = n_nodes - 1

    k = max(2, min(5, n_nodes))

    # 以下是原始算法逻辑，只是把输入的 n, d, k 换成生成的 n_nodes, d, k
    n_val = n_nodes

    if d + 1 > n_val:
        print("NO")
        return

    ans = []
    dist = [0] * n_val
    deg = [0] * n_val
    for i in range(d + 1):
        if i == 0 or i == d:
            deg[i] = 1
        else:
            deg[i] = 2
        if i != d:
            ans.append((i + 1, i + 2))
        dist[i] = max(i, d - i)

    for i in range(n_val):
        if deg[i] > k:
            print("NO")
            return

    from collections import deque
    q = deque(list(range(d + 1)))
    cur = d + 1
    while q and cur < n_val:
        v = q.pop()
        if dist[v] < d and deg[v] < k:
            deg[v] += 1
            dist[cur] = dist[v] + 1
            deg[cur] = 1
            ans.append((v + 1, cur + 1))
            q.append(v)
            q.append(cur)
            cur += 1
        else:
            continue
    if cur != n_val:
        print("NO")
    else:
        print("YES")
        for edge in ans:
            print(edge[0], edge[1])


if __name__ == "__main__":
    # 示例：使用 n=20 进行一次运行
    main(20)