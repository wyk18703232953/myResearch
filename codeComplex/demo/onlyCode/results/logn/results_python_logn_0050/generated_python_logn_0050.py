def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里将 a, b 生成在 [0, n) 范围内
    a = n
    b = n // 2

    k = 2 ** ((a ^ b).bit_length())
    print(k - 1)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)