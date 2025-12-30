def main(n: int):
    # 原逻辑中的预处理
    L = [(i + 1) * 9 * 10 ** i for i in range(12)]

    # 根据规模 n 生成测试数据，这里直接使用 n 作为原程序中的 number
    number = n

    exponent = 0
    while number >= 0:
        number -= L[exponent]
        exponent += 1
    exponent -= 1

    number %= L[exponent]
    start = 10 ** exponent
    numDigits = exponent + 1
    final = start + (number // numDigits - 1)
    remainder = number % numDigits

    if remainder == 0:
        final = str(final)
        print(final[-1])
    else:
        final = str(final + 1)
        print(final[remainder - 1])


if __name__ == "__main__":
    # 示例：调用 main(1000)
    main(1000)