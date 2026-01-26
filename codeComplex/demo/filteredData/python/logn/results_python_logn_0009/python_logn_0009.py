def main(n):
    # 在原程序中，输入是两个整数 a, b
    # 这里将 n 映射为 a 和 b，用确定性方式生成
    a = n
    b = n * 2 + 1

    bitxor = a ^ b

    res = 1
    while bitxor:
        bitxor >>= 1
        res <<= 1

    # print(res - 1)
    pass
if __name__ == "__main__":
    main(10)