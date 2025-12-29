def main(n: int):
    # n 作为规模参数，这里直接用作原程序中的 k
    k = n

    count = 1
    number = 1
    result = 0
    number1 = 1

    # 第一段 while
    while True:
        if number == 1:
            if result + 9 < k:
                result += 9
                number = 20
                number1 = 10
            else:
                break
        elif number == 20:
            if result + 180 < k:
                result += 180
                number += 10
                number1 = 100
            else:
                break
        else:
            if result + 9 * number * 10 ** count < k:
                result += 9 * number * 10 ** count
                number += 10
                count += 1
                number1 *= 10
            else:
                break

    # 第二段 while
    while True:
        if count == 0:
            break
        if result + number * 10 ** count < k:
            result += number * 10 ** count
            number1 += 100 * 10 ** (count - 1)
        else:
            count -= 1

    # 第三段 while
    while True:
        if number == 1:
            break
        if result + number < k:
            result += number
            number1 += 10
        else:
            break

    # 第四段 while
    while True:
        if result + len(str(number1)) >= k:
            print(str(number1)[k - result - 1])
            break
        else:
            number1 += 1
            result += len(str(number1))


if __name__ == "__main__":
    # 示例：根据规模 n 生成一次测试
    # 可以根据需要修改 n 的值
    main(100)