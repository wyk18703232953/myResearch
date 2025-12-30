def main(n: int):
    # 原逻辑：输入 n，如果 n 为奇数输出 (9, n-9)，否则输出 (8, n-8)
    # 这里直接对传入的参数 n 应用相同逻辑
    if n & 1:
        print(9, n - 9)
    else:
        print(8, n - 8)


if __name__ == "__main__":
    # 根据需求生成一个测试规模 n，例如固定给一个值
    # 可以按需修改为随机或序列测试，这里示例使用 n = 100
    test_n = 100
    main(test_n)