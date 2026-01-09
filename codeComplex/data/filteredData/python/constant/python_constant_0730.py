def main(n: int):
    # 生成一个不小于 n 的测试 number，这里设为 n 本身
    number = n

    L = [(i + 1) * 9 * 10 ** i for i in range(12)]

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
        # print(final[-1])
        pass

    else:
        final = str(final + 1)
        # print(final[remainder - 1])
        pass
if __name__ == "__main__":
    # 示例：调用 main(1000) 进行测试，可按需修改 n
    main(1000)