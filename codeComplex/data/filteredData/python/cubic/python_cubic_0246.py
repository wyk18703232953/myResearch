from math import *
from collections import *
from random import *
from decimal import Decimal
from heapq import *
from bisect import *
import sys


def main(n: int):
    """
    n 为规模参数，用来生成 r, g, b 以及对应长度的数组。
    这里采用一种简单的生成策略：
    - r, g, b 为 1..n 范围内的随机数
    - rl, gl, bl 中的元素为 1..10^3 范围内的随机整数
    """
    # 为了可重复性，这里固定随机种子；如需真实随机可删掉下一行
    seed(0)

    # 生成 r, g, b，至少为 1
    r = randint(1, n)
    g = randint(1, n)
    b = randint(1, n)

    # 生成测试数据
    rl = [randint(1, 1000) for _ in range(r)]
    gl = [randint(1, 1000) for _ in range(g)]
    bl = [randint(1, 1000) for _ in range(b)]

    rl.sort()
    gl.sort()
    bl.sort()

    # DP 三维数组：dp[i][j][k] 表示使用前 i 个红、j 个绿、k 个蓝时的最大值
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i + j + k < 2:
                    continue
                if i and j:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j - 1][k] + rl[i - 1] * gl[j - 1])
                if j and k:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i][j - 1][k - 1] + gl[j - 1] * bl[k - 1])
                if i and k:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j][k - 1] + rl[i - 1] * bl[k - 1])

    print(dp[r][g][b])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)