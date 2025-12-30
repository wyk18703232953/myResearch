# -*- coding: utf-8 -*-
"""
根据给定规模 n 生成测试数据 (l, r)，然后执行原算法逻辑：
如果 l == r 输出 0；
否则按原代码的二进制处理逻辑，输出 (2**sol) - 1。
"""

def main(n):
    # 1. 根据规模 n 生成测试数据 (l, r)
    # 生成 [0, n] 范围内的两个数，并保证 l <= r
    l = n // 3
    r = n
    if l > r:
        l, r = r, l

    # 2. 原算法逻辑（移除 input()，改为使用上面生成的 l, r）
    if l == r:
        print(0)
        return

    a = bin(l)
    b = bin(r)
    a = list(a[2:])
    b = list(b[2:])
    d = 0

    if len(a) != len(b):
        d = len(b) - len(a)
        acta = ['0'] * d
        for j in a:
            acta.append(j)
        a = acta

    sol = len(b)
    pos = -1
    for i in range(len(b) - 1, -1, -1):
        if a[i] != b[i]:
            pos = sol - i

    if pos != -1:
        sol = pos

    print((2 ** sol) - 1)


if __name__ == "__main__":
    # 示例：可以修改这里的 n 进行测试
    main(100)