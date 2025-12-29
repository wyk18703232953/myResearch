import random
import sys

def main(n):
    # 规模参数：n
    # 原程序需要 n, m, k，这里根据 n 生成：
    m = n                 # 例如设为正方形网格
    k = 2 * n             # 例如设为偶数步，保证可走回（可自行调整）

    # 生成测试数据：边权均为 1~10 的随机整数
    hor = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    ver = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    # dp 逻辑与原程序一致
    if k % 2:
        for _ in range(n):
            print(*([-1] * m))
        return

    half_k = k // 2
    dp = [[[0] * m for _ in range(n)] for _ in range(half_k + 1)]

    for x in range(1, half_k + 1):
        for y in range(n):
            for z in range(m):
                hold = float('inf')
                if y != 0:
                    hold = min(hold, dp[x - 1][y - 1][z] + ver[y - 1][z])
                if y != n - 1:
                    hold = min(hold, dp[x - 1][y + 1][z] + ver[y][z])
                if z != 0:
                    hold = min(hold, dp[x - 1][y][z - 1] + hor[y][z - 1])
                if z != m - 1:
                    hold = min(hold, dp[x - 1][y][z + 1] + hor[y][z])
                dp[x][y][z] = hold

    for row in dp[half_k]:
        print(*map(lambda i: i * 2, row))


if __name__ == "__main__":
    # 示例：可以修改这里的 n 进行测试
    main(5)