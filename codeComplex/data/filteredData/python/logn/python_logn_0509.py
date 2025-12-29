def main(k):
    l = []
    n = []
    total = 0
    multiply = 9

    # 预处理前缀长度和对应的全9数
    for i in range(1, 12):
        s = '9' * i
        n.append(int(s))
        total += i * multiply
        multiply *= 10
        l.append(total)

    if k < 9:
        print(k)
        return

    t = 0
    for i in range(len(l)):
        if k < l[i]:
            t = i
            break

    temp = k - l[t - 1]
    offset = temp % (t + 1)
    value = temp // (t + 1)
    number = n[t - 1] + value

    if offset == 0:
        print(number % 10)
    else:
        number += 1
        offset -= 1
        print(str(number)[offset])


if __name__ == "__main__":
    # 示例：根据规模 n 生成测试数据 k，并调用 main(k)
    # 这里简单用 n 作为 k，你可以根据需要改成任意生成方式
    test_n = 100  # 规模参数，可修改
    main(test_n)