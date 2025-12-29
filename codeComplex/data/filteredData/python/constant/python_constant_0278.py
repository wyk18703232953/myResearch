def main(n: int):
    # 根据 n 生成测试数据，这里直接使用 n 作为测试数据
    # 原逻辑：读入一个整数 n，输出 int(n/2) + 1
    result = int(n / 2) + 1
    print(result)


if __name__ == "__main__":
    # 示例：自行指定规模 n，用于测试
    # 可根据需要修改或在其他模块中调用 main(n)
    test_n = 10
    main(test_n)