def main(n: int):
    s = 0
    i = 1
    c = 1
    while s < n:
        s += 9 * i * c
        c += 1
        i *= 10
    n = n - s + 9 * i * (c - 1) // 10
    c = c - 1
    r = n % c
    d = n // c
    k = 10 ** (c - 1) + d
    if r == 0:
        # print(int(str(k - 1)[-1]))
        pass

    else:
        # print(int(str(k)[r - 1]))
        pass
if __name__ == "__main__":
    # 示例：根据规模 n 生成测试数据
    # 这里直接调用 main(n)，用户可自行修改 n 以测试不同规模
    test_n = 1000
    main(test_n)