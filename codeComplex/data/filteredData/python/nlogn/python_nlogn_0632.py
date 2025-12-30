import random
import sys


def main(n):
    # 1. 生成规模参数相关的 m（1 <= m <= n）
    if n <= 0:
        return
    m = random.randint(1, n)

    # 2. 生成 x 和 t
    #   - 原程序要求 len(x) = len(t) = n + m
    #   - t 中有 m 个 1，其余为 0（表示 m 个“中心”，其余是“点”）
    length = n + m

    # 生成严格递增或随机序的坐标 x（这里用非降序以便更贴近一般题目）
    x = sorted(random.randint(0, 10 * n) for _ in range(length))

    # 生成 t：包含恰好 m 个 1，剩下的是 0
    t = [1] * m + [0] * (length - m)
    random.shuffle(t)

    # 3. 以下是原逻辑的封装，无 input()
    if m == 1:
        print(n)
        return

    p = []
    tx = []
    for i in range(n + m):
        (tx if t[i] == 1 else p).append(x[i])

    a = [0] * m
    i = 0
    for pi in p:
        while i < m - 1 and pi > (tx[i] + tx[i + 1]) / 2:
            i += 1
        a[i] += 1

    print(" ".join(str(ai) for ai in a))


if __name__ == "__main__":
    # 示例：用一个固定的 n 运行
    main(10)