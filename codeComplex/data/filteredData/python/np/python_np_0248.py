import random

def main(n: int):
    # 1. 生成测试数据
    # n: 点的数量
    # m: 选取的点的数量（1 <= m <= n）
    # k: 有权边的数量（0 <= k <= n*(n-1)）
    #
    # 这里给出一种合理的随机生成方式，你可以按需要修改：
    m = max(1, n // 2)          # 例如取一半节点
    k = min(n * (n - 1), n * 2) # 较稀疏的有权边

    # 节点权值 a[i] 为 1~10 的随机浮点数
    a = [float(random.randint(1, 10)) for _ in range(n)]

    # tree[i][j] 为 i->j 的额外边权，初始化为 0
    tree = [[0.0] * n for _ in range(n)]
    edges = set()
    # 随机选 k 条有权边（允许有重复尝试，不重复计数）
    while len(edges) < k and len(edges) < n * (n - 1):
        x = random.randint(1, n)
        y = random.randint(1, n)
        if x == y:
            continue
        if (x, y) in edges:
            continue
        edges.add((x, y))
        z = float(random.randint(1, 10))
        tree[x - 1][y - 1] = z

    # 2. 原算法逻辑（去掉 input 部分，直接使用上面生成的数据）
    po = [1]
    while len(po) != n:
        po.append(po[-1] * 2)

    dp = [[0.0] * (po[-1] * 2) for _ in range(n)]
    for i in range(n):
        dp[i][po[i]] = a[i]

    for mask in range(po[-1] * 2):
        for j in range(n):
            if mask & po[j]:
                for k_idx in range(n):
                    if not (mask & po[k_idx]):
                        new_mask = mask + po[k_idx]
                        val = dp[j][mask] + a[k_idx] + tree[j][k_idx]
                        if val > dp[k_idx][new_mask]:
                            dp[k_idx][new_mask] = val

    ma = 0.0
    for mask in range(po[-1] * 2):
        if bin(mask).count("1") == m:
            for j in range(n):
                if dp[j][mask] > ma:
                    ma = dp[j][mask]

    print(int(ma))


if __name__ == "__main__":
    # 示例运行：规模 n = 10
    main(10)