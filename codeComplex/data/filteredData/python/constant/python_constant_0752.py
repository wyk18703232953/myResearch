def main(n: int):
    # 根据 n 生成测试数据，这里直接使用传入的 n 作为规模
    # 如果需要批量测试，可在此处构造多个 n 进行循环调用
    result = 2 * n ** 2 - 2 * n + 1
    print(result)


if __name__ == "__main__":
    # 示例：自行设置一个规模 n 进行调用
    example_n = 10
    main(example_n)