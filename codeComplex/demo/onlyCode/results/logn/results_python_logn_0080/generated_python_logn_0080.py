def main(n: int):
    """
    使用规模 n 生成测试区间 [l, r]，并计算区间内任意一对数的最大 XOR 值。

    这里将测试数据设为：
    l = 0
    r = n

    返回最大 XOR 值。
    """
    l = 0
    r = n

    xor = l ^ r

    bms = 0
    while xor != 0:
        bms = bms + 1
        xor = xor >> 1

    maxxor = 0
    dois = 1
    while bms != 0:
        maxxor = maxxor + dois
        dois = dois << 1
        bms = bms - 1

    print(maxxor)


if __name__ == "__main__":
    # 示例：可修改 n 测试不同规模
    main(10)