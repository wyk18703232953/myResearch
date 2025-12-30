# -*- coding: utf-8 -*-
"""
基于原始逻辑的无 input() 版本，封装为 main(n)。
根据 n 生成测试数据 (k, m) 对，并输出结果。
"""

import random

def main(n):
    # 生成测试数据：
    # 这里示例生成 n 个 (k, m) 对，k 为 0~10*n 的随机整数，m 为 1~n 的随机整数
    # 可根据需要修改数据生成策略
    l = []
    for _ in range(n):
        k = random.randint(0, 10 * n)
        m = random.randint(1, n)
        l.append((k, m))

    # 与原程序一致的排序逻辑
    l.sort(key=lambda x: x[0] + x[1])

    last = 0
    ans = 1

    for i in range(1, n):
        if (l[i][0] - l[i][1] >= l[last][0] - l[last][1] and
            abs(l[i][0] - l[last][0]) >= l[i][1] + l[last][1]):
            last = i
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(10)