def main(n: int):
    # 根据 n 生成测试数据，这里仅使用给定的单个 n
    c = 0
    for j in range(2, 1 + n // 2):
        e = 0
        i = n // j
        e += (i * (i + 1)) // 2
        e -= 1
        if e > 0:
            c += e
    print(c * 4)


if __name__ == "__main__":
    # 示例：可在此处修改 n 以测试不同规模
    test_n = 100
    main(test_n)