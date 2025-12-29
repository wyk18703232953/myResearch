def main(n: int):
    # 这里将 n 用作 a, b 的规模来源：例如 a = n, b = n // 2
    # 可根据需要修改为其他生成方式
    a = n
    b = n // 2

    k = 2 ** (a ^ b).bit_length() - 1
    print(k)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)