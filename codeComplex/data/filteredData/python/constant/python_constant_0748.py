def main(n: int):
    # 根据 n 生成测试数据，这里直接使用传入的 n 作为测试规模
    # 原逻辑：print(1 + 2 * ((n - 1) * n))
    result = 1 + 2 * ((n - 1) * n)
    print(result)


if __name__ == "__main__":
    # 示例：自行指定一个规模进行测试
    main(10)