from math import *
import random


def bin_search(arr, n):
    pos = -1
    # all nums < n
    for i in range(35, -1, -1):
        jump = (1 << i)
        if (pos + jump) >= len(arr):
            continue
        if arr[pos + jump] <= n - 1:
            pos += jump
    return len(arr) - pos - 1


def main(n):
    """
    n: 规模参数，用于生成测试数据
    这里约定：
      - 竖直线段数量 = n
      - 水平线段数量 = n
    生成规则可以根据需要修改
    """
    # 生成竖直线段位置 vert
    # 随机生成 n 个在 [1, 1e9] 内的位置
    vert = [random.randint(1, 10**9) for _ in range(n)]

    # 生成水平线段（只保留 col1 == 1 的行）
    # 原逻辑中只使用 col2，且要求 col1 == 1
    # 这里生成 n 个水平线段，col1 固定为 1
    # col2 和 row 随机生成，但实际只用到 col2
    hor = []
    for _ in range(n):
        col1 = 1
        col2 = random.randint(1, 10**9)
        row = random.randint(1, 10**9)  # 保留变量以体现原结构
        if col1 != 1:
            continue
        hor.append(col2)

    vert.append(1000000000)
    vert = sorted(vert)
    hor = sorted(hor)

    best = int(1e10)
    for i in range(len(vert)):
        cur_ans = bin_search(hor, vert[i]) + i
        best = min(best, cur_ans)

    print(best)


if __name__ == "__main__":
    # 可在此指定规模参数进行测试
    main(10)