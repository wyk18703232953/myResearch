def main(n: int):
    t = 1
    while n > 0:
        if n != 3:
            k = n // 2 + n % 2
            # print((str(t) + ' ') * k, end='')
            pass
            n -= k
            t *= 2

        else:
            # print(t, t, t * 3)
            pass
            n = 0


if __name__ == "__main__":
    # 示例：根据需要修改 n 以生成不同规模的测试数据
    test_n = 10
    main(test_n)