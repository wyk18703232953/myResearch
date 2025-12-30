def main(n: int):
    # 根据 n 生成测试数据，这里直接使用 n 作为测试值
    # 如果需要生成多个测试样例，可在此扩展，例如:
    # test_values = [i for i in range(1, n+1)]
    # 并对每个 i 调用下面的计算逻辑。
    
    result = 2 * (n ** 2) - 2 * n + 1
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)