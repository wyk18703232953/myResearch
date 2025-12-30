import random

def main(n):
    # 1. 生成测试数据 p：n×n 的随机概率矩阵，p[i][i] = 0，p[j][i] = 1 - p[i][j]
    # 你可以根据需要修改生成规则
    random.seed(0)
    p = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            prob = random.random()
            p[i][j] = prob
            p[j][i] = 1.0 - prob

    # 2. 按原逻辑计算 dp
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

    ans = [dp[1 << i] for i in range(n)]
    print(*ans)


if __name__ == "__main__":
    # 示例：运行规模 n=4
    main(4)