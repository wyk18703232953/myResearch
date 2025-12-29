def main(n: int):
    # 根据 n 生成测试数据，这里直接使用传入的 n
    # 若需批量测试，可在此处生成一组 n 的列表并循环调用逻辑
    result = n ** 2 + (n - 1) ** 2
    print(result)


if __name__ == "__main__":
    # 示例：使用规模 n = 10 进行测试
    main(10)