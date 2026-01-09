def main(n):
    # n 表示测试用例数量
    c = []
    for i in range(n):
        # 为第 i 个测试用例构造确定性 (a, b)
        # 保证 a, b > 0，且随 n、i 变化但完全可预测
        a = (i + 2) * 3
        b = (i + 3) * 5

        z4 = 0
        while a != 0 and b != 0:
            z1 = z3 = 0
            if a <= b:
                z = (b / a)
                z1 = int(z)
                b = b - (z1 * a)
            if b <= a and b != 0:
                z2 = a / b
                z3 = int(z2)
                a = a - (z3 * b)
            z4 = z4 + z1 + z3
        c.append(z4)

    for val in c:
        # print(val)
        pass
if __name__ == "__main__":
    # 示例：以 n=5 作为输入规模运行一次
    main(5)