def get_decimal_value_digits(number):
    count = 0
    number = str(number)
    for digit in number:
        count += int(digit)
    return count


def is_big_num(number, s):
    return (number - get_decimal_value_digits(number)) >= s


def main(n):
    # 根据 n 生成测试数据，这里令 s = n // 2 作为示例
    s = n // 2

    start = s
    end = n

    while (end - start) >= 0:
        half = (start + end) // 2
        if is_big_num(half, s):
            end = half - 1
        else:
            start = half + 1

    if not is_big_num(start + 1, s):
        print(0)
    else:
        print(n - start + 1)


# 示例调用
if __name__ == "__main__":
    main(1000000)