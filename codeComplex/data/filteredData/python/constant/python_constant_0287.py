def main(n):
    # 这里 n 直接作为规模参数使用
    # 原逻辑：输入 n，输出 (n // 2) + 1
    result = (n // 2) + 1
    print(result)


if __name__ == "__main__":
    # 根据规模 n 生成测试数据
    # 例如：直接使用给定 n 作为测试数据
    test_n = 10  # 可以根据需要修改或在其他地方调用 main(n)
    main(test_n)