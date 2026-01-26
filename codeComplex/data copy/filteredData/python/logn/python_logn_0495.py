def main(n):
    # 原程序中 a 为输入，这里用 n 作为规模参数来生成 a
    # 你可以按需修改生成方式
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
            # print(f[e - 1])
            pass
            return

if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)