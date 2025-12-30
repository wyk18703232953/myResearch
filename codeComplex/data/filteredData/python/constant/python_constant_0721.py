def main(n):
    # n 为要查询的第 n 个数字在无限整数序列 123456789101112... 中对应的数字字符
    a = n
    c = [1] * 30
    for i in range(1, 20):
        c[i] = 9 * i * pow(10, i - 1)

    for i in range(1, 15):
        if a > c[i]:
            a -= c[i]
        else:
            d = int((a - 1) / i + pow(10, i - 1) - 1)
            e = (a - 1) % i + 1
            f = str(d + 1)
            print(f[e - 1])
            return


if __name__ == "__main__":
    # 示例：查询第 1000 个数字
    main(1000)