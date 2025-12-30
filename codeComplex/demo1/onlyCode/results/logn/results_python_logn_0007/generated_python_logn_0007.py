def main(n: int):
    # 根据 n 生成测试数据，这里示例为：
    # a = n, b = n // 2
    a = n
    b = n // 2

    # 原逻辑：输出 (1 << (a ^ b).bit_length()) - 1
    result = (1 << (a ^ b).bit_length()) - 1
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)