def main(n: int):
    # 这里的 n 本身就是规模参数，直接使用
    result = n ** 2 + (n - 1) ** 2
    print(result)


if __name__ == "__main__":
    # 示例：按需修改 n 以生成不同规模的测试
    test_n = 10
    main(test_n)