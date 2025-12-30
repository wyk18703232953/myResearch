def main(n):
    # 在这里将 n 视作原程序中的 k
    k = n

    i = 0
    r = 1
    while k >= r:
        r += 9 * (i + 1) * 10 ** i
        i += 1
    r = r - (9 * i * 10 ** (i - 1))
    ans = str(((k - r) // i) + 10 ** (i - 1))[(k - r) % i]
    print(ans)


if __name__ == "__main__":
    # 示例：根据 n 生成测试数据
    # 这里直接用 n 作为规模参数调用 main
    # 可按需要修改为不同规模的测试
    test_n = 1000
    main(test_n)