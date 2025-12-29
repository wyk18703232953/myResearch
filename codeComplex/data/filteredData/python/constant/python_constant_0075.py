def main(n: int):
    # 根据 n 直接运行原逻辑并打印结果
    if n <= 2:
        print(n)
    else:
        if n % 2 != 0:
            print(n * (n - 1) * (n - 2))
        elif n % 3 == 0:
            print((n - 1) * (n - 2) * (n - 3))
        else:
            print(n * (n - 1) * (n - 3))


if __name__ == "__main__":
    # 示例：根据 n 生成测试数据，这里直接给一个测试规模
    test_n = 10
    main(test_n)