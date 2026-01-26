def main(n):
    # 根据 n 生成确定性输入数据
    # A, B, x, y, z 的构造都只依赖于 n
    A = n
    B = 2 * n
    x = n + 1
    y = n // 2
    z = n % 5

    A1 = 2 * x + y - A
    B1 = 3 * z + y - B
    final = 0
    if A1 > 0:
        final = final + A1
    if B1 > 0:
        final = final + B1
    # print(final)
    pass
if __name__ == "__main__":
    main(10)