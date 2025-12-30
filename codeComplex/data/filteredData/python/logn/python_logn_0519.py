def main(n: int):
    check = True
    t = 0
    tnext = 9

    count = 1
    i = 1
    j = 1
    res = 0

    while check:
        if n <= tnext:
            res = n - t
            check = False
        else:
            count += 1
            if t != 0:
                t = t + 9 * i * j
            else:
                t = 9
            tnext = tnext + 9 * (i + 1) * (j * 10)
            i += 1
            j *= 10

    num1 = res // count
    num2 = res % count

    des = 10 ** (count - 1)
    despac = des + num1

    if num2 == 0:
        despac = str(despac - 1)
        print(despac[-1])
    else:
        despac = str(despac)
        print(despac[num2 - 1])


if __name__ == "__main__":
    # 示例：自动生成一个测试规模 n 调用 main
    # 这里以 n = 100 为例，可按需修改或在外部调用 main(n)
    test_n = 100
    main(test_n)