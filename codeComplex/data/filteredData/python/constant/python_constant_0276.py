def main(n: int):
    # 这里 n 本身就是规模参数，无需再生成额外数据
    # 按原逻辑输出结果
    print(int(n / 2) + 1)


if __name__ == "__main__":
    # 示例：自行指定规模 n，用于测试
    test_n = 10
    main(test_n)