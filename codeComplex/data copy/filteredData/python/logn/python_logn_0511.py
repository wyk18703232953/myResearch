def main(n: int):
    a = n
    i = 1
    amount = a
    while amount > i * ((10 ** i) - (10 ** (i - 1))):
        amount = amount - i * ((10 ** i) - (10 ** (i - 1)))
        i = i + 1

    x = amount // i
    y = amount % i

    if y == 0:
        if i == 1:
            # print(x % 10)
            pass

        else:
            # print((10 ** (i - 1) + x - 1) % 10)
            pass

    else:
        if i == 1:
            # print(x % 10)
            pass

        else:
            # print(((10 ** (i - 1) + x) // (10 ** (i - y))) % 10)
            pass
if __name__ == "__main__":
    # 示例：调用 main(n) 进行测试，这里给一个默认值
    main(1000)