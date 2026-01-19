def main(n):
    # 构造一个 n x n 的概率矩阵 p，满足 p[i][i] = 0 且 p[i][j] + p[j][i] = 1
    # 使用完全确定性的算术规则生成
    if n <= 0:
        print()
        return

    p = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0.0)
            elif i < j:
                # 通过简单算术函数构造 [0,1] 内的确定性概率
                val = ((i + 1) * (j + 2)) % 1001 / 1000.0
                row.append(val)
            else:
                # 保证 p[i][j] + p[j][i] = 1
                row.append(1.0 - p[j][i])
        p.append(row)

    full_bit = (1 << n) - 1
    dp = [0.0] * full_bit + [1.0]

    for i in range(full_bit, 0, -1):
        cunt = bin(i)[2:].count('1')
        if cunt == 1 or dp[i] == 0:
            continue

        mul = 1.0 / ((cunt * (cunt - 1)) >> 1)

        for x in range(n):
            if (i & (1 << x)) == 0:
                continue
            for y in range(x + 1, n):
                if (i & (1 << y)) == 0:
                    continue

                dp[i - (1 << y)] += dp[i] * p[x][y] * mul
                dp[i - (1 << x)] += dp[i] * p[y][x] * mul

    ans = []
    for i in range(n):
        ans.append(dp[1 << i])

    print(*ans)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以做规模实验
    main(5)