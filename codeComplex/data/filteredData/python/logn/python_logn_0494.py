def main(n: int):
    # 这里将 n 视作原程序中的 k
    k = n

    prev = 0
    nextt = 0
    NumofDigits = 0

    while True:
        prev = nextt
        nextt = nextt + (9 * (10 ** (NumofDigits - 1)) * NumofDigits)
        if k >= prev and k <= nextt:
            break
        NumofDigits += 1

    if NumofDigits == 1:
        print(k)
    else:
        result = (10 ** (NumofDigits - 1)) + int((k - (prev + 1)) / NumofDigits)
        i = 0
        while True:
            if (k - int(prev + 1)) % NumofDigits == i:
                break
            i += 1
        result = str(result)
        print(result[i])


if __name__ == "__main__":
    # 示例：自动生成一个规模 n 的测试数据
    # 这里简单地以 n 本身作为测试用的 k
    # 调用者可以修改下面的值进行测试
    test_n = 15
    main(test_n)