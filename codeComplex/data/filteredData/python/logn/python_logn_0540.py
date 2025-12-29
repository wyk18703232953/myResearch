def main(n: int):
    # 使用 n 作为 k 的规模参数
    k = n

    if k <= 9:
        print(k)
    else:
        s = 9
        num_digits = 1

        # 累加每一位数长度的区间总位数，直到覆盖第 k 位
        while s < k:
            num_digits += 1
            prev_s = s
            s += (10 ** num_digits - 10 ** (num_digits - 1)) * num_digits

        digit_pos = k - (prev_s + 1)
        number = 10 ** (num_digits - 1) + digit_pos // num_digits

        if digit_pos / num_digits != digit_pos // num_digits:
            digit_pos = digit_pos - (digit_pos // num_digits) * num_digits
        else:
            digit_pos = 0

        print(str(number)[digit_pos])


if __name__ == "__main__":
    # 示例：根据规模 n 生成测试数据
    # 可根据需要修改 n 的值进行测试
    test_n = 150
    main(test_n)