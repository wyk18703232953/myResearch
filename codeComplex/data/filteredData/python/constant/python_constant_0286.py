def main(n: int):
    # 这里的 n 直接作为规模使用
    result = (n // 2) + 1
    print(result)


if __name__ == "__main__":
    # 根据规模生成测试数据，这里直接使用规模 n 本身作为输入数据
    # 可以按需修改为其他生成方式，例如：n = 2 * n + 1 等
    test_n = 10  # 示例规模，可在外部修改或由测试框架传入
    main(test_n)