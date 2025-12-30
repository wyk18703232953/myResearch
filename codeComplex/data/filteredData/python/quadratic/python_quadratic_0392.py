from math import inf
import random


def main(n: int):
    # 为了生成规模为 n 的测试数据，这里构造一个 n x n 的棋盘
    # 保证至少有一个 'B'，并随机生成一个或多个 'B'
    m = n  # 原程序中 n 行 m 列，这里简单设 m = n
    li = [['W' for _ in range(m)] for _ in range(n)]

    # 随机选择若干个位置放置 'B'
    num_B = random.randint(1, max(1, n // 2))  # 至少 1 个，至多 n//2 个
    for _ in range(num_B):
        x = random.randint(0, n - 1)
        y = random.randint(0, m - 1)
        li[x][y] = 'B'

    # 以下为原逻辑
    min1 = inf
    min2 = inf
    max1 = -inf
    max2 = -inf

    for i in range(n):
        for j in range(m):
            if li[i][j] == "B":
                min1 = min(min1, i)
                min2 = min(min2, j)
                max1 = max(max1, i)
                max2 = max(max2, j)

    # 原程序输出坐标为 1-based
    center_i = (min1 + max1) // 2 + 1
    center_j = (min2 + max2) // 2 + 1

    print(center_i, center_j)


if __name__ == "__main__":
    # 可以在此处简单测试，例如 n=5
    main(5)