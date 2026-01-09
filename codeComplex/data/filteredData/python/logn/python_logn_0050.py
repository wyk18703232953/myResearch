def main(n: int):
    """
    n: 规模参数，用于生成测试数据 (a, b)
    这里简单生成 a = n, b = 2*n 作为示例测试数据。
    """
    a = n
    b = 2 * n

    k = 2 ** (a ^ b).bit_length()
    # print(k - 1)
    pass
if __name__ == "__main__":
    # 可以在此处修改 n 来进行不同规模的测试
    main(10)