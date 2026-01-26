def main(n: int):
    # 原程序中：n = int(input()) - 1
    # 这里按“规模 n”直接使用参数 n，不再做 -1 处理
    # 如需完全模拟原行为，可改为：m = n - 1，再用 m 代入公式
    result = 2 * n * (n + 1) + 1
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：根据规模 n 生成测试数据，这里直接指定一个 n 运行
    test_n = 10
    main(test_n)