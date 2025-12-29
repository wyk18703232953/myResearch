def main(n):
    import random

    # 生成测试数据：n×n 概率矩阵 a[i][j]，i 吃 j 的概率，行内归一化
    a = [[0.0] * n for _ in range(n)]
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0.0)
            else:
                row.append(random.random())
        s = sum(row)
        if s == 0:
            # 若这一行全是 0，则平均分配给其他鱼
            for j in range(n):
                if i != j:
                    a[i][j] = 1.0 / (n - 1)
        else:
            for j in range(n):
                a[i][j] = row[j] / s

    def count_bits(x):
        cnt = 0
        for i in range(n):
            if ((1 << i) & x):
                cnt += 1
        return cnt

    dp = [0.0 for _ in range(1 << n)]  # dp[mask]：当前存活集合为 mask 的概率
    dp[-1] = 1.0  # 初始状态：所有鱼都存活

    for mask in range((1 << n) - 1, -1, -1):
        val = count_bits(mask)
        if val < 2:
            continue
        total = val * (val - 1) // 2
        for i in range(n):
            if (mask & (1 << i)) == 0:
                continue
            for j in range(n):
                if (mask & (1 << j)) == 0 or i == j:
                    continue
                dp[mask ^ (1 << j)] += dp[mask] * a[i][j] / total

    for i in range(n):
        print(dp[1 << i])


if __name__ == "__main__":
    # 示例：n=4，可根据需要修改
    main(4)