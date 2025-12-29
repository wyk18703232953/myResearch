import random

def main(n: int):
    # 1. 生成测试数据
    # 代价 cost[1..4]：随机 1..10
    cost = [0] + [random.randint(1, 10) for _ in range(4)]
    # 4 行、n 列的字符网格，'.' 或 '*'
    a = [
        ''.join(random.choice(['.', '*']) for _ in range(n))
        for _ in range(4)
    ]

    # 2. 原算法逻辑
    mask = [0, 1, 51, 1911]
    inf, bs_size, full_bit = 10**9, 1 << 12, (1 << 12) - 1
    dp = [[inf] * bs_size for _ in range(4 * n + 1)]
    dp[0][0] = 0

    for i in range(4 * n):
        y, x = i & 3, i >> 2
        is_dot = 1 if a[y][x] == '.' else 0

        for bitset in range(bs_size):
            cur = dp[i][bitset]
            if cur == inf:
                continue

            if y == 0:
                if dp[i + 4][full_bit] > cur + cost[4]:
                    dp[i + 4][full_bit] = cur + cost[4]

            if (is_dot | (bitset & 1)) and dp[i + 1][bitset >> 1] > cur:
                dp[i + 1][bitset >> 1] = cur

            for k in range(1, min(4 - y, 3) + 1):
                nb = bitset | mask[k]
                if dp[i][nb] > cur + cost[k]:
                    dp[i][nb] = cur + cost[k]

    ans = min(dp[4 * n])

    # 输出：先输出生成的数据，方便检查；最后输出答案
    print("n:", n)
    print("cost[1..4]:", cost[1:])
    print("grid (4 x n):")
    for row in a:
        print(row)
    print("answer:", ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)