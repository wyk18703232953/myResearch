def main(n: int):
    """
    n: 规模，用于生成测试数据 index。
       这里简单设为 index = n，确保为正整数。
    """
    index = max(1, int(n))  # 生成测试数据

    total = 9
    d = 1  # 当前位数

    # 找到 index 所在的位数区间
    while index > total:
        total += (d + 1) * (10 ** d) * 9
        d += 1

    last = 10 ** (d - 1)  # d 位数的起始数字
    total -= d * 9 * last  # 回退到 d 位数区间开始时的总位数
    index -= total          # 在 d 位数区间内的偏移（从 1 开始）

    r = index % d
    k = index // d

    number = last + k  # 对应的数字

    if r == 0:
        print(str(number - 1)[d - 1])
    else:
        print(str(number)[r - 1])


if __name__ == "__main__":
    # 示例：运行 main(100)
    main(100)