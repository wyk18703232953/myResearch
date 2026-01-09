def main(n: int):
    # 生成测试数据，这里直接将 n 作为原程序中的 k 使用
    k = n

    total_digit = 0
    digit = 1

    while k > total_digit + digit * (pow(10, digit) - pow(10, digit - 1)):
        total_digit += digit * (pow(10, digit) - pow(10, digit - 1))
        digit += 1

    remaining = k - total_digit - 1
    corr_num = str(pow(10, digit - 1) + remaining // digit)
    # print(corr_num[remaining % digit])
    pass
if __name__ == "__main__":
    # 示例：可在此处修改 n 进行测试
    main(15)