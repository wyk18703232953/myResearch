import random

def main(n: int):
    # 生成测试数据
    # n: 点的数量
    # m: 选择的点数量（保证 1 <= m <= n）
    m = random.randint(1, n)

    # a[i]: 访问点 i 的收益（浮点数）
    a = [round(random.uniform(0, 10), 2) for _ in range(n)]

    # k: 有权边的数量（0 到 n^2 之间）
    k = random.randint(0, n * n)
    tree = [[0.0] * n for _ in range(n)]
    for _ in range(k):
        x = random.randint(1, n)
        y = random.randint(1, n)
        z = round(random.uniform(-5, 5), 2)  # 边权可以正也可以负
        tree[x - 1][y - 1] = float(z)

    # 下面是原 main() 的逻辑，使用上面生成的 n, m, a, tree, k

    po = [1]
    while len(po) != n:
        po.append(po[-1] * 2)
    dp = [[0.0] * (po[-1] * 2) for _ in range(n)]
    for i in range(n):
        dp[i][po[i]] = a[i]
    for mask in range(po[-1] * 2):
        for j in range(n):
            if mask & po[j]:
                for k2 in range(n):
                    if not (mask & po[k2]):
                        new_mask = mask + po[k2]
                        val = dp[j][mask] + a[k2] + tree[j][k2]
                        if val > dp[k2][new_mask]:
                            dp[k2][new_mask] = val
    ma = 0.0
    for mask in range(po[-1] * 2):
        if bin(mask).count("1") == m:
            for j in range(n):
                if dp[j][mask] > ma:
                    ma = dp[j][mask]

    print(int(ma))


if __name__ == "__main__":
    # 示例：以 n = 5 运行
    main(5)