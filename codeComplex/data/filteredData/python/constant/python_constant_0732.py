def main(n):
    # 将原先的 k 视作规模参数 n
    k = n

    x = 0
    c = 0
    while x < k:
        x += 9 * (10 ** c) * (c + 1)
        c += 1

    p = (x - k) % c
    k = (10 ** c) - int((x - k) / c) - 1
    k = str(k)

    # 原程序为 print(...)，这里保持同样行为
    print(k[len(k) - p - 1])


if __name__ == "__main__":
    # 示例：根据需要修改 n 的值进行测试
    test_n = 1000
    main(test_n)