def main(n):
    # 1. 根据 n 生成测试数据 a（任意合理的概率矩阵）
    # 这里生成一个随机但“像样”的概率矩阵：a[i][j] + a[j][i] = 1, a[i][i] = 0
    import random
    random.seed(0)

    a = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            p = random.random()
            a[i][j] = p
            a[j][i] = 1.0 - p

    def count_bits(x):
        value = 0
        while x:
            x &= x - 1
            value += 1
        return value

    def nc2(x):
        return (x * (x - 1)) // 2

    def answer(n, a):
        dp = [0.0] * (1 << n)
        # 初始状态：所有鱼都活着
        dp[(1 << n) - 1] = 1.0

        for mask in range((1 << n) - 1, 0, -1):
            m = count_bits(mask)  # 当前存活鱼的数量
            if m == 1:
                continue

            # 随机选出两条活鱼的总概率为 1，单对的权重为 p
            p = 1.0 / nc2(m)

            # 枚举有序对 (i, j)，i 吃 j
            for i in range(n):
                if not (mask >> i) & 1:
                    continue
                for j in range(n):
                    if i == j:
                        continue
                    if (mask >> j) & 1:
                        next_mask = mask ^ (1 << j)
                        dp[next_mask] += dp[mask] * p * a[i][j]

        # 输出每条鱼最后存活的概率
        for i in range(n):
            print(dp[1 << i], end=' ')
        print()

    answer(n, a)


# 示例调用：
# main(3)