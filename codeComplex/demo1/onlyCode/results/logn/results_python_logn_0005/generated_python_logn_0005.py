def main(n: int):
    """
    n 为规模参数，这里用来生成测试数据：
    设 a = n, b = 2 * n
    """
    a = n
    b = 2 * n

    if a == b:
        print(0)
    else:
        x = a ^ b
        c = 1
        while x:
            x >>= 1
            c <<= 1
        print(c - 1)


if __name__ == "__main__":
    # 示例：可修改这里的 n 进行测试
    main(10)