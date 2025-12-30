import sys
from itertools import accumulate
import copy
import random

def main(n: int) -> None:
    # 生成测试数据
    # 这里随便构造一些数据，你可以按需要修改生成逻辑
    m = max(1, n // 3)          # 步长，保证 1 <= m <= n
    k = max(1, n // 5)          # 扣减值
    A = [random.randint(0, 10) for _ in range(n)]

    ANS = 0
    for i in range(m):
        B = copy.deepcopy(A)

        # 每隔 m 个元素从位置 i 开始减去 k
        for j in range(i, n, m):
            B[j] -= k

        SUM = list(accumulate(B))
        SUMMIN = [float("inf")] * n + [0]

        if i == 0:
            SUMMIN[0] = 0

        for j in range(max(1, i), n):
            if j % m == i % m:
                SUMMIN[j] = min(SUMMIN[j - 1], SUM[j - 1])
            else:
                SUMMIN[j] = SUMMIN[j - 1]

        for j in range(i, n):
            ANS = max(ANS, SUM[j] - SUMMIN[j])

    print(ANS)


if __name__ == "__main__":
    # 你可以在这里改动 n 来生成不同规模的测试
    main(10)