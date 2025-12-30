def main(n):
    x = 1

    # 第一阶段：确定结果所在的“位数段”
    while n > (10 ** (len(str(x)) - 1) * 9 * len(str(x))):
        n -= 10 ** (len(str(x)) - 1) * 9 * len(str(x))
        x *= 10

    t = len(str(x))
    nadighe = False

    # 第二阶段：进一步细分段
    while nadighe is False:
        qw = 1
        nadighe = True
        while n > (10 ** (len(str(qw)) - 1) * 9 * t):
            n -= 10 ** (len(str(qw)) - 1) * 9 * t
            nadighe = False
            qw *= 10
        x += qw - 1

    # 第三阶段：在具体数字中定位到目标数字
    while n > len(str(x)):
        n -= len(str(x))
        x += 1

    # 输出结果数字
    for i in range(len(str(x))):
        if n != 0:
            s = str(x)[i]
            n -= 1
    print(s)


if __name__ == "__main__":
    # 示例：规模 n 的测试，可按需修改 n
    test_n = 100
    main(test_n)