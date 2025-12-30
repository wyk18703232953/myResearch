#!/usr/bin/env python3
import random

def main(n, m=None, value_max=10**9, seed=0):
    """
    n: 行数（原程序中的 n）
    m: 列数（原程序中的 m），若为 None 则取 max(1, n // 2)
    value_max: 生成数据的最大值
    seed: 随机种子，方便复现
    """
    random.seed(seed)
    if m is None:
        m = max(1, n // 2)

    # 生成测试数据：n 行 m 列的随机整数矩阵
    array = [[random.randint(0, value_max) for _ in range(m)] for __ in range(n)]

    max_val = max(max(row) for row in array) if array else 0

    good = (1 << m) - 1
    l = 0
    r = max_val + 1
    a = 0
    b = 0

    while r - l > 1:
        mid = (l + r) // 2
        bit_array = dict()
        for k, line in enumerate(array):
            val = 0
            for i, item in enumerate(line):
                if item >= mid:
                    val |= 1 << i
            bit_array[val] = k

        ok = False
        i = j = 0
        keys = list(bit_array.keys())
        for key1 in keys:
            for key2 in keys:
                if key1 | key2 == good:
                    ok = True
                    i = bit_array[key1]
                    j = bit_array[key2]
                    break
            if ok:
                break

        if ok:
            a = i
            b = j
            l = mid
        else:
            r = mid

    print(a + 1, b + 1)


if __name__ == "__main__":
    # 示例：n=5，可自行修改参数测试
    main(5)