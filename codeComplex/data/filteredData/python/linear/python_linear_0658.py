def main(n):
    # 确定性构造：
    # 节点 1 为中心，其余 n-1 个节点与 1 相连，形成星形树
    # 这样叶子节点数量为 n-1，结构简单且确定
    # s 与 n 成线性关系，便于规模化（可根据需要调整）
    s = n * (n + 1) // 2

    a = [0] * (n + 1)

    if n == 2:
        # print(s)
        pass
        return

    # 构造 n-1 条边：1 与每个 i (2..n) 相连
    for v in range(2, n + 1):
        u = 1
        a[u] += 1
        a[v] += 1

    # print(2.0 * s / a.count(1))
    pass
if __name__ == "__main__":
    main(10)