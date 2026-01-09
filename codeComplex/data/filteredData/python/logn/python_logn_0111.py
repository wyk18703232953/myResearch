# -*- coding: utf-8 -*-

def main(n: int):
    """
    规模 n 用来生成测试数据 (l, r)，你可以根据需要修改生成方式。
    这里示例为：
        l = 0
        r = (1 << n) - 1   # n 位全为 1 的数
    """
    # 生成测试数据
    l = 0
    r = (1 << n) - 1

    # 以下为原逻辑的无 input() 封装
    if l == r:
        # print(0)
        pass
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

    # print((2 ** sol) - 1)
    pass


# 示例：直接运行本文件时，给一个默认的 n
if __name__ == "__main__":
    main(5)