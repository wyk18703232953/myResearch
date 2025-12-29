def Fast_power(x, y):
    res = 1
    while y > 0:
        if y % 2 != 0:
            res = res * x
        y //= 2
        x = x * x
    return res


def main(n):
    # 根据规模 n 生成测试数据：
    # 这里设定 m = 2^n + 123，保证和 n 有一定关联性
    m = Fast_power(2, n) + 123

    if n <= 40:
        print(m % Fast_power(2, n))
    else:
        print(m)


if __name__ == "__main__":
    # 示例：调用 main(20)
    main(20)