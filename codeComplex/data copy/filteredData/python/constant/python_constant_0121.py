def main(n):
    # 原逻辑：对给定的 n 进行处理并输出结果
    a = str(n)
    m = len(a)
    if m == 1:
        # 当 n 为一位数时，原程序中 b 和 c 的构造会出错，这里直接输出 n
        # print(n)
        pass
        return

    # 按原逻辑构造 b 和 c
    b = int(a[0:m-1])  # 去掉最后一位
    if m == 2:
        # 当长度为 2 时，a[0:m-2] 为空串，按原代码等价于只取最后一位
        c = int(a[-1])

    else:
        c = int(a[0:m-2] + a[-1])  # 去掉倒数第二位，用最后一位替换

    d = max(n, b, c)
    # print(d)
    pass
if __name__ == "__main__":
    # 根据规模 n 生成测试数据，这里简单示例：使用 n 本身作为待处理的数字
    # 你也可以根据需要，用 n 生成更复杂的测试数据
    test_n = 10 ** (n - 1) + 123  # 例如生成一个 n 位数（首位非 0）
    main(test_n)