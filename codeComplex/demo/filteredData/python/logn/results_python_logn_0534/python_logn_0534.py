def totaller(i):
    if i == 0:
        return 0

    else:
        return totaller(i - 1) + 9 * (10 ** (i - 1)) * i


def main(n):
    # n 为原程序中的 no_of_digits
    no_of_digits = n

    j = 0
    for i in range(1, 13):
        if no_of_digits >= totaller(i):
            j = i

    kth_digit = (no_of_digits - totaller(j)) // (j + 1)

    if ((no_of_digits - totaller(j)) % (j + 1)) != 0:
        answer = str(kth_digit + 10 ** j)
        # print(answer[((no_of_digits - totaller(j)) % (j + 1)) - 1])
        pass

    else:
        answer = str(kth_digit + 10 ** j - 1)
        # 原代码这里索引结果实际上为 -1
        # print(answer[((no_of_digits - totaller(j)) % (j + 1)) - 1])
        pass
if __name__ == "__main__":
    # 根据 n 生成测试数据，这里示例使用 n = 100
    main(100)