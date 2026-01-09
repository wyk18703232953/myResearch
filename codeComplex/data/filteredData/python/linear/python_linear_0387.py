def main(n):
    # 解释规模含义：
    # n：原程序中的 n，同时也用来生成 m 以及后续测试数据规模
    #
    # 数据生成策略（完全确定性）：
    # - 将 m 设为 n（即有 n 组 (x, d)）
    # - 对于第 i 组：
    #     x_i = i
    #     d_i = (-1)**i * (i // 2 + 1)
    #   但为简化并保持整数运算、避免幂运算开销，用符号模式：
    #     i 偶数: d_i =  (i // 2 + 1)
    #     i 奇数: d_i = -(i // 2 + 1)

    m = n

    a = (n * (n - 1)) // 2
    n2 = n // 2
    b = n2 * (n2 + 1)
    if n % 2 == 0:
        b -= n2
    s = 0

    for i in range(m):
        x = i
        if i % 2 == 0:
            d = i // 2 + 1

        else:
            d = -(i // 2 + 1)

        s += x * n
        s += d * (a if d > 0 else b)

    # 返回结果而不是打印，便于在实验环境中多次调用
    return s / n


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 规模进行实验
    result = main(10)
    # print(result)
    pass